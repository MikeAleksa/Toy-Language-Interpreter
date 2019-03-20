# Author: Michael Aleksa
# An interpreter for the 'toy language interpreter' final project in CISC 3160 at Brooklyn College, Spring 2019


from Parser import Parser
import sys


file_name: str = str(sys.argv[1])
file = open(file_name, 'r')
print('OUTPUT FROM %s' % file_name)

p = Parser(file.read())
for var_name, value in p.symbol_table.items():
    print('%s = %i' % (var_name, value))
file.close()
