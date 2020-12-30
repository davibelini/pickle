# The final result that will be printed to the screen.

class Number:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f"{self.value}"