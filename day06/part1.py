f = open('input.txt', 'r')
line = f.readline()
f.close()


def index_of_max(banks):
    maximum = max(banks)
    return banks.index(maximum)


def redistribute(banks):
    max_index = index_of_max(banks)
    blocks = banks[max_index]
    banks[max_index] = 0
    current_index = max_index + 1
    while blocks > 0:
        banks[current_index % len(banks)] += 1
        blocks -= 1
        current_index += 1
    return banks


banks = map(int, line.split('\t'))
old_banks = []
bank_str = ''.join(map(str, banks))
redistribution_counter = 0
while bank_str not in old_banks:
    old_banks.append(bank_str)
    banks = redistribute(banks)
    redistribution_counter += 1
print redistribution_counter
