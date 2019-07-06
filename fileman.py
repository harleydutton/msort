import os
from tkinter import filedialog
from tkinter import *

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
		return default_data

def write(relative_path,filename,data,encoding=None):
	path = relative_root+sep+relative_path
	os.makedirs(path,exist_ok=True)
	with open(path+sep+filename,'w+',encoding=encoding) as f:
		f.write(data)

def pickFolder(reason):
	root = Tk()
	folder_path = StringVar()
	def browse_button():
		filename = filedialog.askdirectory()
		folder_path.set(filename)
		root.destroy()
	root.title('Folder Picker')
	temp = StringVar()
	temp.set(reason)
	lbl2 = Label(master=root,textvariable=temp)
	lbl2.grid(row=0, column=0)
	button2 = Button(text="Browse Folders", command=browse_button)
	button2.grid(row=1, column=0)

	mainloop()
	return folder_path.get()