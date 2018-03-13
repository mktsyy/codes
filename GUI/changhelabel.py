##changhelabel

# -*- coding: UTF-8 -*-
from Tkinter import *
import globalvarity

# counter = raw_input("input:  ")
newVar = StringVar()
def counter_label():
	newVar.set(str(globalvarity.COUNTER))
	# def count():
	# # global counter
	# # counter += 1

	# 	if globalvarity.A !=globalvarity.COUNTER:
			
	# 		globalvarity.A = globalvarity.COUNTER
	# 	label.after(1000, count)
	# count()
 

root = Tk()
root.title("Counting Seconds")

label = Label(root, fg="green",textvariable = newVar)
label.pack()
counter_label()
# button = Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
root.mainloop()	

# from Tkinter import *
# import time 
# root = Tk()
# for i in range(1, 101):
# 	time.sleep(1)
# 	val = str(i)
# Label(root, textvariable = val).pack()
# root.update_idletasks()