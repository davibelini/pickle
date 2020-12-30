from nodes import *
from values import Number

class SymbolTable:
  def __init__(self):
    self.symbols = {}
    self.parent = None

  def get(self, name):
    value = self.symbols.get(name, None)
    if value == None and self.parent:
      return self.parent.get(name)
    return value

  def set(self, name, value):
    self.symbols[name] = value

  def remove(self, name):
    del self.symbols[name]
class Interpreter:
  def __init__(self):
    pass

  def visit(self, node):
    method_name = f"visit_{type(node).__name__}" # type(node).__name__ is the name of the 'node' attribute
    method = getattr(self, method_name) # getattr(self, method_name) is the same as self.visit_ + type(self.node)
    return method(node)

  def visit_NumberNode(self, node):
    return Number(node.value)

  def visit_AddNode(self, node):
    return Number(self.visit(node.node_1).value + self.visit(node.node_2).value)

  def visit_SubtractNode(self, node):
    return Number(self.visit(node.node_1).value - self.visit(node.node_2).value)

  def visit_MultiplyNode(self, node):
    return Number(self.visit(node.node_1).value * self.visit(node.node_2).value)

  def visit_DivideNode(self, node):
    try:
      return Number(self.visit(node.node_1).value / self.visit(node.node_2).value)
    except:
      raise Exception("ERROR: math error: cannot divide by 0")

  def visit_MinusNode(self, node):
    return Number(-(self.visit(node.node).value) )

  def visit_PlusNode(self, node):
    return Number(-(self.visit(node.node).value))

  def visit_VarAccessNode(self, node):
    var_name = node.var_name_token.value
    value = global_symbol_table.get(var_name)

    if not value:
      print(f"'{value}' is not defined")

    return value

  def visit_VarAssignNode(self, node):
    var_name = node.var_name_token.value
    value = self.visit(node.value_node)
    global_symbol_table.set(var_name, value)
    return value