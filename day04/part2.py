f = open('input.txt', 'r')
lines = f.readlines()
f.close()

valid = 0
for line in lines:
    words = line.replace('\n', '').split(' ')
    words = map(lambda word: ''.join(sorted(word)), words)
    unique_words = set(words)
    if len(words) == len(unique_words):
        valid += 1
print valid
