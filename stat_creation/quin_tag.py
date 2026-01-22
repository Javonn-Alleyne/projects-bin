import unicodedata
import re

bits = 5
chunk_size = 5

while True:
    text = input("Enter a word: ")
    if text.lower().strip() == 'qw':
        break

    tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
    words = [token for token in tokens if token.strip()]

    all_tags = []
    word_to_tag = {}

    for word in words:
        if not (word.isalpha() or any(c.isalpha() for c in word)):
            all_tags.append(word)
            continue

        # part 1
        # initial input and letter conversion
        # text = input("Enter a word: ")
        # text = "world"
        initial_word = unicodedata.normalize("NFKD", word)
        initial_word = "".join(character for character in initial_word if not unicodedata.combining(character))

        numbers = []
        for character in initial_word:
            if character.isalpha():
                numbers.append(f"{ord(character.upper())-64:02d}")

        result = "".join(numbers) if numbers else "00"
        # print(text, "->", result) 

        #part 2------
        # Binary conversion
        binary_number = int(result) if result else 0
        binary_output = bin(binary_number)[2:] or "0"
        # print(binary_number, "->", binary_output) 

        #bit chunk calculations
        # chunk_size = 5
        # if chunk_size <= 0:
        #     print('size must be > 0')
        # else:
        padding_needed = (-len(binary_output)) % chunk_size
        padded_binary_string = ("0" * padding_needed) + binary_output

        chunks = [padded_binary_string[i:i+chunk_size] for i in range(0, len(padded_binary_string), chunk_size)]
        # print(chunks) 

        # binray to numbers
        vals = [int(chunk, 2) for chunk in chunks]
        # print(f"numbers {vals}") 

        #part 3-----
        # bits = 5
        # val = 47
        tokens_for_word = []
        for val in vals:
            if bits == 5:
                if 1 <= val <= 26:
                    mapped_char = chr(ord('A') + val - 1)#A-Z
                elif 27 <= val <= 31:
                    mapped_char = chr(ord('a') + (val - 27))#a-e
                else:
                    mapped_char = '_'

            elif bits == 6:
                if 1 <= val <= 26:
                    mapped_char = chr(ord('A') + val - 1)#A-Z
                elif 27 <= val <= 52:
                    mapped_char = chr(ord('a') + (val - 27))#a-z
                else:
                    mapped_char = '_'
            else:
                print("chunk sizes are 5 or 6")
                break

            tokens_for_word.append(mapped_char)

        # promote_on_comma = True
        # promote_all_lowercase = False

        # processed_tokens = tokens[:]

        # if promote_all_lowercase:
        #     for i in range(len(processed_tokens)):
        #         token = processed_tokens[i]
        #         if token.islower():

        #             next_position = (ord(token) - ord('a') + 1) % 26
        #             next_letter = chr(ord('a') + next_position)
        #             processed_tokens[i] = next_letter.upper()

        # elif promote_on_comma:
        #     for i in range(len(processed_tokens) - 1):
        #         current_token = processed_tokens[i]
        #         next_token = processed_tokens[i + 1]
                
        #         if current_token.islower() and next_token == ',':

        #             next_position = (ord(current_token) - ord('a') + 1) % 26
        #             next_letter = chr(ord('a') + next_position)
        #             processed_tokens[i] = next_letter.upper()

        processed_tokens = []
        for token in tokens_for_word:
            if token.islower():
                next_position = (ord(token) - ord('a') + 1) % 26
                next_letter = chr(ord('a') + next_position)
                processed_tokens.append(next_letter.upper())
            else:
                processed_tokens.append(token)

        # part 5
        letters = [token for token in processed_tokens if token.isalpha()]

        tri_tag = []
        for letter in letters:
            if letter.isupper():
                tri_tag.append(letter)
            elif letter.islower():
                tri_tag.append(letter.upper())

            if len(tri_tag) == 5:
                break

        while len(tri_tag) < 5:
            tri_tag.append('?')

        tri_tag_string = "".join(tri_tag)
        all_tags.append(tri_tag_string)
        word_to_tag[word.lower()] = tri_tag_string
        # print(f"letters {letters}")
        # print(tri_tag_string)

    print("Results")
    print(f"Initial word:       {text}")
    # print(f"{result}")
    # print(f"Number conversion1: {binary_number}")
    # print(f"Binary conversion:  {binary_output}")
    # print(f"5bit chunks:        {chunks}")
    # print(f"Number conversion2: {vals}")
    # print(f"Letter conversion:  {tokens}")
    # print(f"{processed_tokens}")
    # print(f"{letters}")
    # print(f"Tri-Tag:            {tri_tag_string}")
    print(f"string: {' '.join(all_tags)}")
