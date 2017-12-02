import re

search = re.compile(r"(\d)(?=\1)")

f = open('input.txt', 'r')
line = f.readline()
f.close()
line += line[0]

print sum([int(x) for x in search.findall(line)])
