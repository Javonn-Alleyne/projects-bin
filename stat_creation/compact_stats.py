import random

bits = 6
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