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
sound_played = 0
sound_recovered = 0


def as_value(param):
    global registers
    return registers[param] if param.isalpha() else int(param)


i = 0
while i < len(lines):
    (command, params) = lines[i].replace('\n', '').split(' ', 1)
    params = params.split(' ')
    if command == 'snd':
        sound_played = as_value(params[0])
    elif command == 'set':
        registers[params[0]] = as_value(params[1])
    elif command == 'add':
        registers[params[0]] = registers[params[0]] + as_value(params[1])
    elif command == 'mul':
        registers[params[0]] = registers[params[0]] * as_value(params[1])
    elif command == 'mod':
        registers[params[0]] = registers[params[0]] % as_value(params[1])
    elif command == 'rcv':
        if as_value(params[0]) != 0:
            sound_recovered = sound_played
            break
    elif command == 'jgz':
        if as_value(params[0]) > 0:
            i += as_value(params[1]) - 1
    i += 1
print sound_recovered

