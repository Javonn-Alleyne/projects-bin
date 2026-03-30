# import unicodedata
# from typing import List

word = input("enter a word: ").upper()
print(f"word: {word}")

num_to_char = []
for character in word:
    number = ord(character) -64
    num_to_char.append(number)
print(f"numbers: {num_to_char}")

num_to_binary = ''.join(str(n).zfill(2) for n in num_to_char)
print(f"decimal string: {num_to_binary}")

binary_integer = bin(int(num_to_binary))[2:]
print(f"binary string: {binary_integer}")

chunks = []
chunk_size = 5

padding = (chunk_size - len(binary_integer) % chunk_size) % chunk_size
binary_integer = '0' * padding + binary_integer

binary_string = str(binary_integer)

for i in range(0, len(binary_string), chunk_size):
    chunks.append(binary_string[i:i + chunk_size])
print(f"chunks: {chunks}")

chunk_integers = []
for chunk in chunks:
    chunk_integers.append(int(chunk,2))
print(f"integers: {chunk_integers}")

chunk_letters = []
for integer_letter in chunk_integers:
    if 1 <= integer_letter <= 26:
        chunk_letters.append(chr(ord('A') + integer_letter - 1) )
    elif 27 <= integer_letter <=31: 
        chunk_letters.append(chr(ord('a') + integer_letter - 27) )
    else:
        chunk_letters.append('_')
print(f"letters: {chunk_letters}")

letters =[]
for chunk_letter in chunk_letters:
    if chunk_letter.isalpha():
        letters.append(chunk_letter)

tag = letters[:3]
while len(tag) < 3:
    tag.append("?")
result = ''.join(tag)
print(result)

tag = letters[:5]
while len(tag) < 5:
    tag.append("?")
result = ''.join(tag)
print(result)