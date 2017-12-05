f = open('input.txt', 'r')
lines = f.readlines()
f.close()

checksum = 0
for line in lines:
    numbers = map(int, line.split('\t'))
    minimum = min(numbers)
    maximum = max(numbers)
    checksum += maximum - minimum
print checksum