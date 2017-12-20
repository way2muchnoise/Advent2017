from threading import Thread
import Queue

f = open('input.txt', 'r')
lines = f.readlines()
f.close()


def as_value(registers, param):
    return registers[param] if param.isalpha() else int(param)


class Program(Thread):
    def __init__(self, identifier, send, receive, counter):
        super(Program, self).__init__()
        self.registers = Registers()
        self.id = identifier
        self.registers['p'] = identifier
        self.send = send
        self.receive = receive
        self.counter = counter

    def as_value(self, param):
        return as_value(self.registers, param)

    def run(self):
        i = 0
        while 0 <= i < len(lines):
            (command, params) = lines[i].replace('\n', '').split(' ', 1)
            params = params.split(' ')
            if command == 'snd':
                self.send.put(self.registers[params[0]])
                self.counter += 1
            elif command == 'set':
                self.registers[params[0]] = self.as_value(params[1])
            elif command == 'add':
                self.registers[params[0]] = self.registers[params[0]] + self.as_value(params[1])
            elif command == 'mul':
                self.registers[params[0]] = self.registers[params[0]] * self.as_value(params[1])
            elif command == 'mod':
                self.registers[params[0]] = self.registers[params[0]] % self.as_value(params[1])
            elif command == 'rcv':
                try:
                    self.registers[params[0]] = self.receive.get(True, .5)
                except Queue.Empty:
                    break
            elif command == 'jgz':
                if self.as_value(params[0]) > 0:
                    i += self.as_value(params[1]) - 1
            i += 1


class Registers(dict):
    def __getitem__(self, item):
        try:
            return super(Registers, self).__getitem__(item)
        except KeyError:
            return 0


send_to_0 = Queue.Queue()
send_to_1 = Queue.Queue()
send_counter_0 = 0
send_counter_1 = 0

program_0 = Program(0, send_to_1, send_to_0, send_counter_0)
program_1 = Program(1, send_to_0, send_to_1, send_counter_1)

program_0.start()
program_1.start()

program_0.join()
program_1.join()

print program_1.counter
