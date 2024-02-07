#! python3
# mcb.pyw - 多重剪切板

import shelve
import sys

import pyperclip as pyperclip

if __name__ == '__main__':
    mcbShelf = shelve.open('mcb')

    if len(sys.argv) == 3:
        # Save clipboard content.
        if sys.argv[1].lower() == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        if sys.argv[1].lower() == 'remove':
            del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'clear':
            mcbShelf.clear()
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    mcbShelf.close()

