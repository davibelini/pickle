# Davi Belini
# 27-Dec-2020
# The Rush Programming Language.

from lexer import Lexer
from parse import Parser
from sys import argv
from os import system

system("cls")
system("@echo The Rush Programming Language.")
version = "0.0.1"
system(f"@echo @{version}")

while True:
  text = input(f"rush > ")
  lexer = Lexer(text)
  tokens = lexer.generate_tokens()
  parser = Parser(tokens)
  tree = parser.generate_tree()
  print(tree)