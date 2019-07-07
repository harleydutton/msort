import fileman
import os

fileman.cd('..')
path = 'myfolder'
dump=fileman.listFiles(path)
for e in dump:
	print(e)
print(80*'#')
a,b = zip(*dump)
for e in a:
	print(e)
for e in b:
	print(e)

#dump is a list of tuples
#I want a pair of lists