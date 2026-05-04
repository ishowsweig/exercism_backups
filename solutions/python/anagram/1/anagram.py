def norm(word):
   normal=''
   word = word.lower()
   for char in word:
       if char.isalpha():
           normal += char
   return ''.join(sorted(list(word)))
    
def find_anagrams(word, candidates):
    anagrams = []
    normal_word = norm(word)
    for candidate in candidates:
        if word.lower() != candidate.lower():
            normal_candidate = norm(candidate)
            if len(candidate) == len(word):
                if normal_word == normal_candidate:
                    anagrams.append(candidate)
    return anagrams
