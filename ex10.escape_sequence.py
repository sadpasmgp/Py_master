tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."#slash tells compiler to skip one slash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("Trying other escape sequences")
print("my name i\\s \\sadiq")
print(''' Following are some of the escape sequences in python
\\ to escape backslash
\' to escape single-quote
\" to excape double-quotes
\a for ASCII bell
\b for ASCII backspace
\f for ASCII formfeed
\n for ASCII linefeed
\r for carriage return
\t for horizontal tab
\v for ASCII vertical tab
''')
