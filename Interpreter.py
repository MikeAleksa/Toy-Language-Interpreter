# Author: Michael Aleksa
# An interpreter for the 'toy language interpreter' final project in CISC 3160 at Brooklyn College, Spring 2019
#
# The Interpreter...


from Parser import Parser

p = Parser('x = 1; y = 2; z = ---(x+y)*(x+-y);')
p.program()
for var_name, value in p.symbol_table.items():
    print('%s = %i' % (var_name, value))
