from nodes import *
from types_ import *

class Parser:
  def __init__(self, tokens):
    self.tokens = iter(tokens)
    self.advance()
  
  def advance(self):
    try:
      self.current_token = next(self.tokens)
    except StopIteration:
      self.current_token = None

  def generate_tree(self):
    if self.current_token == None:
      return None
    
    result = self.expr()
    return result

    if self.current_token != None:
      print("ERROR: parsing error")

  def expr(self):
    result = self.term() # Left part of expression
    while self.current_token != None and self.current_token in (TYPE_PLUS, TYPE_MINUS):
      token = self.current_token()
      self.advance()
      if token.type == TYPE_PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif token.type == TYPE_MINUS:
        self.advance()
        result = SubtractNode(result, self.term())
    return result

  def term(self):
    result = self.factor() # Left part of expression
    while self.current_token != None and self.current_token in (TYPE_MULTIPLY, TYPE_DIVIDE):
      token = self.current_token()
      self.advance()
      if token.type == TYPE_MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.factor())
      elif token.type == TYPE_DIVIDE:
        self.advance()
        result = DivideNode(result, self.factor())
    return result

  def factor(self):
    token = self.current_token
    if token != None:
      if token.type == TYPE_LPAR:
        self.advance()
        result = self.expr()
        if self.current_token.type != TYPE_RPAR:
          print("ERROR: missing close parenthesis")
      elif token.type == TYPE_NUMBER:
        self.advance()
        return NumberNode(token.value)
      elif token.type == TYPE_PLUS:
        self.advance()
        return PlusNode(self.factor())
      elif token.type == TYPE_MINUS:
        self.advance()
        return MinusNode(self.factor())
      elif token.type == TYPE_NUMBER:
        self.advance()
        return NumberNode(self.factor())