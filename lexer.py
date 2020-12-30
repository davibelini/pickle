from tokens import Token
from types_ import *
import string

letters = string.ascii_letters
keywords = [
  "as"
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
          print("ERROR: too many decimal points in one number")
        num += '.'
      elif self.current_char.isnumeric():
        num += self.current_char
      self.advance()
    if '.' in num:
      self.tokens.append(Token(TYPE_NUMBER, float(num)))
    else:
      self.tokens.append(Token(TYPE_NUMBER, int(num)))

  def make_identifier(self):
    id_str = ''

    while self.current_char != None and self.current_char in (letters + '0123456789' + '_'):
      id_str += self.current_char
      self.advance()
    
    token_type = TYPE_KEYWORD if id_str in keywords else TYPE_IDENTIFIER
    return Token(token_type, id_str)


  def generate_tokens(self):
    self.tokens = []
    while self.current_char != None:
      if self.current_char in " \t\n":
        self.advance()
      elif self.current_char.isnumeric():
        self.make_number()
      elif self.current_char in letters:
        self.tokens.append(self.make_identifier())
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
      else:
        print("ERROR: tried to work on not allowed character")
        return;
    return self.tokens