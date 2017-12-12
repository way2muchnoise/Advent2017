f = open('input.txt', 'r')
line = f.readline()
f.close()

sequence = map(int, line.split(','))
standard_list = range(0, 256)

skip_value = 0
current_position = 0
for to_reverse in sequence:
    start = current_position
    end = current_position + to_reverse
    if end <= len(standard_list):
        standard_list[start:end] = reversed(standard_list[start:end])
    else:
        to_reverse_list = standard_list[start:]
        end = end % len(standard_list)
        to_reverse_list.extend(standard_list[:end])
        reversed_list = []
        reversed_list[0:] = reversed(to_reverse_list)
        standard_list[start:] = reversed_list[:len(standard_list[start:])]
        standard_list[:end] = reversed_list[-len(standard_list[:end]):]
    current_position += to_reverse + skip_value
    current_position %= len(standard_list)
    skip_value += 1
print standard_list[0] * standard_list[1]
