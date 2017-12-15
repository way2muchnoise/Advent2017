f = open('input.txt', 'r')
lines = f.readlines()
f.close()

factor_a = 16807
factor_b = 48271
max_int = 2147483647

start_a = int(lines[0].replace('\n', '').split(' ')[-1])
a = int((start_a * factor_a) % max_int)
start_b = int(lines[1].replace('\n', '').split(' ')[-1])
b = int((start_b * factor_b) % max_int)

matches = 0
for i in range(0, 40000000):
    lower_a = bin(a)[-16:]
    lower_b = bin(b)[-16:]
    if lower_a == lower_b:
        matches += 1
    a = int((a * factor_a) % max_int)
    b = int((b * factor_b) % max_int)
print matches
