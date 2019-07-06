import os,fileman
path = 'c:\\users\\harley\\desktop\\blah\\'
filename = 'myfile.txt'
data = 'first line\nsecond line\nthird line'
os.makedirs(path,exist_ok=True)
with open(path+filename,'w+') as f:
	f.write(data)
print(data)
print(80*'#')
fileman.init('c:\\users\\harley\\desktop')
fileman.write('this\\is\\a\\path','file1.txt',data+'\nanother line')
fileman.write('this\\is\\a\\path','file1.txt',data)
fileman.write('\\this\\is\\not\\a\\path\\','\\file1.txt',data)
print(fileman.read('my\\second\\filepath','file2.txt','line1\nline2'))
print(fileman.read('this\\is\\a\\path','file1.txt','line1\nline2'))

