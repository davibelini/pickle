from tokens import Token
from types_ import *
from printf import printf
import string

letters = string.ascii_letters
digits = "0123456789"
keywords = [
  "f"
]

class Lexer():  
  def __init__(self, text):
    self.text = iter(text)
    self.current_char = ''
    self.advance()

  def advance(self):
    try:
      self.current_char = next(self.text)
    except StopIteration:
      self.current_char = None

  def make_number(self):
    decimal_count = 0
    num = self.current_char
    self.advance()
    while self.current_char != None and (self.current_char.isnumeric() or self.current_char == '.'): 
      if self.current_char == '.':
        decimal_count += 1
        if decimal_count > 1:
          printf("ERROR: too many decimal points in one number")
        num += '.'
      elif self.current_char.isnumeric():
        num += self.current_char
      self.advance()
    if '.' in num:
      self.tokens.append(Token(TYPE_NUMBER, float(num)))
    else:
      self.tokens.append(Token(TYPE_NUMBER, int(num)))

  def make_equ(self):
    self.advance()
    if self.current_char == '=' and self.current_char != None:
      self.advance()
      return self.tokens.append(Token(TYPE_EQUAL))
    else:
      self.advance()
      return self.tokens.append(Token(TYPE_COLON))
  def make_identifier(self):
    id_string = self.current_char
    self.advance()
    while self.current_char != None and self.current_char in letters + digits + '_':
      id_string += self.current_char
      self.advance()

    token_type = TYPE_KEYWORD if id_string in keywords else TYPE_IDENTIFIER

    return self.tokens.append(Token(token_type, id_string))

  def generate_tokens(self):
    self.tokens = []
    while self.current_char != None:
      if self.current_char in " \t\n":
        self.advance()
      elif self.current_char.isnumeric():
        self.make_number()
      elif self.current_char == '+':
        self.advance()
        self.tokens.append(Token(TYPE_PLUS))
      elif self.current_char == '-':
        self.advance()
        self.tokens.append(Token(TYPE_MINUS))
      elif self.current_char == '*':
        self.advance()
        self.tokens.append(Token(TYPE_MULTIPLY))
      elif self.current_char == '/':
        self.advance()
        self.tokens.append(Token(TYPE_DIVIDE))
      elif self.current_char == '(':
        self.advance()
        self.tokens.append(Token(TYPE_LPAR))
      elif self.current_char == ')':
        self.advance()
        self.tokens.append(Token(TYPE_RPAR))
      elif self.current_char == ':':
        self.make_equ()
      elif self.current_char in letters or self.current_char == '_':
        self.make_identifier()
      else:
        print(f"ERROR: character not allowed: {self.current_char}")
        return "ERROR"
    return self.tokens