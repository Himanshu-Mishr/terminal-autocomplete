from prompt_toolkit.shortcuts import get_input

if __name__ == '__main__':
    answer = get_input('Give me some input: ')
    print('You said: %s' % answer)