from tkinter import ttk
import sqlite3
import tkinter as tk
import random as rndm
from fpdf import FPDF
#root = tk.Tk()
#root.geometry('800x700')
#frame = tk.Frame(root,bg='#FC9483')
#frame.pack(fill='both', expand=1)
#
#tv = ttk.Treeview(frame,columns=(1,2,3,4,5,6,7),show='headings',height='15',)
#tv.pack()
#a1= 'ekrem'
#a2= 'said'
#a3= 'iz'
#a4 = 'lolo'
#a5 = 'zozo'
#a6 = 'roro'
#a7 = 'momo'
#b1 = '2'
#b2= '2'
#b3= '2'
#b4= '2'
#b5= '2'
#b6= '2'
#b7= '2'
#a= [a1,a2,a3,a4,a5,a6,a7]
#b=[b1,b2,b3,b4,b5,b6,b7]
#ab= [a,b]
#
#tv.heading(1, text='Subject')
#tv.heading(2, text='Question Type')
#tv.heading(3, text='Most Seen Question')
#tv.heading(4, text='Most Second Seen Question')
#tv.heading(5, text='Highest Score')
#tv.heading(6, text='Lowest Score')
#tv.heading(7, text='Average Score')
#for i in range(3):
#
#    tv.insert('','end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))
#
#root.mainloop()
#
#connection = sqlite3.connect('database.db')
#cur = connection.cursor()
#a = cur.execute('''SELECT question_text,seen_times FROM mc_question WHERE subject_name = ? AND seen_times=(SELECT MAX(seen_times) FROM mc_question WHERE subject_name = ?) ''',['division','division']).fetchall()
#b = cur.execute('''SELECT question_text,seen_times FROM true_false_question WHERE subject_name = ? AND seen_times=(SELECT MAX(seen_times) FROM true_false_question WHERE subject_name = ?)  ''',['division','division']).fetchall()
#c = cur.execute('''SELECT question_text,seen_times FROM gap_filling_question WHERE subject_name = ? AND seen_times=(SELECT MAX(seen_times) FROM gap_filling_question WHERE subject_name = ?) ''',['division','division']).fetchall()
#z = [a[0],b[0],c[0]]
#rndm.shuffle(z)
#idx, max_value= max(z, key=lambda item: item[1])
##print(z)
#
#z.remove((idx,max_value))
#idx2, max_value2= max(z, key=lambda item: item[1])
#print('SECOND Maximum value:', max_value2, "At index:",idx2)
#print('Maximum value:', max_value, "At index:",idx)
#print(z)
#print(a)
#print(b)
#print(c)

#class Abc:
#    def __init__(self,name):
#        self.name = ''
#
#
#abc = Abc('ekrem')
#abc.name = 5
#print(abc.name)























