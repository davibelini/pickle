# Davi Belini
# 27-Dec-2020
# The Rush Programming Language.

from lexer import Lexer
from parse import Parser
import sys
import os

os.system("cls")

while True:
  text = input("lang > ")
  lexer = Lexer(text)
  tokens = lexer.generate_tokens()
  parser = Parser(tokens)
  tree = parser.generate_tree()
  print(tree)