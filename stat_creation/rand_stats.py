import random
import unicodedata

bits = 6  # Changed to 6-bit to get full a-z range (27-52)
chunk_size = 6

def generate_random_tag_direct(length=3):
    """Generate completely random tag with A-Z and a-z"""
    tag = []
    for _ in range(length):
        # 50% chance uppercase (1-26), 50% lowercase (27-52)
        if random.choice([True, False]):
            tag.append(chr(ord('A') + random.randint(0, 25)))
        else:
            tag.append(chr(ord('a') + random.randint(0, 25)))
    return ''.join(tag)

# Same calculation function as before
    # Your encoding pipeline
    initial_word = unicodedata.normalize("NFKD", word)
    initial_word = "".join(ch for ch in initial_word if not unicodedata.combining(ch))
    
    numbers = []
    for character in initial_word:
        if character.isalpha():
            numbers.append(f"{ord(character.upper())-64:02d}")
    
    result = "".join(numbers) if numbers else "00"
    
    binary_number = int(result) if result else 0
    binary_output = bin(binary_number)[2:] or "0"
    
    padding_needed = (-len(binary_output)) % chunk_size
    padded_binary_string = ("0" * padding_needed) + binary_output
    chunks = [padded_binary_string[i:i+chunk_size] for i in range(0, len(padded_binary_string), chunk_size)]
    
    vals = [int(chunk, 2) for chunk in chunks]
    
    # Map to letters (KEEP lowercase this time!)
    tag_letters = []
    for val in vals:
        if bits == 6:
            if 1 <= val <= 26:
                mapped_char = chr(ord('A') + val - 1)  # A-Z
            elif 27 <= val <= 52:
                mapped_char = chr(ord('a') + (val - 27))  # a-z (KEEP IT)
            else:
                mapped_char = chr(ord('A') + (val % 26))  # Wrap around
        tag_letters.append(mapped_char)
        
        if len(tag_letters) >= length:
            break
    
    # Pad if needed
    while len(tag_letters) < length:
        tag_letters.append(chr(ord('a') + random.randint(0, 25)))
    
    return ''.join(tag_letters[:length])

def calculate_stat_from_tag(tag):
    """Convert tag to stat value"""
    total = 0
    for char in tag:
        if 'A' <= char <= 'Z':
            total += ord(char) - ord('A') + 1  # A=1, Z=26
        elif 'a' <= char <= 'z':
            total += ord(char) - ord('a') + 27  # a=27, z=52
    
    max_possible = 52 * len(tag)  # Max value for this tag length
    stat_percentage = (total / max_possible) * 100
    return total, stat_percentage

# Example usage
print("Generating random stats:")
for stat_name in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
    tag = generate_random_tag_direct(3)
    raw_sum, percentage = calculate_stat_from_tag(tag)
    print(f"{stat_name:15} {tag} -> {raw_sum:3}/156 = {percentage:5.1f}%")