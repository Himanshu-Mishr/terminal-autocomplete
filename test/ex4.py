from __future__ import unicode_literals
from prompt_toolkit.shortcuts import get_input
from prompt_toolkit.history import History
# from pygments.lexers import SqlLexer
from pygments.lexers import BashLexer

def main():
	history = History()

	while True:

		text = get_input('> ', lexer=BashLexer, history=history)
		print('You entered:', text)
	print('GoodBye!')

if __name__ == '__main__':
	main()
