
from Application import *
import tkinter as tk

LARGEFONT = ("Verdana", 25)
MIDDLEFONT = ("Verdana", 12)

#==============creating root window===============================#
root = tk.Tk()
root.title('QUIZ')
root.geometry('1250x650')
root.resizable(False,False)
root.iconphoto(False, tk.PhotoImage(file='logo.png'))
#==================================================================#
#==========================CREATING APPLICATION OBJECT========================================#

app = Application(root)

#===========================================================================#

#==========putting our window into loop=====================#
root.mainloop()
