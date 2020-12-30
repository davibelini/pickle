# Davi Belini
# 27-Dec-2020
# The Pickle Programming Language.

from lexer import Lexer
from parse import Parser
from interpreter import Interpreter, SymbolTable
from sys import argv
from os import system

system("cls")
system("@echo The Pickle Programming Language.")
version = "0.0.1"
system(f"@echo @{version}")

global_symbol_table = SymbolTable()

while True:
  text = input("pickle > ")
  lexer = Lexer(text)
  tokens = lexer.generate_tokens()
  parser = Parser(tokens)
  tree = parser.generate_tree()
  interpreter = Interpreter()
  if not tree:
    print("ERROR: parser tree does not exist")
  else:
    print(interpreter.visit(tree))