# Author: Michael Aleksa
# An interpreter for the 'toy language interpreter' final project in CISC 3160 at Brooklyn College, Spring 2019
#
# The Interpreter...


from Parser import Parser

p = Parser('x = 3*3; y = 4; z = x + y;')

p.program()

print(p.symbol_table)

