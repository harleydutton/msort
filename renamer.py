import os
import string
sep = os.path.sep
path = os.path.dirname(os.path.realpath(__file__))+sep+'poop'
# print(path)

def printPrintable(s):
    if ''.join(c for c in s if c not in string.printable) != '':
        print("#########################################################")
    print(''.join(c for c in s if c in string.printable))

songs = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
for song in songs:
    printPrintable(song)

for song in songs:
    s = ''.join(c for c in song if c in string.printable)
    os.rename(path+sep+song,path+sep+s)

songs = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
for song in songs:
    printPrintable(song)



