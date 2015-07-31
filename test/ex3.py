from __future__ import unicode_literals
from prompt_toolkit.shortcuts import get_input
from prompt_toolkit.history import History

def main():
    # creating instance of history
    # If you want to keep your history across several ``get_input`` calls, you
    # have to create a :class:`History` instance and pass it every time.
    history = History()

    while True:
        text = get_input("> ", history=history)
        print('You entered:', text)
    print('GoodBye!')

if __name__ == '__main__':
    main()
