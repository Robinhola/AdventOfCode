#!/opt/bb/bin/python

import sys

program = []
for line in sys.stdin:
    line = line.rstrip().split(" if ")
    res = {}
    x = line[0].split()
    res["operation"] = {'name' : x[0], 'op' : x[1], 'val' : int(x[2])}
    x = line[1].split()
    res["condition"] = {'name' : x[0], 'op' : x[1], 'val' : int(x[2])}
    program.append(res)

def conditionTest(lval, op, rval):
    if op == "==": return lval == rval
    if op == ">":  return lval >  rval
    if op == ">=": return lval >= rval
    if op == "<":  return lval <  rval
    if op == "<=": return lval <= rval
    if op == "!=": return lval != rval

variables = {}
maximum = 0

def isTrue(condition):
    n, op, val = condition['name'], condition['op'], condition['val']
    if n not in variables: variables[n] = 0
    return conditionTest(variables[n], op, val)

def executeOperation(operation):
    n, op, val = operation['name'], operation['op'], operation['val']
    if n not in variables: variables[n] = 0
    if op == "inc": variables[n] += val
    if op == "dec": variables[n] -= val
    return variables[n]

for line in program:
    condition = line["condition"]
    operation = line["operation"]
    if isTrue(condition):
        val = executeOperation(operation)
        maximum = max(maximum, val)

print max(variables.values())
print maximum
