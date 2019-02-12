# Michael Aleksa
# A TOKENIZER FOR THE TOY LANGUAGE PROJECT FOR CISC 3160

import re

# dict contains the name of the token type (key) and a compiled regex (value) for all tokens in the Toy Language
# Digit, NonZeroDigit, and Letter are not defined here since they are only used within the definition
#   of Literals and Identifiers
tokens = {'Whitespace': re.compile(r'\s'),
          'Semicolon': re.compile(r';'),
          'Equal': re.compile(r'='),
          'Left Paren': re.compile(r'\('),
          'Right Paren': re.compile(r'\)'),
          'Times': re.compile(r'\*'),
          'Plus': re.compile(r'\+'),
          'Minus': re.compile(r'-'),
          'Identifier': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
          'Literal': re.compile(r'0|[1-9][0-9]*'),
          'Invalid Input': re.compile('.')}


class Tokenizer:

    def __init__(self, text):
        self.text = text
        self.endPosition = len(text)
        self.currentPosition = 0

    def tokenize(self):
        # continue to tokenize the string until the current position is at the end of the string
        while self.currentPosition != self.endPosition:
            for pattern in tokens:
                # for all regex patterns in tokens dictionary, check for a match at current position
                match = tokens[pattern].match(self.text, self.currentPosition)
                if match:
                    if pattern == 'Invalid Input':
                        # catch invalid characters and raise an exception
                        # catches anything that does not match another pattern in tokens
                        raise Exception('ERROR: unrecognized character ' + self.text[match.start():match.end()])
                    elif pattern == 'Whitespace':
                        # skip over whitespace
                        self.currentPosition = match.end()
                        break
                    else:
                        # output string and corresponding token type
                        print(self.text[match.start():match.end()] + ' --- ' + pattern)
                        self.currentPosition = match.end()
                        break


# an example of the tokenizer running on two different input strings
try:
    t = Tokenizer('x = (-13 * 2) + var3;')
    t.tokenize()
    print('\n')
    t = Tokenizer('0+B15 _B01 / 9')
    t.tokenize()
except Exception as error:
    print(error)
