# The Interpreter is a command line Python3 utility that can be use to parse a file containing a program written in
#   the toy language, specified in the final project assignment for CISC. 3160 at Brooklyn College, Spring 2019.
#   It accepts any number of file names to interpret from the command line.
#
# interpreter_tl.py uses the Parser from parser_tl.py to create a symbol table of variable names and their assignments


from parser_tl import Parser
import sys


for i in range(1, len(sys.argv)):
    # use command line argument to open a file
    file_name: str = str(sys.argv[i])
    file = open(file_name, 'r')
    print('Output from file: %s' % file_name)

    # try to parse the program and print symbol table
    # if an error is encountered Parser will throw an exception and stop parsing, and the error will be printed
    try:
        p = Parser(file.read())
        for var_name, value in p.symbol_table.items():
            print('%s = %i' % (var_name, value))
    except Exception as error:
        print(error)
    print()

    # close file
    file.close()
