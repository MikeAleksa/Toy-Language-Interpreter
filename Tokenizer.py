# Michael Aleksa
# A TOKENIZER FOR THE TOY LANGUAGE PROJECT FOR CISC 3160

import re

class Tokenizer:

    # dict contains the name of the token type (key) and a compiled regex (value) for all terminals in the toy language
    tokens = {';': re.compile(r';'),
              '=': re.compile(r'='),
              '(': re.compile(r'\('),
              ')': re.compile(r'\)'),
              '*': re.compile(r'\*'),
              '+': re.compile(r'\+'),
              '-': re.compile(r'-'),
              'Identifier': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
              'Literal': re.compile(r'0|[1-9][0-9]*'),
              'Invalid': re.compile('.')}

    # regular expression to match whitespace, which should be removed from input text
    whitespace = re.compile(r'\s+')

    # initialize tokenizer by removing whitespace from text and creating variables to track the current position
    #   in the text, as well as the length of the text
    def __init__(self, text):
        self.text = re.sub(self.whitespace, '', text)
        self.endPosition = len(self.text)
        self.currentPosition = 0

    def read_next_token(self):
        for pattern in self.tokens:
            # for all regex patterns in tokens dictionary, check for a match at current position
            match = self.tokens[pattern].match(self.text, self.currentPosition)
            if match:
                if pattern == 'Invalid':
                    # catches anything that does not match another pattern in tokens
                    raise Exception('ERROR: unrecognized character ' + self.text[match.start():match.end()])
                else:
                    # return tuple containing token (as a string) and the pattern type
                    self.currentPosition = match.end()
                    return {'token': self.text[match.start():match.end()], 'type': pattern}


# an example of the tokenizer running on two different input strings
try:
    t = Tokenizer('x = (-13 * 2) + var3;')
    while t.currentPosition != t.endPosition:
        current_token = t.read_next_token()
        print(current_token)
except Exception as error:
    print(error)
    exit(1)
