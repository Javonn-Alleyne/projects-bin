import textwrap

# enter a sentence / paragraph
'''
Input is split into individual words.
Each word is run through the full TAGES pipeline.
Both TRI-TAG and QUIN-TAG are printed per word.
'''
sentence = input("enter a sentence: ")
print(f"sentence: {sentence}")

# split sentence into words
'''
.split() breaks the sentence on spaces into a list of words.
punctuation is ignored by stripping non-alpha characters from each word.
'''
raw_words = sentence.split()
words = []
for raw in raw_words:
    clean = ''.join(ch for ch in raw if ch.isalpha())
    if clean:
        words.append(clean.upper())
print(f"words: {words}")

# process each word through the TAGES pipeline
'''
each word goes through the exact same steps as the single-word version.
results are collected and printed per word.
'''
quin_tags = []

for word in words:

    # convert each letter to its A1Z26 number
    '''
    ord() converts letters to ASCII.
    since A=65, we minus 64 to get A=1.
    '''
    num_to_char = []
    for character in word:
        number = ord(character) - 64
        num_to_char.append(number)

    # zero-pad each number to 2 digits and concatenate into one decimal string
    '''
    zfill(2) pads single-digit numbers with a leading zero.
    e.g. A=1 -> "01", J=10 -> "10"
    joining them gives one big decimal string e.g. TWO -> "202315"
    '''
    decimal_string = ''.join(str(n).zfill(2) for n in num_to_char)

    # convert the whole decimal string as one integer to binary
    '''
    treat the entire decimal string as a single integer, then convert to binary.
    [2:] removes the 0b prefix.
    '''
    binary_integer = bin(int(decimal_string))[2:]

    # left-pad binary to the nearest multiple of 5
    '''
    pad the LEFT side with zeros so total length is a multiple of 5.
    '''
    chunk_size = 5
    pad_length = (chunk_size - len(binary_integer) % chunk_size) % chunk_size
    binary_integer = '0' * pad_length + binary_integer

    # chunk the string into 5-bit pieces
    chunks = []
    for i in range(0, len(binary_integer), chunk_size):
        chunks.append(binary_integer[i:i + chunk_size])

    # convert chunks from binary to decimal
    '''
    used ai here
    '''
    chunk_integers = []
    for chunk in chunks:
        chunk_integers.append(int(chunk, 2))

    # convert integers to letters
    '''
    used ai here
    check if number is within range of 1-26 (A-Z)
    5-bit chunks max out at 31, so lowercase range is 27-31 -> a-e
    '''
    chunk_letters = []
    for integer_letter in chunk_integers:
        if 1 <= integer_letter <= 26:
            chunk_letters.append(chr(ord('A') + integer_letter - 1))
        elif 27 <= integer_letter <= 31:
            chunk_letters.append(chr(ord('a') + integer_letter - 27))  # a-e only
        else:
            chunk_letters.append('_')


    promoted_letters = []
    for ch in chunk_letters:
        if 'a' <= ch <= 'e':
            next_upper = chr(ord('A') + (ord(ch) - ord('a') + 1) % 26)
            promoted_letters.append(next_upper)
        else:
            promoted_letters.append(ch)

    # collect only alpha characters
    # letters = []
    # for chunk_letter in chunk_letters:
    #     if chunk_letter.isalpha():
    #         letters.append(chunk_letter)
    letters = []
    for chunk_letter in promoted_letters:
        if chunk_letter.isalpha():
            letters.append(chunk_letter)

    # creating the tri-tag
    '''
    used ai here
    '''
    tri_tag = letters[:3]
    while len(tri_tag) < 3:
        tri_tag.append("?")
    tri_result = ''.join(tri_tag)

    # creating the quin-tag
    '''
    used ai here
    '''
    quin_tag = letters[:5]
    while len(quin_tag) < 5:
        quin_tag.append("X")
    quin_tags.append(''.join(quin_tag))
    # quin_result = ''.join(quin_tag)

    # print(f"{word} -> TRI-TAG: {tri_result}  QUIN-TAG: {quin_result}")

print(textwrap.fill(' '.join(quin_tags), width=80))