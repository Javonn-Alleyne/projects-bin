import unicodedata
from typing import List, Tuple

# ---------- Core alphabet helpers ----------
def normalize_letters(s: str) -> str:
    """Normalize accents, drop non-letters, uppercase A-Z."""
    s_norm = unicodedata.normalize("NFKD", s)
    s_norm = "".join(ch for ch in s_norm if not unicodedata.combining(ch))
    return "".join(ch.upper() for ch in s_norm if ch.isalpha())

def a1z26_concat(s: str) -> str:
    """Legacy: map letters to 01..26 and concat (lossy pipeline used by your TRI flow)."""
    s_up = normalize_letters(s)
    nums = [f"{ord(ch)-64:02d}" for ch in s_up]
    return "".join(nums) if nums else "00"

# ---------- Bit utilities ----------
def to_binary_str(num_str: str) -> str:
    """Legacy: Convert concatenated digits to int, then to binary (no '0b')."""
    n = int(num_str) if num_str else 0
    return bin(n)[2:] or "0"

def chunk_bits(bstr: str, size: int) -> List[str]:
    """Left-pad with zeros to a multiple of size, then split."""
    if size <= 0:
        raise ValueError("Chunk size must be > 0")
    pad = (-len(bstr)) % size
    bstr = ("0" * pad) + bstr
    return [bstr[i:i+size] for i in range(0, len(bstr), size)]

def bits_to_int(bits: str) -> int:
    return int(bits, 2)

def ints_to_bits(values: List[int], width: int) -> str:
    """Fixed-width big-endian bit packing for a list of integers."""
    return "".join(f"{v:0{width}b}" for v in values)

def bits_pad_to_byte(bstr: str) -> Tuple[str, int]:
    """Pad bitstring with trailing zeros to full bytes. Return (padded_bits, pad_count)."""
    pad = (-len(bstr)) % 8
    return (bstr + ("0" * pad), pad)

def bits_to_hex(bstr: str) -> str:
    """Bitstring -> hex (uppercase), assumes length is multiple of 8."""
    if len(bstr) % 8 != 0:
        raise ValueError("bits_to_hex requires bit length multiple of 8")
    by = int(bstr, 2).to_bytes(len(bstr)//8, "big")
    return by.hex().upper() if by else ""

def hex_to_bits(h: str) -> str:
    if h == "":
        return ""
    by = bytes.fromhex(h)
    return "".join(f"{b:08b}" for b in by)

# ---------- Mapping rules (legacy lossy tokens) ----------
def map_chunk(val: int, bits: int) -> str:
    """
    Map chunk value to a character by rule:
      5-bit mode:
        1-26 -> A-Z
        27-31 -> a-e
        else  -> '_'
      6-bit mode:
        1-26  -> A-Z
        27-52 -> a-z
        else  -> '_'
    """
    if bits == 5:
        if 1 <= val <= 26:
            return chr(ord('A') + val - 1)
        elif 27 <= val <= 31:
            return chr(ord('a') + (val - 27))  # a..e
        else:
            return '_'
    elif bits == 6:
        if 1 <= val <= 26:
            return chr(ord('A') + val - 1)
        elif 27 <= val <= 52:
            return chr(ord('a') + (val - 27))  # a..z
        else:
            return '_'
    else:
        raise ValueError("Supported chunk sizes are 5 or 6.")

def promote_next_upper(ch: str) -> str:
    """Promote a lowercase a-z to the NEXT uppercase letter (a->B, z->A)."""
    if 'a' <= ch <= 'z':
        nxt = chr(ord('a') + ((ord(ch) - ord('a') + 1) % 26))
        return nxt.upper()
    return ch

def apply_promotion(tokens: List[str], promote_on_comma=True, promote_all_lowercase=False) -> List[str]:
    """
    If promote_on_comma=True: when a token is lowercase and the NEXT token is ',', promote it.
    If promote_all_lowercase=True: promote every lowercase token (handy if you’re not inserting commas).
    """
    out = tokens[:]
    if promote_all_lowercase:
        out = [promote_next_upper(t) if t.islower() else t for t in out]
        return out

    if promote_on_comma:
        for i in range(len(out) - 1):
            if out[i].islower() and out[i+1] == ',':
                out[i] = promote_next_upper(out[i])
    return out

# ---------- TRI-tag derivation (lossy) ----------
def tri_tag_from_tokens(tokens: List[str]) -> str:
    """
    Build a 3-letter human tag from mapped tokens:
      - Take letters only (skip '_' and ','), prefer uppercase.
      - If fewer than 3, pad by promoting lowercase or using 'X'.
    """
    letters = [t for t in tokens if t.isalpha()]
    tri = []
    for t in letters:
        tri.append(t.upper())
        if len(tri) == 3:
            break
    while len(tri) < 3:
        tri.append('X')
    return "".join(tri)

# ---------- LOSSLESS MODE ----------
# Encode each normalized letter as a 5-bit value (A=1..Z=26). This is inherently reversible.
# We store: (version, bit_width, letter_count, pad_bits, payload_hex)
LL_VERSION = 1

def encode_lossless(s: str) -> str:
    """Return a compact lossless token like: R1-5-N{count}-P{pad}-{HEX}"""
    letters = normalize_letters(s)
    values = [(ord(ch) - 64) for ch in letters]  # 1..26
    if any(v < 1 or v > 26 for v in values):
        raise ValueError("Unexpected non A-Z after normalization")

    bit_width = 5
    bitstream = ints_to_bits(values, bit_width)  # 5 bits per letter
    padded_bits, pad = bits_pad_to_byte(bitstream)
    payload_hex = bits_to_hex(padded_bits)
    token = f"R{LL_VERSION}-{bit_width}-N{len(values)}-P{pad}-{payload_hex}"
    return token

def decode_lossless(token: str) -> str:
    """Inverse of encode_lossless. Returns reconstructed normalized letters (A-Z)."""
    # Parse header
    try:
        head, hexpart = token.rsplit("-", 1)
        r, bitw, npart, ppart = head.split("-")
        assert r.startswith("R") and bitw.isdigit()
        version = int(r[1:])
        bit_width = int(bitw)
        assert version == LL_VERSION
        assert npart.startswith("N") and ppart.startswith("P")
        n_letters = int(npart[1:])
        pad_bits = int(ppart[1:])
    except Exception:
        raise ValueError("Invalid lossless token format")

    bits_all = hex_to_bits(hexpart)
    if pad_bits:
        if pad_bits > len(bits_all):
            raise ValueError("Pad count exceeds payload length")
        bits_all = bits_all[:-pad_bits]  # drop trailing pad zeros

    # Now split back into 5-bit groups and take the first n_letters
    groups = [bits_all[i:i+bit_width] for i in range(0, len(bits_all), bit_width)]
    groups = groups[:n_letters]
    vals = [int(g, 2) for g in groups]
    letters = "".join(chr(64 + v) for v in vals)
    return letters

# ---------- Combined runner ----------
def run(bits=5, inject_commas_every=0, promote_on_comma=True, promote_all_lowercase=False):
    """
    bits: 5 or 6 for the *lossy* preview mapping and TRI-tag derivation.
    Lossless mode always uses 5-bit packing (A=1..Z=26) + header to reconstruct.
    """
    print(f"Reality Encoder — lossy bits={bits}, commas_every={inject_commas_every}, "
          f"promote_on_comma={promote_on_comma}, promote_all_lowercase={promote_all_lowercase}")
    print("Enter a word/name (or 'q' to quit).")
    while True:
        s = input("> ")
        if s.lower().strip() == 'q':
            break

        # --- Lossy preview (your original flow) ---
        root = a1z26_concat(s)
        bstr = to_binary_str(root)
        chunks = chunk_bits(bstr, bits)
        vals = [bits_to_int(c) for c in chunks]
        tokens = [map_chunk(v, bits) for v in vals]

        if inject_commas_every and inject_commas_every > 0:
            with_commas = []
            for i, t in enumerate(tokens, 1):
                with_commas.append(t)
                if i % inject_commas_every == 0 and i != len(tokens):
                    with_commas.append(',')
            tokens = with_commas

        tokens = apply_promotion(tokens, promote_on_comma=promote_on_comma,
                                 promote_all_lowercase=promote_all_lowercase)
        tri = tri_tag_from_tokens(tokens)

        # --- Lossless encoding (new) ---
        lossless_token = encode_lossless(s)
        roundtrip = decode_lossless(lossless_token)

        print(f"\nInput:            {s}")
        print(f"Normalized:       {normalize_letters(s)}")
        print(f"--- Lossy preview ---")
        print(f"A1Z26 concat:     {root}")
        print(f"Binary:           {bstr}")
        print(f"Chunks({bits}):      {chunks}")
        print(f"Values:           {vals}")
        print(f"Mapped:           {''.join(tokens)}")
        print(f"TRI tag (lossy):  {tri}")
        print(f"--- Lossless ---")
        print(f"Token:            {lossless_token}")
        print(f"Decoded:          {roundtrip}\n")

if __name__ == "__main__":
    # Default lossy preview uses 5-bit; lossless is always 5-bit packed per letter.
    run(bits=5, inject_commas_every=0, promote_on_comma=True, promote_all_lowercase=False)
