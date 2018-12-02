#!/usr/bin/python
import sys
import time

instructions = []
for line in sys.stdin:
    line = line.rstrip().split(" ")
    instruction = {
        'ins' : line[0],
    }
    if (ord(line[1]) >= ord('a') and ord(line[1]) <= ord('z')):
        instruction['reg']    = line[1]
    else:
        instruction['reg']    = int(line[1])

    if (len(line) == 2):
        pass
    elif len(line[2]) > 1:
        instruction['lookup'] = False
        instruction['val']    = int(line[2])
    elif (ord(line[2]) >= ord('a') and ord(line[2]) <= ord('z')):
        instruction['lookup'] = True
        instruction['src']    = line[2]
    else:
        instruction['lookup'] = False
        instruction['val']    = int(line[2])
    instructions.append(instruction)

int = 0
for i in instructions:
    print(int, i)
    int +=1

reg0 = {}
reg1 = {}
for l in range(ord('a'), ord('z') + 1):
    reg0[chr(l)] = 0
    reg1[chr(l)] = 0

indexes   = [    0,    0 ]
regs      = [ reg0, reg1 ]
snds      = [   [],   [] ]
deadlocks = [ True, True ]
regs[0]['p'] = 0
regs[1]['p'] = 1

program = 0
count   = 0

deadlocks = [ False, False ]
terminate = [ False, False ]

while(not (terminate[0] and terminate[1]) and
      not (deadlocks[0] and deadlocks[1]) and
      (indexes[program] >= 0) and
      (indexes[program] < len(instructions))
      ):

    instruction = instructions[indexes[program]]
    reg         = regs[program]
    other = (program + 1) % 2

    print(program, instruction)

    if len(instruction) > 2:
        if instruction['lookup']:
            val = reg[instruction['src']]
        else:
            val = instruction['val']

    ins = instruction['ins']
    if 'snd' == ins:
        r = instruction['reg']
        if (ord(r) >= ord('a') and ord(r) <= ord('z')):
            val = reg[r]
        else:
            val = int(r)
        snds[other].append(val)
        deadlocks[other] = False
        if program == 1:
            count += 1
    elif 'set' == ins:
        reg[instruction['reg']] = val
    elif 'add' == ins:
        reg[instruction['reg']] += val
    elif 'mul' == ins:
        reg[instruction['reg']] *= val
    elif 'mod' == ins:
        reg[instruction['reg']] %= val
    elif 'rcv' == ins:
        if len(snds[program]) == 0:
            deadlocks[program] = True
            program = other
            continue
        else:
            reg[instruction['reg']] = snds[program].pop(0)
    elif 'jgz' == ins:
        if instruction['reg'] not in reg.keys():
            test = instruction['reg']
        else:
            test = reg[instruction['reg']]
        if test > 0:
            indexes[program] += val
            ind = indexes[program]
            if ind < 0 or ind >= len(instructions):
                terminate[program] = True
                program = other
            continue
    indexes[program] += 1

print(count)

