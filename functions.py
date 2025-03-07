

def caesar(direction: str, text: str, shift: int):
    """
       Encrypts or decrypts a string using the Caesar cipher.
       direction (str): "E" for encryption, "D" for decryption.
       text (str): The input text to be processed.
       shift (int): The number of positions to shift each letter.

       Returns:
       str: Processed text after encryption.
       """

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    output = ""
    str_ = text
    for char in str_:
        if char.lower() not in alphabet:
            output += char
        else:
            letter_pos = alphabet.index(char.lower())

            if direction.upper() == "E":
                letter_pos += shift
            elif direction.upper() == "D":
                letter_pos -= shift

            letter_pos %= len(alphabet)

            new_letter = alphabet[letter_pos]
            if char.isupper():
                output += new_letter.upper()
            else:
                output += new_letter

    return output


if __name__ == "__main__":
    input_text = "the quick brown FOX jumps over THE LAZY DOG"
    input_text_2 = "uif rvjdl cspxo GPY kvnqt pwfs UIF MBAZ EPH"
    print(caesar("E", input_text, 1))
    print(caesar("D", input_text_2, 1))

