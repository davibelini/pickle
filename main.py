from lexer import Lexer
import sys
import os

os.system("cls")

while True:
  text = input("lang > ")
  lexer = Lexer(text)
  result = lexer.generate_tokens()
  print(result)