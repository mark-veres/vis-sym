simmetric = ['i', 'l', 'm', 'o', 'u', 'v', 'w', 'x', 'y']
mirrors = [('p', 'q'), ('d', 'b'), ('q', 'p'), ('b', 'd')]
for s in simmetric:
    mirrors.append((s, s))

words = open('words.txt').read().splitlines()
simmetric_words = []

def is_simmetric(word):
    if len(word)%2 == 0:
        first_half = word[:int(len(word)/2)]
        second_half = word[int(len(word)/2):] [::-1]
    else:
        first_half = word[:int((len(word)-1)/2)]
        second_half = word[int((len(word)+1)/2):] [::-1]
        middle = word[int((len(word)-1)/2)]

        if middle not in simmetric:
            return False
    
    for i, char in enumerate(first_half):
        opposite = second_half[i]
        if (char, opposite) not in mirrors:
            return False

    return True

for w in words:
    if is_simmetric(w):
        simmetric_words.append(w)

print(simmetric_words)