class ErrorLessDict(dict):
    def set(self, x, y, v):
        self.__setitem__(repr(x) + ',' + repr(y), v)

    def find(self, x, y):
        return self.__getitem__(repr(x) + ',' + repr(y))

    def __getitem__(self, item):
        try:
            return super(ErrorLessDict, self).__getitem__(item)
        except KeyError:
            return 0


threshold = 289326
numbers = ErrorLessDict()
x = 0
y = 0
numbers.set(x, y, 1)


def sum_diagonals(x, y):
    total = 0
    total += numbers.find(x + 1, y)  # right
    total += numbers.find(x + 1, y + 1)  # top right
    total += numbers.find(x, y + 1)  # top
    total += numbers.find(x - 1, y + 1)  # top let
    total += numbers.find(x - 1, y)  # left
    total += numbers.find(x - 1, y - 1)  # bottom left
    total += numbers.find(x, y - 1)  # bottom
    total += numbers.find(x + 1, y - 1)  # bottom right
    numbers.set(x, y, total)
    return total


k = 0
do_loop = True
while do_loop:
    k += 1
    for i in range(0, k):
        x += 1  # right
        number = sum_diagonals(x, y)
        if number > threshold:
            print number
            do_loop = False
            break
    for i in range(0, k):
        y += 1  # up
        number = sum_diagonals(x, y)
        if number > threshold:
            print number
            do_loop = False
            break
    k += 1
    for i in range(0, k):
        x -= 1  # left
        number = sum_diagonals(x, y)
        if number > threshold:
            print number
            do_loop = False
            break
    for i in range(0, k):
        y -= 1  # down
        number = sum_diagonals(x, y)
        if number > threshold:
            print number
            do_loop = False
            break
