import os, sys

sep = os.path.sep
relative_root = os.getcwd()+sep+'storage'
def init(absolute_path):
	global relative_root
	os.makedirs(absolute_path,exist_ok=True)
	relative_root=absolute_path

def read(relative_path,filename,default_data=None,encoding=None):
	path = relative_root+sep+relative_path
	os.makedirs(path,exist_ok=True)
	if os.path.isfile(path+sep+filename):
		with open(path+sep+filename,'r',encoding=encoding) as f:
			return f.read()
	elif default_data:
		with open(path+sep+filename,'w+',encoding=encoding) as f:
			f.write(default_data)
		with open(path+sep+filename,'r',encoding=encoding) as f:
			return f.read()

def write(relative_path,filename,data,encoding=None):
	path = relative_root+sep+relative_path
	os.makedirs(path,exist_ok=True)
	with open(path+sep+filename,'w+',encoding=encoding) as f:
		f.write(data)

