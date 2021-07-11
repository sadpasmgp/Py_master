"""
Write a python script to copy one file from another
"""

from sys import argv
#from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input is {len(indata)} bytes long")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "a+")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
