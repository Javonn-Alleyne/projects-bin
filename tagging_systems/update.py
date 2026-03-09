import unicodedata
from typing import List

# simplification update
def a1z26_concat(word):
	result = ""
	for letter in word.upper():
		if letter.isalpha():
			number = ord(letter) - 64
			result += f"{number:02d}" # A = 01 NOT A = 1
	return result if result else "00"
	
def to_binary(num_str):
	return bin(int(num_str))[2:]
	
def split_into_chunks(binary_str, chunk_size=5):
	while len(binary_str) % chunk_size != 0:
		binary_str = "0" + binary_str
	chunks = []
	for i in range(0, len(binary_str), chunk_size):
		chunks.append(binary_str[i:i+chunk_size])
	return chunks
	
def chunk_to_letter(chunk):
	value = int(chunk, 2)
	if 1 <= value <= 26:
		return chr(ord('A') + value - 1)
	else:
		return "_"
		
def tri_tag(word):
	num_str = a1z26_concat(word)
	binary = to_binary(num_str)
	chunks = split_into_chunks(binary)
	letters = []
	for chunk in chunks:
		letter = chunk_to_letter(chunk)
		if letter != "_":
			letters.append(letter)
	tag = letters[:3]
	while len(tag) < 3:
		tag.append("X")
	return "".join(tag)

word = input("enter a word: ")
print(tri_tag(word))