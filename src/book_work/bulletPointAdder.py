# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Sepreate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]   # loop through all indexes for "lines" list
text = '\n'.join(lines)  # add star to each string in "lines" list
pyperclip.copy(text)

# This program can be altered for other text maipulation task that deal with large list.
