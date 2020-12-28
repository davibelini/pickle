class NumberNode:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f"({self.value})"

class PlusNode:
  def __init__(self, node):
    self.node = node

  def __repr__(self):
    return f"(+{self.node})"

class MinusNode:
  def __init__(self, node):
    self.node = node

  def __repr__(self):
    return f"(-{self.node})"

class AddNode:
  def __init__(self, node_1, node_2):
    self.node_1 = node_1
    self.node_2 = node_2

  def __repr__(self):
    return f"({self.node_1} + {self.node_2})"

class SubtractNode:
  def __init__(self, node_1, node_2):
    self.node_1 = node_1
    self.node_2 = node_2

  def __repr__(self):
    return f"({self.node_1} - {self.node_2})"

class MultiplyNode:
  def __init__(self, node_1, node_2):
    self.node_1 = node_1
    self.node_2 = node_2

  def __repr__(self):
    return f"({self.node_1} * {self.node_2})"

class DivideNode:
  def __init__(self, node_1, node_2):
    self.node_1 = node_1
    self.node_2 = node_2

  def __repr__(self):
    return f"({self.node_1} / {self.node_2})"