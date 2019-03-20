# Author: Michael Aleksa
# An interpreter for the 'toy language interpreter' final project in CISC 3160 at Brooklyn College, Spring 2019


from Parser import Parser
import sys


# use the command line argument to open a file
file_name: str = str(sys.argv[1])
file = open(file_name, 'r')
print('Output from file: %s' % file_name)

# try to parse the program - if an error is encountered, print and exit the interpreter
try:
    p = Parser(file.read())
    # print all variables in the symbol table and their values
    for var_name, value in p.symbol_table.items():
        print('%s = %i' % (var_name, value))
except Exception as error:
    print(error)

# close file
file.close()
