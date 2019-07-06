import fileman
import os

fileman.cd('..')
path = 'myfolder'
dump=fileman.list(path)
for e in dump:
	print(e)
