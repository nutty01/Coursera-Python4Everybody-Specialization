#Program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.

fname = input('Enter file name: ')
fh = open(fname)
print(fh.read().upper().strip()) #or for lx in fh: ly=lx.rstrip() print(ly.upper())

