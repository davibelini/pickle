from lexer import Lexer
import sys
import os

os.system("cls")

while True:
  text = input("lang > ")
  if text == 'quit' or 'q':
    sys.exit()
  lexer = Lexer(text)
  result = list(lexer.generate_tokens())
  print(result)