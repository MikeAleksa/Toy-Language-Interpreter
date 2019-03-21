# The Parser is a recursive descent parser that takes some input program and recursively parses the text starting at
#   the program level, until an EOF token or an error is found. Variable names and values are stored and updated in a
#   dictionary representing a symbol table.
#
# To construct a recursive descent parser, ambiguity must be removed from the context free grammar for the toy language
#   given in the assignment statement:
#       Program ::= Assignment*
#       Assignment ::= Identifier = Exp;
#       Exp ::= Term Exp'
#       Exp' ::= + Term Exp' | - Term Exp' | null
#       Term ::= Fact Term'
#       Term' ::= * Fact Term' | null
#       Fact ::= ( Exp ) | - Fact | + Fact | Literal | Identifier
#       Identifier ::= Letter [Letter | Digit]*
#       Letter ::= a|...|z|A|...|Z|_
#       Literal ::= 0 | [1-9] [0-9]*#
#
# parser_tl.py uses tokenizer_tl.py to extract tokens from the input program


from tokenizer_tl import Tokenizer


class Parser:

    # initialize the Parser by loading the program into the Tokenizer and start parsing from the program level
    def __init__(self, text):
        self.t = Tokenizer(text)
        self.current_token = {}
        self.symbol_table = {}
        self.program()

    # read the next token and load it into current_token
    def consume_token(self):
        self.current_token = self.t.read_next_token()

    # check if the next token matches the expected_token
    def match(self, expected_token):
        if self.current_token['type'] != expected_token:
            raise Exception('Syntax Error: expected ' + expected_token +
                            ' but found type ' + self.current_token['type'])

    # parse program
    def program(self):
        while True:
            self.assignment()
            if self.current_token['type'] == 'EOF':
                break

    # parse assignment statements
    def assignment(self):
        self.consume_token()
        if self.current_token['type'] == 'Id':
            var_name = self.current_token['token']
            self.consume_token()
            self.match('=')
            expr = self.expr()
            self.match(';')
            self.symbol_table[var_name] = expr
            return

    # parse expressions
    def expr(self):
        t = self.term()
        return t + self.expr_p()

    # used to eliminate left recursion when parsing expressions
    def expr_p(self):
        if self.current_token['type'] == '+':
            t = self.term()
            return t + self.expr_p()
        elif self.current_token['type'] == '-':
            t = self.term()
            return (-1 * t) + self.expr_p()
        else:
            # if no more expr_p found, return 0 for (term + 0)
            return 0

    # parse terms
    def term(self):
        f = self.factor()
        return f * self.term_p()

    # used to eliminate left recursion when parsing terms
    def term_p(self):
        self.consume_token()
        if self.current_token['type'] == '*':
            f = self.factor()
            return f * self.term_p()
        else:
            # if no more term_p found, return 1 for (factor * 1)
            return 1

    # parse factors
    def factor(self):
        self.consume_token()
        if self.current_token['type'] == 'Lit':
            return int(self.current_token['token'])
        elif self.current_token['type'] == 'Id':
            if self.current_token['token'] in self.symbol_table:
                return self.symbol_table.get(self.current_token['token'])
            else:
                raise Exception('Error: uninitialized variable ' + self.current_token['token'])
        elif self.current_token['type'] == '+':
            return self.factor()
        elif self.current_token['type'] == '-':
            return -1 * self.factor()
        elif self.current_token['type'] == '(':
            exp = self.expr()
            self.match(')')
            return exp
