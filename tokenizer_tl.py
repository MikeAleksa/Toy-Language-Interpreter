# The Tokenizer is used to extract tokens and their type from input text, which are then returned as a dictionary
#   for the Parser to use in its syntax analysis.

import re


class Tokenizer:

    # dictionary contains the type (key) and a compiled regex (value) for all terminals in the toy language
    tokens = {'=': re.compile(r'='),
              ';': re.compile(r';'),
              '+': re.compile(r'\+'),
              '-': re.compile(r'-'),
              '*': re.compile(r'\*'),
              '(': re.compile(r'\('),
              ')': re.compile(r'\)'),
              'Id': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
              'Lit': re.compile(r'0|[1-9][0-9]*'),
              'Inv': re.compile('.')}

    # regular expression to match whitespace, which should be removed from input text
    whitespace = re.compile(r'\s+')

    # initialize tokenizer by removing whitespace from text and creating variables to track the current position
    #   in the text, as well as the length of the text
    def __init__(self, text):
        self.text = re.sub(self.whitespace, '', text)
        self.endPosition = len(self.text)
        self.currentPosition = 0

    # read the next token that starts from currentPosition and return the token and its type
    def read_next_token(self):
        if self.currentPosition < self.endPosition:
            for pattern in self.tokens:
                # for all regex patterns in tokens dictionary, check for a match at current position
                match = self.tokens[pattern].match(self.text, self.currentPosition)
                if match:
                    if pattern == 'Inv':
                        # catch anything that does not match another pattern in tokens
                        raise Exception('ERROR: unrecognized character ' + self.text[match.start():match.end()])
                    else:
                        # return dictionary containing token (as a string) and the pattern type
                        self.currentPosition = match.end()
                        return {'token': self.text[match.start():match.end()], 'type': pattern}
        else:
            # if end of text is reached, return an EOF token
            return {'token': '', 'type': 'EOF'}
