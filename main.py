#!C:\Python38\python.exe

# Davi Belini
# 27-Dec-2020
# The Pickle Programming Language.

from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from sys import argv
from os import system
from printf import printf
from SymbolTable import SymbolTable

global_symbol_table = SymbolTable()

system("cls")
system("@echo The Pickle Programming Language.")
version = "0.0.1"
system(f"@echo @{version}")

line_number = 0

while True:
  text = input(f"pickle > ")
  lexer = Lexer(text)
  tokens = lexer.generate_tokens()
  parser = Parser(tokens)
  tree = parser.generate_tree()
  interpreter = Interpreter(global_symbol_table)
  if not tree:
    print(f"\u007b{line_number}\u007d")
    line_number += 1
    continue
  else:
    print(f"\u007b{line_number}\u007d => {interpreter.visit(tree)}")
    line_number += 1