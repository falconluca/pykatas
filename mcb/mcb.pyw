#! python3
# mcb.pyw - 多重剪切板

import shelve
import sys

import pyperclip as pyperclip

if __name__ == '__main__':
    mcbShelf = shelve.open('mcb')

    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        # Save clipboard content.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

    mcbShelf.close()

