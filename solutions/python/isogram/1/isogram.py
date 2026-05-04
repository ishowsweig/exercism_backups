def is_isogram(string):
    letters = ''.join([char for char in string if char.isalpha()]).lower()
    unique_letters = ''.join(set(letters))
    return len(letters) == len(unique_letters)