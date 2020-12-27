from tokens import Token

TYPE_NUMBER = "NUMBER"
TYPE_PLUS = "PLUS"
TYPE_MINUS = "MINUS"
TYPE_MULTIPLY = "MULTIPLY"
TYPE_DIVIDE = "DIVIDE"

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
  def generate_tokens(self):
    self.tokens = []
    while self.current_char != None:
      if self.current_char in " \t\n":
        self.advance()
      elif self.current_char.isnumeric():
        self.make_number()
    return self.tokens