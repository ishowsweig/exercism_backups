from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):

    ciphertext = ''

    for char in text:
        if char == ' ':
            ciphertext += char

        elif char.isalpha():
            if char.islower():
                original_index = ascii_lowercase.index(char)
                new_index = (original_index + key) % 26
                ciphertext += ascii_lowercase[new_index]
            else:
                original_index = ascii_uppercase.index(char)
                new_index = (original_index + key) % 26
                ciphertext += ascii_uppercase[new_index]

        else:
            ciphertext += char

    return ciphertext
