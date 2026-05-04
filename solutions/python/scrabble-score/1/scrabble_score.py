def score(word):
    score = 0
    for char in word.upper():
        if char in 'AEIOULNRST':
           score += 1
        elif char in 'DG':
            score += 2
        elif char in 'BCMP':
            score += 3
        elif char in 'FHVWY':
            score += 4
        elif char == 'K':
            score += 5
        elif char in 'JX':
            score += 8
        elif char in 'QZ':
            score += 10
        else:
            score += 0
    return score
