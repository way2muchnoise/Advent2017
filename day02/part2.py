f = open('input.txt', 'r')
lines = f.readlines()
f.close()

checksum = 0
for line in lines:
    numbers = map(float, line.split('\t'))
    found = False
    for x in range(0, len(numbers)):
        for y in range(x+1, len(numbers)):
            division = numbers[x] / numbers[y]
            if division.is_integer():
                checksum += division
                found = True
                break
            division_other = numbers[y] / numbers[x]
            if division_other.is_integer():
                checksum += division_other
                found = True
                break
        if found:
            break

print checksum
