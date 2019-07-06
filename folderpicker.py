from tkinter import filedialog
from tkinter import *

def pick(reason):
	root = Tk()
	folder_path = StringVar()
	def browse_button():
		filename = filedialog.askdirectory()
		folder_path.set(filename)
		root.destroy()

	print(reason)
	root.title('Folder Picker')
	temp = StringVar()
	temp.set(reason)
	lbl2 = Label(master=root,textvariable=temp)
	lbl2.grid(row=0, column=0)
	button2 = Button(text="Browse Folders", command=browse_button)
	button2.grid(row=1, column=0)

	mainloop()
	return folder_path.get()
#okay, now just write it to the settings file or something. this isn't ideal but it will do.