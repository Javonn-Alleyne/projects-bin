import unicodedata
from typing import List

# enter a word
'''
All letters entered will be ocnverted to uppercase
'''
word = input("enter a word: ").upper()
print(f"word: {word}")

# conver to a string. must use for loop to get to other chars.
'''
ord() converts all letters to their ASCII.
since A=65, we minus 64 to get A=1.
'''
num_to_char = []
for character in word:
    number = ord(character) - 64
    num_to_char.append(number)
print(f"numbers: {num_to_char}")

# conver numbers to binary
'''
bin() converst all numbers into their binary state.
[2:] removes 0b

!edit:
!zfill(5) -> pads each binary number with leading zeros(0) up ot 5 digits
'''
num_to_binary =[bin(x)[2:] for x in num_to_char]
# num_to_binary =[bin(x)[2:].zfill(5) for x in num_to_char]
print(f"binary: {num_to_binary}")

#combine/concatenate the list
'''
''.join the string together collapsing individual elments into 1 single string
'''
binary_integer =''.join(num_to_binary)
print(f"single binary: {binary_integer}")

#chunk the string(integer) into smaller pieces
'''
create a list for the chunks
set the chunk size to desired value
convert the collasped bianry interget into a string
split the string based on the number of chunks

edit:
ljust (left justify) -> pad the right side with zeroes(0) if short
'''
chunks = []
chunk_size = 5

binary_string = str(binary_integer)

for i in range(0, len(binary_string), chunk_size ):
    chunks.append(binary_string[i:i + chunk_size])
    # chunk = binary_string[i:i + chunk_size]
    # chunk = chunk.ljust(chunk_size, '0') #pad right with zeroes if short
    # chunks.append(chunk)
print(f"chunks: {chunks}")

# convert from binary to decimal
'''
used ai here
'''
chunk_integers = []
for chunk in chunks:
    chunk_integers.append(int(chunk, 2))
print(f"integers: {chunk_integers}")

# convert integers to numbers
'''
used ai here
check if number is within range of 1-26(A-Z)

edit:
handling 27-52 (a-z)
'''
chunk_letters = []
for integer_letter in chunk_integers:
    if 1 <= integer_letter <= 26:
        chunk_letters.append(chr(ord('A') + integer_letter - 1) )
    elif 27 <= integer_letter <=52: 
        chunk_letters.append(chr(ord('a') + integer_letter - 27) )
    else:
        chunk_letters.append('_')
print(f"letters: {chunk_letters}")

# creating the tri tag
'''
used ai here
'''
letters =[]
for chunk_letter in chunk_letters:
    if chunk_letter.isalpha():
        letters.append(chunk_letter)

tag = letters[:3]
while len(tag) < 3:
    tag.append("?")
result = ''.join(tag)
print(result)