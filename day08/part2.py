f = open('input.txt', 'r')
lines = f.readlines()
f.close()


class Registers(dict):
    def __getitem__(self, item):
        try:
            return super(Registers, self).__getitem__(item)
        except KeyError:
            return 0


registers = Registers()
maximum = 0
for line in lines:
    (register, operator, number, iff, to_eval) = line.replace('\n', '').split(' ', 4)
    (eval_register, eval_exp) = to_eval.split(' ', 1)
    if eval('registers[\'' + eval_register + '\'] ' + eval_exp):
        if operator == 'inc':
            registers[register] = registers[register] + int(number)
        elif operator == 'dec':
            registers[register] = registers[register] - int(number)
    if registers[register] > maximum:
        maximum = registers[register]
print maximum
