"""
growth_generator.py

Generates pseudo-random weekly digitization data by sampling deltas
from a normal distribution fitted to real observed growth rates.

Usage:
    python growth_generator.py                  # generates 24 weeks, prints to console
    python growth_generator.py --weeks 52       # generate a full year
    python growth_generator.py --noise 1.5      # 1.5x the observed variability
    python growth_generator.py --seed 42        # reproducible output
    python growth_generator.py --out output.csv # write to file
"""

import csv
import random
import math
import argparse
import statistics
from datetime import date, timedelta
from io import StringIO


# ---------------------------------------------------------------------------
# Column definitions
# ---------------------------------------------------------------------------

# Columns to generate via delta sampling
NUMERIC_COLS = [
    "volumes_digitised",
    "images_digitised",
    "digitised_size",
    "volumes_uploaded",
    "images_uploaded",
    "image_storage_size",
    "not_volumes",
    "not_images",
    "not_storage_size",
    "volume_master",
    "images_master",
    "master_on_viewer",
    "storage_master",
    "estimated_storage_on_viwer",
    "volumes_goobi",
    "images_goobi",
    "upload_goobi",
    "storaged_used",
]

# Columns that stay fixed across all rows
FIXED_COLS = {
    "total_storage": 64,
}

# Columns that should never go below zero
NON_NEGATIVE = set(NUMERIC_COLS)  # all of them in this dataset

# Decimal places to round each column to (keeps output clean)
ROUND_TO = {
    "volumes_digitised":        0,
    "images_digitised":         0,
    "digitised_size":           2,
    "volumes_uploaded":         0,
    "images_uploaded":          0,
    "image_storage_size":       2,
    "not_volumes":              0,
    "not_images":               0,
    "not_storage_size":         2,
    "volume_master":            0,
    "images_master":            0,
    "master_on_viewer":         0,
    "storage_master":           2,
    "estimated_storage_on_viwer": 2,
    "volumes_goobi":            2,
    "images_goobi":             2,
    "upload_goobi":             2,
    "storaged_used":            2,
}


# ---------------------------------------------------------------------------
# Quarter / month helpers
# ---------------------------------------------------------------------------

QUARTER_MAP = {
    1: "first", 2: "first", 3: "first",        # Jan–Mar
    4: "second", 5: "second", 6: "second",      # Apr–Jun
    7: "third", 8: "third", 9: "third",         # Jul–Sep
    10: "fourth", 11: "fourth", 12: "fourth",   # Oct–Dec
}

MONTH_MAP = {
    1: "jan", 2: "feb", 3: "mar", 4: "apr",
    5: "may", 6: "jun", 7: "jul", 8: "aug",
    9: "sep", 10: "oct", 11: "nov", 12: "dec",
}


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def load_seed_data(filepath):
    """Read the CSV and return a list of row dicts."""
    with open(filepath, newline="") as f:
        return list(csv.DictReader(f))


def compute_delta_stats(rows, cols):
    """
    Given seed rows (chronological), compute mean and population stdev
    of week-over-week deltas for each numeric column.

    Returns:
        dict: { col_name: {"mean": float, "stdev": float} }
    """
    stats = {}
    for col in cols:
        vals = [float(r[col]) for r in rows]
        deltas = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        stats[col] = {
            "mean":  statistics.mean(deltas),
            "stdev": statistics.pstdev(deltas),
        }
    return stats


def sample_delta(mean, stdev, noise_scale=1.0):
    """
    Draw one delta from N(mean, stdev * noise_scale).
    Falls back to the mean if stdev is effectively zero.
    """
    effective_stdev = stdev * noise_scale
    if effective_stdev < 1e-9:
        return mean
    return random.gauss(mean, effective_stdev)


def chaos_event(current, delta_stats):
    """
    Randomly trigger one of several chaos modes that temporarily
    distort growth patterns.

    Returns a dict of per-column delta multipliers for this week.
    """
    roll = random.random()

    if roll < 0.05:
        # Catastrophic drop — a bad week, most things shrink or stall
        return {col: random.uniform(-3.0, 0.1) for col in NUMERIC_COLS}

    elif roll < 0.10:
        # Huge spike — massive burst of activity
        return {col: random.uniform(3.0, 10.0) for col in NUMERIC_COLS}

    elif roll < 0.18:
        # Dead week — nearly nothing happens
        return {col: random.uniform(0.0, 0.1) for col in NUMERIC_COLS}

    elif roll < 0.25:
        # Partial chaos — random multiplier per column independently
        return {col: random.uniform(-2.0, 5.0) for col in NUMERIC_COLS}

    else:
        # Normal week — multiplier of 1 (no distortion)
        return {col: 1.0 for col in NUMERIC_COLS}


def drifting_mean(base_mean, week, n_weeks):
    """
    Slowly shift the base mean over time so long runs don't stay flat.
    Applies a gentle sine wave drift on top of a slow upward trend.
    """
    trend    = base_mean * (1 + 0.0003 * week)                        # slow upward drift
    wobble   = base_mean * 0.3 * math.sin(2 * math.pi * week / 52)    # yearly sine wave
    jitter   = base_mean * random.uniform(-0.15, 0.15)                 # per-week random nudge
    return trend + wobble + jitter


def generate_rows(seed_row, delta_stats, n_weeks, noise_scale=1.0, start_date=None):
    """
    Generate n_weeks of chaotic rows starting from seed_row values.

    Each week:
      - The mean itself drifts (trend + sine wave + jitter)
      - Stdev is re-rolled randomly each week
      - Chaos events randomly distort entire weeks
      - Columns are independently noisy (each gets its own multiplier)
    """
    if start_date is None:
        seed_date = date.fromisoformat(seed_row["date"])
        start_date = seed_date + timedelta(weeks=1)

    current = {col: float(seed_row[col]) for col in NUMERIC_COLS}
    results = []

    for week in range(n_weeks):
        current_date = start_date + timedelta(weeks=week)

        # Roll chaos multipliers for this week
        chaos = chaos_event(current, delta_stats)

        row = {}
        row["id"]            = int(seed_row["id"]) + week + 1
        row["quarter"]       = QUARTER_MAP[current_date.month]
        row["month"]         = MONTH_MAP[current_date.month]
        row["date"]          = current_date.isoformat()
        row["total_storage"] = FIXED_COLS["total_storage"]

        for col in NUMERIC_COLS:
            # Drift the mean rather than keeping it fixed
            drifted_mean = drifting_mean(delta_stats[col]["mean"], week, n_weeks)

            # Re-roll stdev each week — some weeks are wild, some calm
            wild_stdev = delta_stats[col]["stdev"] * noise_scale * random.uniform(0.1, 4.0)

            d = sample_delta(drifted_mean, wild_stdev) * chaos[col]

            new_val = current[col] + d

            if col in NON_NEGATIVE:
                new_val = max(0.0, new_val)

            current[col] = new_val
            row[col] = round(new_val, ROUND_TO.get(col, 2))

        results.append(row)

    return results


def write_csv(rows, fieldnames, filepath=None):
    """Write rows to a file or return as a string if filepath is None."""
    output = StringIO() if filepath is None else open(filepath, "w", newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    if filepath is None:
        return output.getvalue()
    output.close()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate pseudo-random digitization data.")
    parser.add_argument("--input",  default="disk_space_data_set.csv",
                        help="Seed CSV file (default: disk_space_data_set.csv)")
    parser.add_argument("--seed-rows", type=int, default=6,
                        help="Number of real rows to use for fitting (default: 6)")
    parser.add_argument("--weeks",  type=int, default=24,
                        help="Number of weeks to generate (default: 24)")
    parser.add_argument("--noise",  type=float, default=1.0,
                        help="Noise scale multiplier on stdev (default: 1.0)")
    parser.add_argument("--seed",   type=int, default=None,
                        help="Random seed for reproducibility (default: None)")
    parser.add_argument("--out",    default="generated_data.csv",
                        help="Output CSV path (default: generated_data.csv)")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # Load and slice seed data
    all_rows   = load_seed_data(args.input)
    seed_rows  = all_rows[:args.seed_rows]
    last_row   = seed_rows[-1]

    # Fit delta distributions
    delta_stats = compute_delta_stats(seed_rows, NUMERIC_COLS)

    # Generate
    new_rows = generate_rows(
        seed_row    = last_row,
        delta_stats = delta_stats,
        n_weeks     = args.weeks,
        noise_scale = args.noise,
    )

    # Field order matches original CSV
    fieldnames = list(all_rows[0].keys())

    if args.out:
        write_csv(new_rows, fieldnames, args.out)
        import os
        print(f"Wrote {args.weeks} rows to {os.path.abspath(args.out)}")
    else:
        print(write_csv(new_rows, fieldnames))


if __name__ == "__main__":
    main()