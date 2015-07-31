from __future__ import unicode_literals
from prompt_toolkit.shortcuts import get_input

def main():
   text = get_input("> ")
   print('You entered:', text)

if __name__ == '__main__':
   main()
