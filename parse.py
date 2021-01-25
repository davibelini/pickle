from nodes import *
from types_ import *
from printf import printf

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

    if self.current_token != None:
      print("ERROR: parsing error")

    return result

  def expr(self):
    if self.current_token.type == TYPE_IDENTIFIER:
      var_name = self.current_token.value
      self.advance()
      if self.current_token.type != TYPE_EQUAL:
        return print("ERROR: missing ':='")
      self.advance()
      var_value = self.expr()
      return VarAssignNode(var_name, var_value)
    else:
      result = self.term() # Left part of expression
      while self.current_token != None and self.current_token.type in (TYPE_PLUS, TYPE_MINUS):
        if self.current_token.type == TYPE_PLUS:
          self.advance()
          result = AddNode(result, self.term())
        elif self.current_token.type == TYPE_MINUS:
          self.advance()
          result = SubtractNode(result, self.term())
      return result

  def term(self):
    result = self.factor() # Left part of expression
    while self.current_token != None and self.current_token.type in (TYPE_MULTIPLY, TYPE_DIVIDE):
      if self.current_token.type == TYPE_MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.factor())
      elif self.current_token.type == TYPE_DIVIDE:
        self.advance()
        result = DivideNode(result, self.factor())
    return result

  def factor(self):
    token = self.current_token
    if token.type == TYPE_LPAR:
      self.advance()
      result = self.expr()
      if self.current_token.type != TYPE_RPAR:
        printf("ERROR: missing close parenthesis")
        return;
      self.advance()
      return result
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
    elif token.type == TYPE_IDENTIFIER:
      self.advance()
      return VarAccessNode(token.value)