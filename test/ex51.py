from __future__ import unicode_literals  # from __future__ imports must occur at the beginning of the file :O
import os
from prompt_toolkit.shortcuts import get_input
from prompt_toolkit.history import History
from prompt_toolkit.contrib.completers import WordCompleter
# from pygments.lexers import SqlLexer
from pygments.style import Style
from pygments.token import Token
from pygments.styles.default import DefaultStyle


class DocumentStyle(Style):
	styles = {
		Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
		Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
		Token.Menu.Completions.ProgressButton: 'bg:#003333',
		Token.Menu.Completions.ProgressBar: 'bg:#00aaaa',
	}
	styles.update(DefaultStyle.styles)

def makeCmdList():
	pathList = os.environ.get('PATH').split(':')
	cmdList = []
	for i in pathList:
		tempCmd = os.listdir(i)
		cmdList.extend(tempCmd)
		cmdList = list(set(cmdList))
	cmdList.sort()
	return cmdList

def main():
	history = History()
	cmd_completer = WordCompleter(makeCmdList(), ignore_case=True)
	while True:
		try:
			text = get_input('> ', completer=cmd_completer, style=DocumentStyle, history=history)
		except EOFError:
			print("Exiting program.")
			return 0
		else:
			print('You entered:', text)

	print('GoodBye!')

if __name__ == '__main__':
	main()
