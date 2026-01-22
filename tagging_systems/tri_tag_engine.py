import unicodedata
from typing import List

# ---------- Core alphabet helpers ----------
def a1z26_concat(s: str) -> str:
    """Normalize accents, drop non-letters, map letters to 01..26 and concat."""
    s_norm = unicodedata.normalize("NFKD", s)
    s_norm = "".join(ch for ch in s_norm if not unicodedata.combining(ch))
    nums = []
    for ch in s_norm:
        if ch.isalpha():
            nums.append(f"{ord(ch.upper())-64:02d}")
    return "".join(nums) if nums else "00"

# ---------- Bit utilities ----------
def to_binary_str(num_str: str) -> str:
    """Convert concatenated digits to int, then to binary (no '0b')."""
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

# ---------- Mapping rules ----------
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
        # next letter in cycle, then uppercase
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

# ---------- TRI-tag derivation ----------
def tri_tag_from_tokens(tokens: List[str]) -> str:
    """
    Build a 3-letter human tag from mapped tokens:
      - Take letters only (skip '_' and ','), prefer uppercase.
      - If fewer than 3, pad by promoting available lowercase to uppercase or using 'X'.
    """
    letters = [t for t in tokens if t.isalpha()]
    # Prefer uppercase; if not enough, promote lowercase on the fly
    tri = []
    for t in letters:
        if t.isupper():
            tri.append(t)
        elif t.islower():
            tri.append(t.upper())
        if len(tri) == 3:
            break
    while len(tri) < 3:
        tri.append('X')
    return "".join(tri)

# ---------- Interactive runner ----------
def run(bits=6, inject_commas_every=0, promote_on_comma=True, promote_all_lowercase=False):
    """
    bits: 5 or 6. Use 6 to allow 27-52 -> a-z (your requested behavior).
    inject_commas_every: if >0, inserts a ',' after every N tokens to demo comma-promotion.
    promote_on_comma: apply the comma-based promotion rule.
    promote_all_lowercase: promote all lowercase to next uppercase (quick test mode).
    """
    print(f"Reality Encoder — bits={bits}, commas_every={inject_commas_every}, "
          f"promote_on_comma={promote_on_comma}, promote_all_lowercase={promote_all_lowercase}")
    print("Enter a word/name (or 'q' to quit).")
    while True:
        s = input("> ")
        if s.lower().strip() == 'q':
            break

        root = a1z26_concat(s)
        bstr = to_binary_str(root)
        chunks = chunk_bits(bstr, bits)
        vals = [bits_to_int(c) for c in chunks]
        tokens = [map_chunk(v, bits) for v in vals]

        # optional: inject commas as delimiters to exercise the promotion rule
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

        print(f"\nInput:        {s}")
        print(f"A1Z26 concat: {root}")
        print(f"Binary:       {bstr}")
        print(f"Chunks({bits}):  {chunks}")
        print(f"Values:       {vals}")
        print(f"Mapped:       {''.join(tokens)}")
        print(f"TRI tag:      {tri}\n")

if __name__ == "__main__":
    # Defaults: 6-bit (so 27–52 map to a–z), no commas, no global promotion.
    run(bits=5, inject_commas_every=0, promote_on_comma=True, promote_all_lowercase=False)
