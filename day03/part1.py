import math


def get_shell_size(number):
    size = math.ceil(math.sqrt(number))
    return size if size % 2 != 0 else size + 1


puzzle_input = 289326

shell_size = int(get_shell_size(puzzle_input))
shell_index = (shell_size - 1) / 2
inner_numbers = math.pow(shell_size - 2, 2)
outer_location = int(puzzle_input - inner_numbers)
distance = shell_index
if shell_size > 1:
    center = (shell_size - 1) / 2
    offset_from_center = center - (outer_location % (shell_size - 1))
    distance += abs(offset_from_center)
print distance
