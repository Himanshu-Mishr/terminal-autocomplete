from __future__ import unicode_literals
from prompt_toolkit.shortcuts import get_input
from prompt_toolkit.history import History
from prompt_toolkit.contrib.completers import WordCompleter

def main():
	history = History()

	while True:
		sql_completer = WordCompleter(['create', 'select', 'insert', 'drop', 'delete', 'from', 'where', 'table'], ignore_case=True)

		text = get_input('> ', completer=sql_completer, history=history)
		print('You entered:', text)
	print('GoodBye!')

if __name__ == '__main__':
	main()
