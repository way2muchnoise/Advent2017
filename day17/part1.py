puzzle_input = 316

step = puzzle_input
spinlock_buffer = [0]
position = 0

for i in range(1, 2018):
    position = ((position + step) % len(spinlock_buffer)) + 1
    spinlock_buffer.insert(position, i)
print spinlock_buffer[spinlock_buffer.index(2017) + 1]
