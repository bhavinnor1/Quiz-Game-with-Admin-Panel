from distutils import command
from Module import *
from Quiz import *
from Question import *
from tkinter import messagebox
import tkinter as tk
import random as rndm
import sqlite3
from tkinter import ttk
# from fpdf import FPDF

'''
To be able to get pdf version of report, you need to install "fpdf" from your command prompt by typing "pip install fpdf"
then you need to import FPDF from fpdf.

'''

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

LARGEFONT = ("Verdana", 25)
MIDDLEFONT = ("Verdana", 12)
TESTFONT = ("Verdana", 10)


class Application:
    def __init__(self,window):
        self.window = window
    #==========CREATING ALL FRAMES THAT ARE NEEDED=============#
        self.main_page = tk.Frame(self.window, bg='lightblue')
        self.main_page.pack(fill='both', expand=1)
        self.quiz_page = tk.Frame(self.window, bg='lightblue')
        self.module_page = tk.Frame(self.window, bg='lightblue')
        self.report_page = tk.Frame(self.window, bg='lightblue')
        self.question_type_page = tk.Frame(self.window, bg='lightblue')
        self.question1_page = tk.Frame(self.window, bg='lightblue')
        self.question2_page = tk.Frame(self.window, bg='lightblue')
        self.question3_page = tk.Frame(self.window, bg='lightblue')
        self.question4_page = tk.Frame(self.window, bg='lightblue')
        self.question5_page = tk.Frame(self.window, bg='lightblue')
        #ZAHID
        self.admin_page = tk.Frame(self.window, bg='lightblue')
        self.add_page = tk.Frame(self.window, bg='lightblue')
        self.update_page = tk.Frame(self.window, bg='lightblue')
        self.delete_page = tk.Frame(self.window, bg='lightblue')
        self.question_page = tk.Frame(self.window, bg='lightblue')
        #ZAHID
        self.add_module_page = tk.Frame(self.window, bg='lightblue')
        self.update_module_page = tk.Frame(self.window, bg='lightblue')
        self.delete_module_page = tk.Frame(self.window, bg='lightblue')
        self.add_subject_page = tk.Frame(self.window, bg='lightblue')
        self.update_subject_page = tk.Frame(self.window, bg='lightblue')
        self.delete_subject_page = tk.Frame(self.window, bg='lightblue')
        self.add_mc_question = tk.Frame(self.window, bg='lightblue')
        self.update_mc_question = tk.Frame(self.window, bg='lightblue')
        self.delete_mc_question = tk.Frame(self.window, bg='lightblue')
        self.add_tf_question = tk.Frame(self.window, bg='lightblue')
        self.update_tf_question = tk.Frame(self.window, bg='lightblue')
        self.delete_tf_question = tk.Frame(self.window, bg='lightblue')
        self.add_gf_question = tk.Frame(self.window, bg='lightblue')
        self.update_gf_question = tk.Frame(self.window, bg='lightblue')
        self.delete_gf_question = tk.Frame(self.window, bg='lightblue')
    #========================================================================#
    #====================CREATING OBJECTS===========================#
        self.main_quiz = Quiz()

        self.module_object_list = {}
        self.subject_object_list = {}
        self.mc_question_object_list = {}
        self.filling_gap_question_object_list = {}
        self.true_false_question_object_list = {}
        self.main_quiz.set_module_list()

        for modules in self.main_quiz.get_module_list():
            main_module = Module(modules)
            self.module_object_list[modules] = main_module
        for modules2 in self.module_object_list.values():
            modules2.set_subject_list()
            for subjects in modules2.get_subject_list():
                main_subject = Subject(subjects)
                self.subject_object_list[subjects] = main_subject

        for subject in self.subject_object_list.values():
            subject.set_multiple_choice_question_list()
            subject.set_gap_filling_question_list()
            subject.set_true_false_question_list()
            for mc_question in subject.get_multiple_choice_question_list():
                main_mc_question = MutlipleChoice(mc_question)
                self.mc_question_object_list[mc_question] = main_mc_question

            for filling_question in subject.get_gap_filling_question_list():
                main_gap_filling_question = GapFilling(filling_question)
                self.filling_gap_question_object_list[filling_question] = main_gap_filling_question

            for true_false_question in subject.get_true_false_question_list():
                main_true_false_question = TrueFalse(true_false_question)
                self.true_false_question_object_list[true_false_question] = main_true_false_question



    #========================================================================#
    #=====================HOME PAGE==========================================#
        self.quiz_btn = tk.Button(self.main_page, text='Quiz', font=LARGEFONT, command=self.quiz_frame)
        self.quiz_btn.pack()
        self.quiz_btn.place(relx=0.45, rely=0.35, relwidth=0.3, relheight=0.3, anchor='ne')
        #ZAHID
        self.admin_btn = tk.Button(self.main_page, text='Admin', font=LARGEFONT, command=self.admin_frame)
        self.admin_btn.pack()
        self.admin_btn.place(relx=0.85, rely=0.35, relwidth=0.3, relheight=0.3, anchor='ne')

        self.main_page.pack(fill='both', expand=1)
    # ========================================================================#

    # ===============CLEAR FRAME FUNCTION FOR DEBUGGING=======================#
    def clear_frame(self,frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    # ========================================================================#

    # ===============FUNCTION TO DISPLAY AND SHOW QUIZ FRAME=======================#
    def quiz_frame(self):
        self.clear_frame(self.quiz_page)
        self.main_page.pack_forget()
        self.quiz_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.quiz_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_main_menu,self.quiz_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        #ZAHID
        main_page_btn = tk.Button(self.quiz_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.quiz_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')
        var = 0
        self.main_quiz.set_module_list()
        for module in self.main_quiz.get_module_list():
            modules_btn = tk.Button(self.quiz_page, text=module.title(), font=LARGEFONT,command=partial(self.module_frame,module))
            modules_btn.pack()
            modules_btn.place(relx=0.75, rely=0.2 + var, relwidth=0.5, relheight=0.1, anchor='ne')
            var += 0.11

    # ========================================================================#

    # ZAHID ===============FUNCTION TO ADMIN AND SHOW ADD,UPDATE & DELETE FRAME=======================#
    def admin_frame(self):
        self.clear_frame(self.admin_page)
        self.main_page.pack_forget()
        self.admin_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.admin_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_main_menu,self.admin_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.admin_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.admin_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')
        
        add_btn = tk.Button(self.admin_page,text='ADD',font=LARGEFONT,command=self.add_frame)
        add_btn.pack()
        add_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        update_btn = tk.Button(self.admin_page,text='UPDATE',font=LARGEFONT,command=self.update_frame)
        update_btn.pack()
        update_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        delete_btn = tk.Button(self.admin_page,text='DELETE',font=LARGEFONT,command=self.delete_frame)
        delete_btn.pack()
        delete_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    # ========================================================================#

    # fiverr - question

##    def status_handler(self,wq): #wq= which question MCQ, Gap filling question or true false questions (I provide them as arguments when you click the button)
##        if self.status=='delete': #self.status= from which page did you came to question_frame (see first line of update, add, delete _frame functions so you understand how)
##            if wq=='mcq': 
##                self.del_mcq()
##            elif wq=='gfq':
##                self.del_gfquestions()
##            elif wq=='tfq':
##                self.del_tfq()
##        elif self.status=='add':
##            if wq=='mcq':
##                self.add_mcq()
##            elif wq=='gfq':
##                self.add_gfq()
##            elif wq=='tfq':
##                self.add_tfq()
##        elif self.status=='update':
##            if wq=='mcq':
##                self.update_mcq()
##            elif wq=='gfq':
##                self.update_gfq()
##            elif wq=='tfq':
##                self.update_tfq()
            
                

    # ZAHID ===============FUNCTION TO SHOW OPTION'S FOR ADD FRAME=======================#
    def add_frame(self):
        self.status='add' # see status handler function
        self.clear_frame(self.add_page)
        self.admin_page.pack_forget()
        self.add_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_admin_frame,self.add_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        add_module_btn = tk.Button(self.add_page,text='ADD MODULE',font=LARGEFONT, command=self.add_module)
        add_module_btn.pack()
        add_module_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        add_subject_btn = tk.Button(self.add_page,text='ADD SUBJECT',font=LARGEFONT, command=self.add_subject)
        add_subject_btn.pack()
        add_subject_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        add_question_btn = tk.Button(self.add_page,text='ADD QUESTION',font=LARGEFONT, command=self.question_frame_add)
        add_question_btn.pack()
        add_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    #fiverr - question

    def amcq(self, tree,table,q,o1,o2,o3,oa,ad,c):
        # make an Insert query and adding neccessary arguments(SQL)
        query="INSERT into "+table+"('question_text','subject_name','option1','option2','option3','option_answer','answer_description','seen_times') VALUES(?,?,?,?,?,?,?,0)"
        #I used try except block so it can show SQL errors to the USER 
        try:
            cursor.execute(query, (q.get(),c.get(),o1.get(),o2.get(),o3.get(),oa.get(),ad.get()))
            connection.commit()
            tree.delete(*tree.get_children()) # delete every row in the table that is visible
            cursor.execute('SELECT * from '+table)
            r=cursor.fetchall() # extracted data in tuple
            n=0 # initialize the counter
            l=[]
            
            for rows in r: # -1 beacuse we dont include seentimes
                    n=n+1 #increment the counter
                    l=[]# make the list empty for the incremented number 
                    l.append(str(n))# add number to the list
                    add=tuple(l)+rows[:-1] #add the number as a tuple so the the first column in the row has index number
                    tree.insert('', tk.END, values=add) # insert values to our table
            messagebox.showinfo('Question Added!','Your Multiple Choice Question was Added')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e) # display exception if any
        
    def add_mcq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.add_mc_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_mc_question,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.add_mc_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_mc_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_mc_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.add_mc_question,text='Multiple Choice Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_2','option_3','option_answer','answer_description')

        tree = ttk.Treeview(self.add_mc_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=5)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=10)
        tree.column("# 6",anchor=tk.W,width=10)
        tree.column("# 7",anchor=tk.W,width=10)
        tree.column("# 8",anchor=tk.W,width=120)

        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_1', text='Option 1')
        tree.heading('option_2', text='Option 2')
        tree.heading('option_3', text='Option 3')
        tree.heading('option_answer', text='Option Answer')
        tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from mc_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# -1 beacuse we dont include seentimes
            n=n+1#increment the counter
            l=[]# make the list empty for the incremented number 
            l.append(str(n))# add number to the list
            add=tuple(l)+rows[:-1] #add the number as a tuple so the the first column in the row has index number
            tree.insert('', tk.END, values=add) # insert values to our table

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)
        # adding x and y scrollbars
        scrollbar = ttk.Scrollbar(self.add_mc_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.add_mc_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        l1 = tk.Label(self.add_mc_question,text='Enter the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.40, rely=0.51, relwidth=0.5, relheight=0.015, anchor='ne')
        qname = tk.Entry(self.add_mc_question)
        qname.pack()
        qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.add_mc_question,text='Option 01:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.233, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        o1 = tk.Entry(self.add_mc_question)
        o1.pack()
        o1.place(relx=0.222, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')
        
        l3 = tk.Label(self.add_mc_question,text='Option 02:',bg='lightblue')
        l3.pack()
        l3.place(relx=0.506, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        o2 = tk.Entry(self.add_mc_question)
        o2.pack()
        o2.place(relx=0.497, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')

        l4 = tk.Label(self.add_mc_question,text='Option 03:',bg='lightblue')
        l4.pack()
        l4.place(relx=0.233, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        o3 = tk.Entry(self.add_mc_question)
        o3.pack()
        o3.place(relx=0.222, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')
        
        l5 = tk.Label(self.add_mc_question,text='Option Answer:',bg='lightblue')
        l5.pack()
        l5.place(relx=0.517, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        oa = tk.Entry(self.add_mc_question)
        oa.pack()
        oa.place(relx=0.497, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')

        l1 = tk.Label(self.add_mc_question,text='Enter Description:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.3975, rely=0.745, relwidth=0.5, relheight=0.02, anchor='ne')
        ad = tk.Entry(self.add_mc_question)
        ad.pack()
        ad.place(relx=0.36, rely=0.77, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.add_mc_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.85, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()

        # tuples dont work properly with dropdown so making tuples to a list
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])#add the first element to the list not the whole tuple
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( self.s_names[0] )
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.add_mc_question, c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.835, relwidth=0.1, relheight=0.05, anchor='ne')

        addbtn = tk.Button(self.add_mc_question,text='ADD',font=MIDDLEFONT, command=lambda:self.amcq(tree,'mc_question',qname,o1,o2,o3,oa,ad,c)) # lambda: to execute the function on button click only not on initializing the current page 
        addbtn.pack()
        addbtn.place(relx=0.41, rely=0.84, relwidth=0.1, relheight=0.05, anchor='ne')

    def agfq(self, tree,table,q,oa,ad,c):
        query="INSERT into "+table+"('question_text','subject_name','option_answer','answer_description','seen_times') VALUES(?,?,?,?,0)"
        try:
            cursor.execute(query, (q.get(),c.get(),oa.get(),ad.get()))
            connection.commit()
            tree.delete(*tree.get_children())# delete all values from table
            cursor.execute('SELECT * from '+table)
            r=cursor.fetchall()
            n=0
            l=[]
            for rows in r:# explained above 
                    n=n+1
                    l=[]
                    l.append(str(n))
                    add=tuple(l)+rows[:-1]
                    tree.insert('', tk.END, values=add)
            messagebox.showinfo('Question Added!','Your Gap Filling Question was Added')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e)

    def add_gfq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.add_gf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_gf_question,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.add_gf_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_gf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_gf_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.add_gf_question,text='Gap Filling Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_answer','answer_description')

        tree = ttk.Treeview(self.add_gf_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=5)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=120)

        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_answer', text='Option Answer')
        tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from gap_filling_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# explained above would be copy paste so i didnt did it
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            tree.insert('', tk.END, values=add)

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)
        scrollbar = ttk.Scrollbar(self.add_gf_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.add_gf_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        l1 = tk.Label(self.add_gf_question,text='Enter the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.40, rely=0.51, relwidth=0.5, relheight=0.015, anchor='ne')
        qname = tk.Entry(self.add_gf_question)
        qname.pack()
        qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.add_gf_question,text='Answer:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.228, rely=0.595, relwidth=0.2, relheight=0.02, anchor='ne')
        oa = tk.Entry(self.add_gf_question)
        oa.pack()
        oa.place(relx=0.223, rely=0.62, relwidth=0.225, relheight=0.05, anchor='n')
        
        l3 = tk.Label(self.add_gf_question,text='Enter Description:',bg='lightblue')
        l3.pack()
        l3.place(relx=0.3975, rely=0.68, relwidth=0.5, relheight=0.02, anchor='ne')
        ad = tk.Entry(self.add_gf_question)
        ad.pack()
        ad.place(relx=0.36, rely=0.705, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.add_gf_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.78, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# convert r tuple to a list
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( self.s_names[0] )
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.add_gf_question , c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.765, relwidth=0.1, relheight=0.05, anchor='ne')

        addbtn = tk.Button(self.add_gf_question,text='ADD',font=MIDDLEFONT, command=lambda:self.agfq(tree,'gap_filling_question',qname,oa,ad,c))# to avoid initialization execution
        addbtn.pack()
        addbtn.place(relx=0.41, rely=0.765, relwidth=0.1, relheight=0.05, anchor='ne')

    def atfq(self, tree,table,q,o1,oa,ad,c):
        query="INSERT into "+table+"('question_text','subject_name','option1','option_answer','answer_description','seen_times') VALUES(?,?,?,?,?,0)"
        try:
            cursor.execute(query, (q.get(),c.get(),o1.get(),oa.get(),ad.get()))# adding argumentsin place of ? in query
            connection.commit()
            tree.delete(*tree.get_children())# remove all data from table
            cursor.execute('SELECT * from '+table)# extract data from database
            r=cursor.fetchall()
            n=0
            l=[]
            for rows in r:# explained above in previous functions
                    n=n+1
                    l=[]
                    l.append(str(n))
                    add=tuple(l)+rows[:-1]
                    tree.insert('', tk.END, values=add)
            messagebox.showinfo('Question Added!','Your True/False Question was Added')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e)

    def add_tfq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.add_tf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_tf_question,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.add_tf_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_tf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_tf_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.add_tf_question,text='True/False Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_answer','answer_description')

        tree = ttk.Treeview(self.add_tf_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=5)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=10)
        tree.column("# 6",anchor=tk.W,width=120)

        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_1', text='Option 1')
        tree.heading('option_answer', text='Option Answer')
        tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from true_false_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# -1 so to not add the last column seen times
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            tree.insert('', tk.END, values=add)

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)
        scrollbar = ttk.Scrollbar(self.add_tf_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.add_tf_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        l1 = tk.Label(self.add_tf_question,text='Enter the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.40, rely=0.51, relwidth=0.5, relheight=0.015, anchor='ne')
        qname = tk.Entry(self.add_tf_question)
        qname.pack()
        qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.add_tf_question,text='Option 01:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.233, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        o1 = tk.Entry(self.add_tf_question)
        o1.pack()
        o1.place(relx=0.222, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')

        l4 = tk.Label(self.add_tf_question,text='Option Answer:',bg='lightblue')
        l4.pack()
        l4.place(relx=0.243, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        oa = tk.Entry(self.add_tf_question)
        oa.pack()
        oa.place(relx=0.222, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')

        l1 = tk.Label(self.add_tf_question,text='Enter Description:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.3975, rely=0.745, relwidth=0.5, relheight=0.02, anchor='ne')
        ad = tk.Entry(self.add_tf_question)
        ad.pack()
        ad.place(relx=0.36, rely=0.77, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.add_tf_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.85, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()# comes in a tuple data type
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# changing the tuple to a list
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( self.s_names[0] )
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.add_tf_question , c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.835, relwidth=0.1, relheight=0.05, anchor='ne')

        addbtn = tk.Button(self.add_tf_question,text='ADD',font=MIDDLEFONT, command=lambda:self.atfq(tree,'true_false_question',qname,o1,oa,ad,c))# avoid initialization execution
        addbtn.pack()
        addbtn.place(relx=0.41, rely=0.84, relwidth=0.1, relheight=0.05, anchor='ne')

    #fiverr

    def addm(self,tbox):
        query=' INSERT INTO module(module_name) VALUES(?) '
        cursor.execute(query, (tbox.get(),))# tbox.get() get the values from the textbox
        tbox.delete(0,'end')
        connection.commit()

    def add_module(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.add_module_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_module_page ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.add_module_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_module_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_module_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete = tk.Label(self.add_module_page,text='ADD MODULE',bg='lightblue',font=LARGEFONT)
        delete.pack()
        delete.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.add_module_page,text='Enter the name of the Module:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.50, rely=0.44, relwidth=0.6, relheight=0.05, anchor='n')

        mname = tk.Entry(self.add_module_page)
        mname.pack()
        mname.place(relx=0.50, rely=0.55, relwidth=0.2, relheight=0.05, anchor='n')
        
        add_btn = tk.Button(self.add_module_page,text='Add',command=lambda:self.addm(mname))# avoid initialization execution of the function
        add_btn.pack()
        add_btn.place(relx=0.55, rely=0.66, relwidth=0.1, relheight=0.05, anchor='ne')

    def adds(self,tbox,c):
        query=' INSERT INTO subject(subject_name,module_name,attempts,total_score,lowest_score_out_of_five,highest_score_out_of_five) VALUES(?,?,?,?,?,?) '
        cursor.execute(query, (tbox.get(),c.get(),0,0,6,-1)) # # tbox.get() get the values from the textbox 0,0,6,-1 added default values
        tbox.delete(0,'end')# delete the data in the entry box
        connection.commit()# save the changes in database

    def add_subject(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.add_subject_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.add_subject_page ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.add_subject_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.add_subject_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.add_subject_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        add = tk.Label(self.add_subject_page,text='ADD SUBJECT',bg='lightblue',font=LARGEFONT)
        add.pack()
        add.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.add_subject_page,text='Enter the name of the Subject:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.50, rely=0.44, relwidth=0.6, relheight=0.05, anchor='n')

        mname = tk.Entry(self.add_subject_page)
        mname.pack()
        mname.place(relx=0.50, rely=0.50, relwidth=0.2, relheight=0.05, anchor='n')

        sm = tk.Label(self.add_subject_page,text='Select Module:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.05, anchor='n')

        cursor.execute('SELECT module_name from module')
        r=cursor.fetchall()
        module_names = []
        for row in r:
            module_names.append(row[0])# convert tuple to a list of subjects
        print(r)
        print(module_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( module_names[0] )
          
        # Create Dropdown menu
        self.dropad1 = tk.OptionMenu( self.add_subject_page , c, *module_names )
        self.dropad1.pack()
        self.dropad1.place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.05, anchor='ne')
        
        add_btn = tk.Button(self.add_subject_page,text='Add',command=lambda:self.adds(mname,c))# avoid executing the function when creating the page
        add_btn.pack()
        add_btn.place(relx=0.55, rely=0.66, relwidth=0.1, relheight=0.05, anchor='ne')

    # ========================================================================#    

    # ZAHID ===============FUNCTION TO SHOW OPTION's FOR UPDATE FRAME=======================#
    def update_frame(self):
        self.status='update'# update status to update page
        self.clear_frame(self.update_page)
        self.admin_page.pack_forget()
        self.update_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_admin_frame,self.update_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        update_module_btn = tk.Button(self.update_page,text='UPDATE MODULE',font=LARGEFONT, command=self.update_module)
        update_module_btn.pack()
        update_module_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        update_subject_btn = tk.Button(self.update_page,text='UPDATE SUBJECT',font=LARGEFONT, command=self.update_subject)
        update_subject_btn.pack()
        update_subject_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        update_question_btn = tk.Button(self.update_page,text='UPDATE QUESTION',font=LARGEFONT, command=self.question_frame_update)
        update_question_btn.pack()
        update_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    #fiverr - question

    def entrybox_updater(self, event):# this function deletes and inserts the selected data on every single click with the help of .bind inbuilt function
        print(event)
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']#extract the current row data to record
        self.qname.delete(0,'end')# delete the data from the entry box
        self.qname.insert(0,record[1])#insert the current selected row's 1st index to the entry box
        self.c.set(record[2])# change the dropdown value to records second index value
        self.o1.delete(0,'end')#same as above
        self.o1.insert(0,record[3])
        self.o2.delete(0,'end')
        self.o2.insert(0,record[4])
        self.o3.delete(0,'end')
        self.o3.insert(0,record[5])
        self.oa.delete(0,'end')
        self.oa.insert(0,record[6])
        self.ad.delete(0,'end')
        self.ad.insert(0,record[7])
        
    def umcq(self):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']# extract current selected row data to record 
        query="UPDATE mc_question SET question_text='"+self.qname.get()+"' ,subject_name='"+self.c.get()+"', option1='"+self.o1.get()+"', option2='"+self.o2.get()+"', option3='"+self.o3.get()+"', option_answer='"+self.oa.get()+"', answer_description='"+self.ad.get()+"' WHERE question_text=?"
        try:
            print(record[1])
            cursor.execute(query, (record[1],))# adding subject name as argument
            connection.commit()
            self.tree.delete(*self.tree.get_children())# delete the data from the table
            cursor.execute('SELECT * from mc_question')
            r=cursor.fetchall()
            n=0
            l=[]
            for rows in r:# explained above
                    n=n+1
                    l=[]
                    l.append(str(n))
                    add=tuple(l)+rows[:-1]
                    self.tree.insert('', tk.END, values=add)
            messagebox.showinfo('Question Updated!','Your Multiple Choice Question was Updated')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e)

        # delete the data after completed
        self.qname.delete(0,'end')
        self.o1.delete(0,'end')
        self.o2.delete(0,'end')
        self.o3.delete(0,'end')
        self.oa.delete(0,'end')
        self.ad.delete(0,'end')
        
        

    def update_mcq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.update_mc_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_mc_question,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.update_mc_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_mc_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_mc_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.update_mc_question,text='Multiple Choice Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_2','option_3','option_answer','answer_description')

        self.tree = ttk.Treeview(self.update_mc_question, columns=columns, show='headings')
        self.tree.column("# 1",anchor=tk.CENTER,width=5)
        self.tree.column("# 2",anchor=tk.W,width=120)
        self.tree.column("# 3",anchor=tk.W,width=10)
        self.tree.column("# 4",anchor=tk.W,width=10)
        self.tree.column("# 5",anchor=tk.W,width=10)
        self.tree.column("# 6",anchor=tk.W,width=10)
        self.tree.column("# 7",anchor=tk.W,width=10)
        self.tree.column("# 8",anchor=tk.W,width=120)

        # define headings
        self.tree.heading('roll_no', text='No.')
        self.tree.heading('question_text', text='Question text')
        self.tree.heading('subject_name', text='Subject name')
        self.tree.heading('option_1', text='Option 1')
        self.tree.heading('option_2', text='Option 2')
        self.tree.heading('option_3', text='Option 3')
        self.tree.heading('option_answer', text='Option Answer')
        self.tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from mc_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# explained above
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            self.tree.insert('', tk.END, values=add)

        self.tree.pack()
        self.tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)

        self.tree.bind('<<TreeviewSelect>>', self.entrybox_updater)# call this function every time you select a value in the table
        
        scrollbar = ttk.Scrollbar(self.update_mc_question, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.update_mc_question, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        l1 = tk.Label(self.update_mc_question,text='Update the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.405, rely=0.51, relwidth=0.5, relheight=0.02, anchor='ne')
        self.qname = tk.Entry(self.question_page)
        self.qname.pack()
        self.qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.update_mc_question,text='Option 01:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.233, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        self.o1 = tk.Entry(self.update_mc_question)
        self.o1.pack()
        self.o1.place(relx=0.222, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')
        
        l3 = tk.Label(self.update_mc_question,text='Option 02:',bg='lightblue')
        l3.pack()
        l3.place(relx=0.506, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        self.o2 = tk.Entry(self.update_mc_question)
        self.o2.pack()
        self.o2.place(relx=0.497, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')

        l4 = tk.Label(self.update_mc_question,text='Option 03:',bg='lightblue')
        l4.pack()
        l4.place(relx=0.233, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        self.o3 = tk.Entry(self.update_mc_question)
        self.o3.pack()
        self.o3.place(relx=0.222, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')
        
        l5 = tk.Label(self.update_mc_question,text='Option Answer:',bg='lightblue')
        l5.pack()
        l5.place(relx=0.517, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        self.oa = tk.Entry(self.update_mc_question)
        self.oa.pack()
        self.oa.place(relx=0.497, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')

        l1 = tk.Label(self.update_mc_question,text='Update Description:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.4025, rely=0.745, relwidth=0.5, relheight=0.02, anchor='ne')
        self.ad = tk.Entry(self.update_mc_question)
        self.ad.pack()
        self.ad.place(relx=0.36, rely=0.77, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.update_mc_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.85, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# convert r tuple to list
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        self.c = tk.StringVar()
          
        # initial menu text
        self.c.set( self.s_names[0] )
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.update_mc_question , self.c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.835, relwidth=0.1, relheight=0.05, anchor='ne')

        addbtn = tk.Button(self.update_mc_question,text='UPDATE',font=MIDDLEFONT, command=self.umcq)
        addbtn.pack()
        addbtn.place(relx=0.41, rely=0.84, relwidth=0.1, relheight=0.05, anchor='ne')

    def eu2(self, event): #entry Updater
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']# extract data from current selected row
        self.qname.delete(0,'end')# delete the data in textbox
        self.qname.insert(0,record[1])# insert new extracted data into textbox
        self.c.set(record[2])# same as above
        self.oa.delete(0,'end')
        self.oa.insert(0,record[3])
        self.ad.delete(0,'end')
        self.ad.insert(0,record[4])

    def ugfq(self):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']# extract data from current selected row
        query="UPDATE gap_filling_question SET question_text='"+self.qname.get()+"' ,subject_name='"+self.c.get()+"', option_answer='"+self.oa.get()+"', answer_description='"+self.ad.get()+"' WHERE question_text=?"
        try:
            print(record[1])
            cursor.execute(query, (record[1],))
            connection.commit()
            self.tree.delete(*self.tree.get_children())# delete every row from the table
            cursor.execute('SELECT * from gap_filling_question')
            r=cursor.fetchall()# fetch the tables data into r
            n=0
            l=[]
            for rows in r:# explained above in add
                    n=n+1
                    l=[]
                    l.append(str(n))
                    add=tuple(l)+rows[:-1]
                    self.tree.insert('', tk.END, values=add)# add data to the table
            messagebox.showinfo('Question Updated!','Your Gap Filling Question was Updated')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e)

        # delete data in textbox after finished adding data to database
        self.qname.delete(0,'end')
        self.oa.delete(0,'end')
        self.ad.delete(0,'end')

    def update_gfq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.update_gf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_gf_question ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.update_gf_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_gf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_gf_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.update_gf_question,text='Gap Filling Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_answer','answer_description')

        self.tree = ttk.Treeview(self.update_gf_question, columns=columns, show='headings')
        self.tree.column("# 1",anchor=tk.CENTER,width=5)
        self.tree.column("# 2",anchor=tk.W,width=120)
        self.tree.column("# 3",anchor=tk.W,width=10)
        self.tree.column("# 4",anchor=tk.W,width=10)
        self.tree.column("# 5",anchor=tk.W,width=120)

        # define headings
        self.tree.heading('roll_no', text='No.')
        self.tree.heading('question_text', text='Question text')
        self.tree.heading('subject_name', text='Subject name')
        self.tree.heading('option_answer', text='Option Answer')
        self.tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from gap_filling_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# explained above in add
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            self.tree.insert('', tk.END, values=add)

        self.tree.pack()
        self.tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)
        scrollbar = ttk.Scrollbar(self.update_gf_question, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.update_gf_question, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        self.tree.bind('<<TreeviewSelect>>', self.eu2)# run eu2 function every time you select a data in the table

        l1 = tk.Label(self.update_gf_question,text='Update the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.40, rely=0.51, relwidth=0.5, relheight=0.015, anchor='ne')
        self.qname = tk.Entry(self.update_gf_question)
        self.qname.pack()
        self.qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.update_gf_question,text='Answer:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.228, rely=0.595, relwidth=0.2, relheight=0.02, anchor='ne')
        self.oa = tk.Entry(self.update_gf_question)
        self.oa.pack()
        self.oa.place(relx=0.223, rely=0.62, relwidth=0.225, relheight=0.05, anchor='n')
        
        l3 = tk.Label(self.update_gf_question,text='Update Description:',bg='lightblue')
        l3.pack()
        l3.place(relx=0.3975, rely=0.68, relwidth=0.5, relheight=0.02, anchor='ne')
        self.ad = tk.Entry(self.update_gf_question)
        self.ad.pack()
        self.ad.place(relx=0.36, rely=0.705, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.update_gf_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.78, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# convert tuple to list
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        self.c = tk.StringVar()
          
        # initial menu text
        self.c.set( self.s_names[0] )# set the value that is shown at the start instead of choose
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.update_gf_question , self.c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.765, relwidth=0.1, relheight=0.05, anchor='ne')

        addbtn = tk.Button(self.update_gf_question,text='UPDATE',font=MIDDLEFONT, command=self.ugfq)
        addbtn.pack()
        addbtn.place(relx=0.41, rely=0.765, relwidth=0.1, relheight=0.05, anchor='ne')

    def eu3(self, event): #entry Updater
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values'] #Extract current row data in a form of tuple to record variable
        self.qname.delete(0,'end')# delete text in textbox
        self.qname.insert(0,record[1])#add text in textbox
        self.c.set(record[2])# set the current displayed subject 
        self.o1.delete(0,'end')# same as above
        self.o1.insert(0,record[3])
        self.oa.delete(0,'end')
        self.oa.insert(0,record[4])
        self.ad.delete(0,'end')
        self.ad.insert(0,record[5])

    def utfq(self):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']#Extract current row data in a form of tuple to record variable
        query="UPDATE true_false_question SET question_text='"+self.qname.get()+"', subject_name='"+self.c.get()+"', option1='"+self.o1.get()+"', option_answer='"+self.oa.get()+"', answer_description='"+self.ad.get()+"' WHERE question_text=?"
        try:
            print(record[1])
            cursor.execute(query, (record[1],))
            connection.commit()
            self.tree.delete(*self.tree.get_children())# delete every row in the table on the screeen
            cursor.execute('SELECT * from true_false_question')
            r=cursor.fetchall()
            n=0
            l=[]
            for rows in r:# explained above in add
                    n=n+1
                    l=[]
                    l.append(str(n))
                    add=tuple(l)+rows[:-1]
                    self.tree.insert('', tk.END, values=add)
            messagebox.showinfo('Question Updated!','Your True/False Question was Updated')
        except Exception as e:
            messagebox.showerror('Exception Occurred!',e)

        # delete data in the textbox after delete data from database
        self.qname.delete(0,'end')
        self.o1.delete(0,'end')
        self.oa.delete(0,'end')
        self.ad.delete(0,'end')

    def update_tfq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.update_tf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_tf_question ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.update_tf_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_tf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_tf_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.update_tf_question,text='True/False Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_answer','answer_description')

        self.tree = ttk.Treeview(self.update_tf_question, columns=columns, show='headings')
        self.tree.column("# 1",anchor=tk.CENTER,width=5)
        self.tree.column("# 2",anchor=tk.W,width=120)
        self.tree.column("# 3",anchor=tk.W,width=10)
        self.tree.column("# 4",anchor=tk.W,width=10)
        self.tree.column("# 5",anchor=tk.W,width=10)
        self.tree.column("# 6",anchor=tk.W,width=120)

        # define headings
        self.tree.heading('roll_no', text='No.')
        self.tree.heading('question_text', text='Question text')
        self.tree.heading('subject_name', text='Subject name')
        self.tree.heading('option_1', text='Option 1')
        self.tree.heading('option_answer', text='Option Answer')
        self.tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from true_false_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:# explain in add
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            self.tree.insert('', tk.END, values=add)

        self.tree.pack()
        self.tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.35)
        scrollbar = ttk.Scrollbar(self.update_tf_question, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.92, rely=0.11, relwidth=0.015, relheight=0.35, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.update_tf_question, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.46, relwidth=0.81, relheight=0.03)

        self.tree.bind('<<TreeviewSelect>>', self.eu3)# call eu3 function every timr you select a row in the table

        l1 = tk.Label(self.update_tf_question,text='Enter the Question:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.40, rely=0.51, relwidth=0.5, relheight=0.015, anchor='ne')
        self.qname = tk.Entry(self.update_tf_question)
        self.qname.pack()
        self.qname.place(relx=0.36, rely=0.53, relwidth=0.5, relheight=0.05, anchor='n')

        l2 = tk.Label(self.update_tf_question,text='Option 01:',bg='lightblue')
        l2.pack()
        l2.place(relx=0.233, rely=0.585, relwidth=0.2, relheight=0.02, anchor='ne')
        self.o1 = tk.Entry(self.update_tf_question)
        self.o1.pack()
        self.o1.place(relx=0.222, rely=0.61, relwidth=0.225, relheight=0.05, anchor='n')

        l4 = tk.Label(self.update_tf_question,text='Option Answer:',bg='lightblue')
        l4.pack()
        l4.place(relx=0.243, rely=0.665, relwidth=0.2, relheight=0.02, anchor='ne')
        self.oa = tk.Entry(self.update_tf_question)
        self.oa.pack()
        self.oa.place(relx=0.222, rely=0.69, relwidth=0.225, relheight=0.05, anchor='n')

        l1 = tk.Label(self.update_tf_question,text='Enter Description:',bg='lightblue')
        l1.pack()
        l1.place(relx=0.3975, rely=0.745, relwidth=0.5, relheight=0.02, anchor='ne')
        self.ad = tk.Entry(self.update_tf_question)
        self.ad.pack()
        self.ad.place(relx=0.36, rely=0.77, relwidth=0.5, relheight=0.05, anchor='n')

        l6 = tk.Label(self.update_tf_question,text='Select Subject:',bg='lightblue')
        l6.pack()
        l6.place(relx=0.243, rely=0.85, relwidth=0.2, relheight=0.02, anchor='ne')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# convert tuple to list
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        self.c = tk.StringVar()
          
        # initial menu text
        self.c.set( self.s_names[0] )
          
        # Create Dropdown menu
        drop = tk.OptionMenu( self.update_tf_question , self.c, *self.s_names )
        drop.pack()
        drop.place(relx=0.28, rely=0.835, relwidth=0.1, relheight=0.05, anchor='ne')

        updatebtn = tk.Button(self.update_tf_question,text='UPDATE',font=MIDDLEFONT, command=self.utfq)
        updatebtn.pack()
        updatebtn.place(relx=0.41, rely=0.84, relwidth=0.1, relheight=0.05, anchor='ne')

    #fiverr
    def upm(self,tbox,c):
        # upate command in sql
        query="UPDATE module SET module_name='"+tbox.get()+"' WHERE module_name=?"
        print(c.get())
        cursor.execute(query, (c.get(),))# c.get() = get the current dropdown selection 
        connection.commit()

    def update_module(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.update_module_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_module_page ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.update_module_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_module_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_module_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete = tk.Label(self.update_module_page,text='UPDATE MODULE',bg='lightblue',font=LARGEFONT)
        delete.pack()
        delete.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.update_module_page,text='Select Module:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.45, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')

        cursor.execute('SELECT module_name from module')
        r=cursor.fetchall()
        module_names = []
        for row in r:
            module_names.append(row[0])# convert tuple to list
        print(r)
        print(module_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( module_names[0] )
          
        # Create Dropdown menu
        self.dropup1 = tk.OptionMenu( self.update_module_page , c, *module_names )
        self.dropup1.pack()
        self.dropup1.place(relx=0.60, rely=0.44, relwidth=0.1, relheight=0.05, anchor='ne')

        sm = tk.Label(self.update_module_page,text='Enter Updated name:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.50, rely=0.55, relwidth=0.6, relheight=0.05, anchor='n')

        mname = tk.Entry(self.update_module_page)
        mname.pack()
        mname.place(relx=0.50, rely=0.66, relwidth=0.2, relheight=0.05, anchor='n')
        
        add_btn = tk.Button(self.update_module_page,text='Update',command=lambda:self.upm(mname,c))
        add_btn.pack()
        add_btn.place(relx=0.55, rely=0.77, relwidth=0.1, relheight=0.05, anchor='ne')

    def ups(self,tbox,c,dropdown):
        query="UPDATE subject SET subject_name='"+tbox.get()+"' WHERE subject_name=?"
        print(c.get())
        cursor.execute(query, (c.get(),))
        connection.commit()
        menu = dropdown['menu']
        # Clear the menu.
        menu.delete(0, 'end')
        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        s_names = []
        for row in r:
            s_names.append(row[0])
        self.s_names=s_names
        for name in s_names:
            # Add menu items.
            menu.add_command(label=name, command=lambda name=name: c.set(name))
        i=self.s_names.index(tbox.get())
        c.set(s_names[i])
        

    def update_subject(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.update_subject_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.update_subject_page ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.update_subject_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.update_subject_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.update_subject_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete = tk.Label(self.update_subject_page,text='UPDATE SUBJECT',bg='lightblue',font=LARGEFONT)
        delete.pack()
        delete.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.update_subject_page,text='Select Subject:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.45, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        self.s_names = []
        for row in r:
            self.s_names.append(row[0])# conert tuple r to a list to work as dropdown option to dropdown menu
        print(r)
        print(self.s_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( self.s_names[0] )
          
        # Create Dropdown menu
        self.dropup2 = tk.OptionMenu( self.update_subject_page , c, *self.s_names )
        self.dropup2.pack()
        self.dropup2.place(relx=0.60, rely=0.44, relwidth=0.1, relheight=0.05, anchor='ne')

        sm = tk.Label(self.update_subject_page,text='Enter Updated name:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.50, rely=0.55, relwidth=0.6, relheight=0.05, anchor='n')

        mname = tk.Entry(self.update_subject_page)
        mname.pack()
        mname.place(relx=0.50, rely=0.66, relwidth=0.2, relheight=0.05, anchor='n')
        
        add_btn = tk.Button(self.update_subject_page,text='Update',command=lambda:self.ups(mname,c,self.dropup2))
        add_btn.pack()
        add_btn.place(relx=0.55, rely=0.77, relwidth=0.1, relheight=0.05, anchor='ne')

    # ========================================================================#      
     
    # ZAHID ===============FUNCTION TO SHOW OPTION's FOR DELETE FRAME=======================#
    def delete_frame(self):
        self.status='delete'
        self.clear_frame(self.delete_page)
        self.admin_page.pack_forget()
        self.delete_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_admin_frame,self.delete_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete_module_btn = tk.Button(self.delete_page,text='DELETE MODULE',font=LARGEFONT, command=self.delete_module)
        delete_module_btn.pack()
        delete_module_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        delete_subject_btn = tk.Button(self.delete_page,text='DELETE SUBJECT',font=LARGEFONT, command=self.delete_subject)
        delete_subject_btn.pack()
        delete_subject_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        delete_question_btn = tk.Button(self.delete_page,text='DELETE QUESTION',font=LARGEFONT, command=self.question_frame_delete)
        delete_question_btn.pack()
        delete_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    # ========================================================================#     

    # ZAHID ===============FUNCTION TO SHOW OPTION'S FOR ANY QUESTION FRAME=======================#
    def question_frame_add(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.question_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_add_frame,self.question_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.question_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.question_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        multiple_questions_btn = tk.Button(self.question_page,text='MULTIPLE QUESTION',font=LARGEFONT, command=self.add_mcq)
        multiple_questions_btn.pack()
        multiple_questions_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        gap_filling_question_btn = tk.Button(self.question_page,text='GAP FILLING QUESTION',font=LARGEFONT, command=self.add_gfq)
        gap_filling_question_btn.pack()
        gap_filling_question_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        true_false_question_btn = tk.Button(self.question_page,text='TRUE/FALSE QUESTION',font=LARGEFONT, command=self.add_tfq)
        true_false_question_btn.pack()
        true_false_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    def question_frame_update(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.question_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_update_frame,self.question_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.question_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.question_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        multiple_questions_btn = tk.Button(self.question_page,text='MULTIPLE QUESTION',font=LARGEFONT, command=self.update_mcq)
        multiple_questions_btn.pack()
        multiple_questions_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        gap_filling_question_btn = tk.Button(self.question_page,text='GAP FILLING QUESTION',font=LARGEFONT, command=self.update_gfq)
        gap_filling_question_btn.pack()
        gap_filling_question_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        true_false_question_btn = tk.Button(self.question_page,text='TRUE/FALSE QUESTION',font=LARGEFONT, command=self.update_tfq)
        true_false_question_btn.pack()
        true_false_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    def question_frame_delete(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.question_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.question_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.question_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.question_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        multiple_questions_btn = tk.Button(self.question_page,text='MULTIPLE QUESTION',font=LARGEFONT, command=self.del_mcq)
        multiple_questions_btn.pack()
        multiple_questions_btn.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')
        
        gap_filling_question_btn = tk.Button(self.question_page,text='GAP FILLING QUESTION',font=LARGEFONT, command=self.del_gfquestions)
        gap_filling_question_btn.pack()
        gap_filling_question_btn.place(relx=0.75, rely=0.44, relwidth=0.5, relheight=0.1, anchor='ne')
        
        true_false_question_btn = tk.Button(self.question_page,text='TRUE/FALSE QUESTION',font=LARGEFONT, command=self.del_tfq)
        true_false_question_btn.pack()
        true_false_question_btn.place(relx=0.75, rely=0.55, relwidth=0.5, relheight=0.1, anchor='ne')

    #fiverr - questions

    def delq(self, tree,table):
        for selected_item in reversed(tree.selection()):
            item = tree.item(selected_item)
            record = item['values']
            print(record)
            query='DELETE from '+table+' WHERE question_text=?'
            cursor.execute(query, (record[1],))
            connection.commit()

        tree.delete(*tree.get_children())
        cursor.execute('SELECT * from '+table)
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:
                n=n+1
                l=[]
                l.append(str(n))
                add=tuple(l)+rows[:-1]
                tree.insert('', tk.END, values=add)

    def del_mcq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.delete_mc_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_mc_question ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.delete_mc_question))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_mc_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_mc_question))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.delete_mc_question,text='Multiple Choice Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_2','option_3','option_answer','answer_description')

        tree = ttk.Treeview(self.delete_mc_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=5)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=10)
        tree.column("# 6",anchor=tk.W,width=10)
        tree.column("# 7",anchor=tk.W,width=10)
        tree.column("# 8",anchor=tk.W,width=120)

        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_1', text='Option 1')
        tree.heading('option_2', text='Option 2')
        tree.heading('option_3', text='Option 3')
        tree.heading('option_answer', text='Option Answer')
        tree.heading('answer_description', text='Answer description')
        cursor.execute('SELECT * from mc_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            tree.insert('', tk.END, values=add)

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.5)
        scrollbar = ttk.Scrollbar(self.delete_mc_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.91, rely=0.11, relwidth=0.015, relheight=0.5, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.delete_mc_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.61, relwidth=0.8, relheight=0.03)
        
        delete = tk.Button(self.delete_mc_question,text='DELETE',font=MIDDLEFONT, command=lambda:self.delq(tree,'mc_question'))
        delete.pack()
        delete.place(relx=0.55, rely=0.7, relwidth=0.1, relheight=0.05, anchor='ne')
        
    def del_gfquestions(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.delete_gf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_gf_question ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.delete_gf_question ))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_gf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_gf_question ))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        gfq = tk.Label(self.delete_gf_question,text='Gap Filling Questions',bg='lightblue',font=LARGEFONT)
        gfq.pack()
        gfq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_answer','answer_description','seen_times')

        tree = ttk.Treeview(self.delete_gf_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=10)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=120)

        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_answer', text='Option answer')
        tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from gap_filling_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            tree.insert('', tk.END, values=add)

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.5)
        scrollbar = ttk.Scrollbar(self.delete_gf_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.91, rely=0.11, relwidth=0.015, relheight=0.5, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.delete_gf_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.61, relwidth=0.8, relheight=0.03)
        
        delete = tk.Button(self.delete_gf_question,text='DELETE',font=MIDDLEFONT, command=lambda:self.delq(tree,'gap_filling_question'))
        delete.pack()
        delete.place(relx=0.55, rely=0.7, relwidth=0.1, relheight=0.05, anchor='ne')

    def del_tfq(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.question_page.pack_forget()
        self.delete_tf_question.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_tf_question ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.delete_tf_question ))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_tf_question, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_tf_question ))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        mcq = tk.Label(self.delete_tf_question,text='True/False Questions',bg='lightblue',font=LARGEFONT)
        mcq.pack()
        mcq.place(relx=0.75, rely=0.01, relwidth=0.5, relheight=0.1, anchor='ne')

        # define columns
        columns = ('roll_no','question_text','subject_name','option_1','option_answer','answer_description')

        tree = ttk.Treeview(self.delete_tf_question, columns=columns, show='headings')
        tree.column("# 1",anchor=tk.CENTER,width=5)
        tree.column("# 2",anchor=tk.W,width=120)
        tree.column("# 3",anchor=tk.W,width=10)
        tree.column("# 4",anchor=tk.W,width=10)
        tree.column("# 5",anchor=tk.W,width=10)
        tree.column("# 6",anchor=tk.W,width=120)
        # define headings
        tree.heading('roll_no', text='No.')
        tree.heading('question_text', text='Question text')
        tree.heading('subject_name', text='Subject name')
        tree.heading('option_1', text='Option 1')
        tree.heading('option_answer', text='Option Answer')
        tree.heading('answer_description', text='Answer description')

        cursor.execute('SELECT * from true_false_question')
        r=cursor.fetchall()
        n=0
        l=[]
        for rows in r:
            n=n+1
            l=[]
            l.append(str(n))
            add=tuple(l)+rows[:-1]
            tree.insert('', tk.END, values=add)

        tree.pack()
        tree.place(relx=0.11, rely=0.11, relwidth=0.8, relheight=0.5)
        scrollbar = ttk.Scrollbar(self.delete_tf_question, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()
        scrollbar.place(relx=0.91, rely=0.11, relwidth=0.015, relheight=0.5, anchor='ne')
        scrollbar2 = ttk.Scrollbar(self.delete_tf_question, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack()
        scrollbar2.place(relx=0.11, rely=0.61, relwidth=0.8, relheight=0.03)
        
        delete = tk.Button(self.delete_tf_question,text='DELETE',font=MIDDLEFONT, command=lambda:self.delq(tree,'true_false_question'))
        delete.pack()
        delete.place(relx=0.55, rely=0.7, relwidth=0.1, relheight=0.05, anchor='ne')

    #fiverr

    def delm(self, table, clicked, drop):
        ddown_selection=clicked.get()
        query="DELETE from "+table+" where module_name=?"
        cursor.execute(query, (ddown_selection,))
        connection.commit()
        i=drop['menu'].index(ddown_selection)
        drop['menu'].delete(i)
        clicked.set(drop['menu'].entrycget(0, 'label'))
        
    def delete_module(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.delete_module_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_module_page,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.delete_module_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_module_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_module_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete = tk.Label(self.delete_module_page,text='DELETE MODULE',bg='lightblue',font=LARGEFONT)
        delete.pack()
        delete.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.delete_module_page,text='Select Module:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.45, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')

        cursor.execute('SELECT module_name from module')
        r=cursor.fetchall()
        module_names = []
        for row in r:
            module_names.append(row[0])
        print(r)
        print(module_names)
        
  
        # datatype of menu text
        self.clicked = tk.StringVar()
          
        # initial menu text
        self.clicked.set( module_names[0] )
          
        # Create Dropdown menu
        self.drop = tk.OptionMenu( self.delete_module_page , self.clicked , *module_names )
        self.drop.pack()
        self.drop.place(relx=0.60, rely=0.44, relwidth=0.1, relheight=0.05, anchor='ne')

        
        delete_btn = tk.Button(self.delete_module_page,text='Delete',command=lambda:self.delm('module', self.clicked, self.drop))
        delete_btn.pack()
        delete_btn.place(relx=0.55, rely=0.55, relwidth=0.1, relheight=0.05, anchor='ne')

    def delete_subject(self):
        self.clear_frame(self.question_page)
        self.admin_page.pack_forget()
        self.add_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.delete_subject_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.delete_subject_page ,text='BACK',font=MIDDLEFONT,command=partial(self.go_to_delete_frame,self.delete_subject_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.delete_subject_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.delete_subject_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        delete = tk.Label(self.delete_subject_page,text='DELETE SUBJECT',bg='lightblue',font=LARGEFONT)
        delete.pack()
        delete.place(relx=0.75, rely=0.33, relwidth=0.5, relheight=0.1, anchor='ne')

        sm = tk.Label(self.delete_subject_page,text='Select Subject:',bg='lightblue')
        sm.pack()
        sm.place(relx=0.45, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')

        cursor.execute('SELECT subject_name from subject')
        r=cursor.fetchall()
        module_names = []
        for row in r:
            module_names.append(row[0])
        print(r)
        print(module_names)
        
  
        # datatype of menu text
        c = tk.StringVar()
          
        # initial menu text
        c.set( module_names[0] )
          
        # Create Dropdown menu
        self.drop2 = tk.OptionMenu( self.delete_subject_page , c, *module_names )
        self.drop2.pack()
        self.drop2.place(relx=0.60, rely=0.44, relwidth=0.1, relheight=0.05, anchor='ne')

        
        delete_btn = tk.Button(self.delete_subject_page,text='Delete',command=lambda:self.delm('subject', c, self.drop2))
        delete_btn.pack()
        delete_btn.place(relx=0.55, rely=0.55, relwidth=0.1, relheight=0.05, anchor='ne')

    
    # ========================================================================# 

    # ===============FUNCTION TO DISPLAY AND SHOW MODULE FRAME=======================#
    def module_frame(self,name):
        self.clear_frame(self.module_page)
        self.quiz_page.pack_forget()
        self.module_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.module_page, text='BACK', font=MIDDLEFONT,command=partial(self.go_to_quiz_frame, self.module_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.module_page, text='Main Menu', font=MIDDLEFONT, command=partial(self.go_to_main_menu,self.module_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')
        report_btn = tk.Button(self.module_page, text=f'{name.title()} Report', font=MIDDLEFONT,command=partial(self.report_frame,name))
        report_btn.pack()
        report_btn.place(relx=0, rely=0, relwidth=0.4,relheight=0.1,anchor='nw')
        var = 0
        self.module_object_list[name].set_subject_list()
        for subjects in self.module_object_list[name].get_subject_list():
            subjects_btn = tk.Button(self.module_page, text=subjects.title(), font=LARGEFONT,command = partial(self.question_type_frame,subjects))
            subjects_btn.pack()
            subjects_btn.place(relx=0.75, rely=0.2 + var, relwidth=0.5, relheight=0.1, anchor='ne')
            var += 0.11
    # =====================================================================#

    #================FUNCTION TO SHOW REPORT FRAME================================#

    def report_frame(self,name):
        self.clear_frame(self.report_page)
        self.module_page.pack_forget()
        self.report_page.pack(fill='both', expand=1)
        back_btn = tk.Button(self.report_page, text='BACK', font=MIDDLEFONT,
                             command=partial(self.go_to_module_frame, self.report_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')

        tv = ttk.Treeview(self.report_page, columns=(1, 2, 3, 4, 5, 6), show='headings', height='15',selectmode='none' )
        tv.pack()

        tv.place()
        headings_list = ['Subject','Most Seen Question','Most Second Seen Question','Highest Score','Lowest Score','Average Score']
        heading_pos = 1
        for headings in headings_list:
            tv.heading(heading_pos, text=headings)
            heading_pos +=1


        pdf_btn = tk.Button(self.report_page, text='PRINT TO PDF', font=MIDDLEFONT, command=partial(self.print_to_pdf,name))
        pdf_btn.pack()
        pdf_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        self.pdf = FPDF(format='A4', unit='in',)
        self.pdf.add_page()
        efective_page_width = self.pdf.w - 2*self.pdf.l_margin
        column_width = efective_page_width/4

        self.pdf.set_font('Times', 'B', 14.0)
        self.pdf.cell(efective_page_width,0.0,f'{name.upper()}',align='C')
        self.pdf.set_font('Times', 'B', 10.0)
        self.pdf.ln(0.5)
        for headings_for_pdf in ['Subject','Highest Score','Lowest Score','Average Score']:
            self.pdf.cell(column_width,2*self.pdf.font_size,headings_for_pdf,border=1)
        self.pdf.ln(2*self.pdf.font_size)
        self.pdf.set_font('Times', '', 10.0)

        self.module_object_list[name].set_subject_list()
        for subjects in self.module_object_list[name].get_subject_list():
            most_seen_mcq = cursor.execute(
                '''SELECT question_text,seen_times FROM mc_question WHERE subject_name = ? ORDER BY seen_times DESC ''',
                [subjects]).fetchmany(2)
            most_seen_true_false = cursor.execute(
                '''SELECT question_text,seen_times FROM true_false_question WHERE subject_name = ? ORDER BY seen_times DESC  ''',
                [subjects]).fetchmany(2)
            most_seen_gap_filling = cursor.execute(
                '''SELECT question_text,seen_times FROM gap_filling_question WHERE subject_name = ? ORDER BY seen_times DESC ''',
                [subjects]).fetchmany(2)

            most_seen_list = [most_seen_mcq[0],most_seen_mcq[1], most_seen_true_false[0],most_seen_true_false[1], most_seen_gap_filling[0],most_seen_gap_filling[1]]
            rndm.shuffle(most_seen_list)
            question1, max_value = max(most_seen_list, key=lambda item: item[1])

            most_seen_list.remove((question1, max_value))
            question2, second_max_value = max(most_seen_list, key=lambda item: item[1])

            if max_value == 0:
                most_seen_question = '--'
            else:
                most_seen_question = question1

            if second_max_value == 0:
                most_second_seen_question = '--'
            else:
                most_second_seen_question = question2






            report_list = cursor.execute(''' SELECT attempts,total_score,lowest_score_out_of_five,highest_score_out_of_five FROM subject WHERE subject_name = ?''',[subjects]).fetchall()

            if report_list[0][0] == 0:
                avg = f'{0}/5'
            else:
                avg = f'{report_list[0][1] / report_list[0][0]}/5'

            if report_list[0][2] == 6:
                lowest = 'You have no score'
            else:
                lowest = f'{report_list[0][2]}/5'

            if report_list[0][3] == -1:
                highest = 'You have no score'
            else:
                highest = f'{report_list[0][3]}/5'


            tv.insert('', 'end', values=(subjects.title(),most_seen_question,most_second_seen_question,highest,lowest,avg))
            pdf_report_list = [subjects.title(),highest,lowest,avg]

            for pdf_data in pdf_report_list:
                self.pdf.cell(column_width,2*self.pdf.font_size,str(pdf_data),border=1)
            self.pdf.ln(2*self.pdf.font_size)
    #==============================================================================#


    # =====================PRINT TO PDF============================================#
    def print_to_pdf(self,name):
        self.pdf.output(f'{name}.pdf')


    # ==============================================================================#

    #====================FUNCTION TO DISPLAY AND SHOW QUESTION TPYE FRAME==================#
    def question_type_frame(self,name):
        self.clear_frame(self.question_type_page)
        self.module_page.pack_forget()
        self.question_type_page.pack(fill='both', expand=1)
        mcq_btn = tk.Button(self.question_type_page, text='Multiple Question', font=LARGEFONT,
                            command=partial(self.mc_questions_in_questions_frame, name))
        mcq_btn.pack()
        mcq_btn.place(relx=0.75, rely=0.26, relwidth=0.5, relheight=0.1, anchor='ne')


        gap_filling_btn = tk.Button(self.question_type_page, text='Gap Filling Question', font=LARGEFONT,
                                    command=partial(self.gap_filling_questions_in_questions_frame, name))
        gap_filling_btn.pack()
        gap_filling_btn.place(relx=0.75, rely=0.37, relwidth=0.5, relheight=0.1, anchor='ne')


        true_false_btn = tk.Button(self.question_type_page, text='True/False Question', font=LARGEFONT,
                                   command=partial(self.true_false_questions_in_questions_frame, name))
        true_false_btn.pack()
        true_false_btn.place(relx=0.75, rely=0.48, relwidth=0.5, relheight=0.1, anchor='ne')

        back_btn = tk.Button(self.question_type_page, text='BACK', font=MIDDLEFONT,command=partial(self.go_to_module_frame, self.question_type_page))
        back_btn.pack()
        back_btn.place(relx=0, rely=1,relwidth=0.2, relheight=0.1, anchor='sw')
        main_page_btn = tk.Button(self.question_type_page, text='Main Menu', font=MIDDLEFONT,
                                  command=partial(self.go_to_main_menu, self.question_type_page))
        main_page_btn.pack()
        main_page_btn.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

    # =====================================================================#

    # ====================FUNCTIONS TO DISPLAY QUIESTIONS AND SHOW QUESTIONS FRAME==================#

    def mc_questions_in_questions_frame(self,name):
        self.subject_object_list[name].set_multiple_choice_question_list()
        rndm.shuffle(self.subject_object_list[name].get_multiple_choice_question_list())
        self.clear_frame(self.question1_page)
        self.clear_frame(self.question2_page)
        self.clear_frame(self.question3_page)
        self.clear_frame(self.question4_page)
        self.clear_frame(self.question5_page)
        self.question_type_page.pack_forget()
        self.question1_page.pack(fill='both', expand=1)

        question1_option = tk.StringVar()
        question2_option = tk.StringVar()
        question3_option = tk.StringVar()
        question4_option = tk.StringVar()
        question5_option = tk.StringVar()
    # ==============================================================================================#

    #===================QUESTION PAGE 1============================================================================#
        self.label1_mcq = tk.Label(self.question1_page,
                          text=f'Question 1: {self.subject_object_list[name].get_multiple_choice_question_list()[0]}',
                          font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label1_mcq.pack(ipady=25,fill='x')

        next_btn_1 = tk.Button(self.question1_page, text='NEXT', font=MIDDLEFONT, command=self.question1_to_2)
        next_btn_1.pack()
        next_btn_1.place(relx=1, rely=1,relwidth=0.2, relheight=0.1, anchor='se')

        var = 0
        rndm.shuffle(self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[0]].get_options_list())
        self.radio_btn_q1_mcq = []
        for options in self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[0]].get_options_list():
            radio_btn_q1 = tk.Radiobutton(self.question1_page, text=options, variable=question1_option,
                                               value=options, font=MIDDLEFONT, bg='lightblue',
                                               activebackground='lightblue',wraplength=750)
            self.radio_btn_q1_mcq.append(radio_btn_q1)
            radio_btn_q1.pack()
            radio_btn_q1.place(relx=1, rely=0.2 + var, relwidth=1, relheight=0.1, anchor='ne')
            var += 0.11

    # ==============================================================================================#

    # ===================QUESTION PAGE 2============================================================================#
        self.label2_mcq = tk.Label(self.question2_page,
                          text=f'Question 2: {self.subject_object_list[name].get_multiple_choice_question_list()[1]}',
                          font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label2_mcq.pack(ipady=25, fill='x')

        next_btn_2 = tk.Button(self.question2_page, text='NEXT', font=MIDDLEFONT, command=self.question2_to_3)
        next_btn_2.pack()
        next_btn_2.place(relx=1, rely=1,relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_2 = tk.Button(self.question2_page, text='BACK', font=MIDDLEFONT, command=self.question2_to_1)
        back_btn_2.pack()
        back_btn_2.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var2 = 0
        rndm.shuffle(self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[1]].get_options_list())
        self.radio_btn_q2_mcq = []
        for options2 in self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[1]].get_options_list():
            radio_btn_q2 = tk.Radiobutton(self.question2_page, text=options2, variable=question2_option,
                                               value=options2, font=MIDDLEFONT, bg='lightblue',
                                               activebackground='lightblue',wraplength=750)
            self.radio_btn_q2_mcq.append(radio_btn_q2)
            radio_btn_q2.pack()
            radio_btn_q2.place(relx=1, rely=0.2 + var2, relwidth=1, relheight=0.1, anchor='ne')
            var2 += 0.11
    # ==============================================================================================#

    # ===================QUESTION PAGE 3============================================================================#
        self.label3_mcq = tk.Label(self.question3_page,
                          text=f'Question 3: {self.subject_object_list[name].get_multiple_choice_question_list()[2]}',
                          font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label3_mcq.pack(ipady=25, fill='x')

        next_btn_3 = tk.Button(self.question3_page, text='NEXT', font=MIDDLEFONT, command=self.question3_to_4)
        next_btn_3.pack()
        next_btn_3.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_3 = tk.Button(self.question3_page, text='BACK', font=MIDDLEFONT, command=self.question3_to_2)
        back_btn_3.pack()
        back_btn_3.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var3 = 0
        rndm.shuffle(self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[2]].get_options_list())
        self.radio_btn_q3_mcq = []
        for options3 in self.mc_question_object_list[
            self.subject_object_list[name].get_multiple_choice_question_list()[2]].get_options_list():
            radio_btn_q3 = tk.Radiobutton(self.question3_page, text=options3, variable=question3_option,
                                               value=options3, font=MIDDLEFONT, bg='lightblue',
                                               activebackground='lightblue',wraplength=750)
            self.radio_btn_q3_mcq.append(radio_btn_q3)
            radio_btn_q3.pack()
            radio_btn_q3.place(relx=1, rely=0.2 + var3, relwidth=1, relheight=0.1, anchor='ne')
            var3 += 0.11
    # ==============================================================================================#

    # ===================QUESTION PAGE 4============================================================================#
        self.label4_mcq = tk.Label(self.question4_page,
                          text=f'Question 4: {self.subject_object_list[name].get_multiple_choice_question_list()[3]}',
                          font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label4_mcq.pack(ipady=25, fill='x')

        next_btn_4 = tk.Button(self.question4_page, text='NEXT', font=MIDDLEFONT, command=self.question4_to_5)
        next_btn_4.pack()
        next_btn_4.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_4 = tk.Button(self.question4_page, text='BACK', font=MIDDLEFONT, command=self.question4_to_3)
        back_btn_4.pack()
        back_btn_4.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var4 = 0
        rndm.shuffle(self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[3]].get_options_list())
        self.radio_btn_q4_mcq = []
        for options4 in self.mc_question_object_list[
            self.subject_object_list[name].get_multiple_choice_question_list()[3]].get_options_list():
            radio_btn_q4 = tk.Radiobutton(self.question4_page, text=options4, variable=question4_option,
                                               value=options4, font=MIDDLEFONT, bg='lightblue',
                                               activebackground='lightblue',wraplength=750)
            self.radio_btn_q4_mcq.append(radio_btn_q4)
            radio_btn_q4.pack()
            radio_btn_q4.place(relx=1, rely=0.2 + var4, relwidth=1, relheight=0.1, anchor='ne')
            var4 += 0.11
    # ==============================================================================================#

    # ===================QUESTION PAGE 5============================================================================#
        self.label5_mcq = tk.Label(self.question5_page,
                          text=f'Question 5: {self.subject_object_list[name].get_multiple_choice_question_list()[4]}',
                          font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label5_mcq.pack(ipady=25, fill='x')

        back_btn_5 = tk.Button(self.question5_page, text='BACK', font=MIDDLEFONT, command=self.question5_to_4)
        back_btn_5.pack()
        back_btn_5.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')
        self.submit_btn_mcq = tk.Button(self.question5_page, text='SAVE & SUBMIT', font=LARGEFONT,wraplength=200,
                                    command=partial(self.submit_multiple_choice_question,name = name, option1 = question1_option,
                                                    option2 = question2_option,option3 = question3_option,option4 = question4_option
                                                    ,option5 = question5_option))
        self.submit_btn_mcq.pack()
        self.submit_btn_mcq.place(relx=1, rely=1, relwidth=0.3,relheight=0.15, anchor='se')
        var5 = 0
        rndm.shuffle(self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[4]].get_options_list())
        self.radio_btn_q5_mcq = []
        for options5 in self.mc_question_object_list[
            self.subject_object_list[name].get_multiple_choice_question_list()[4]].get_options_list():
            radio_btn_q5 = tk.Radiobutton(self.question5_page, text=options5, variable=question5_option,
                                               value=options5, font=MIDDLEFONT, bg='lightblue',
                                               activebackground='lightblue',wraplength=750)
            self.radio_btn_q5_mcq.append(radio_btn_q5)
            radio_btn_q5.pack()
            radio_btn_q5.place(relx=1, rely=0.2 + var5, relwidth=1, relheight=0.1, anchor='ne')
            var5 += 0.11
    # ==============================================================================================#



    def gap_filling_questions_in_questions_frame(self,name):
        self.subject_object_list[name].set_gap_filling_question_list()
        rndm.shuffle(self.subject_object_list[name].get_gap_filling_question_list())
        self.clear_frame(self.question1_page)
        self.clear_frame(self.question2_page)
        self.clear_frame(self.question3_page)
        self.clear_frame(self.question4_page)
        self.clear_frame(self.question5_page)
        self.question_type_page.pack_forget()
        self.question1_page.pack(fill='both', expand=1)
        #===============================================================#

        #==========================QUESTION PAGE 1====================================#
        self.label1_gap_filling = tk.Label(self.question1_page, text=f'Question 1: {self.subject_object_list[name].get_gap_filling_question_list()[0]}',
                                           font=MIDDLEFONT, bg='lightblue',wraplength=750)
        self.label1_gap_filling.pack(ipady=25,fill='x')

        next_btn_1 = tk.Button(self.question1_page, text='NEXT', font=MIDDLEFONT, command=self.question1_to_2)
        next_btn_1.pack()
        next_btn_1.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        self.label_entry = tk.Label(self.question1_page,text='Write your answer in the gap below',font = MIDDLEFONT, bg='lightblue')
        self.label_entry.pack()
        self.label_entry.place(relx=0.37, rely=0.35, anchor='sw')
        question1_entry = tk.Entry(self.question1_page, width= 50)
        question1_entry.pack()
        question1_entry.place(relx=0.37, rely=0.375, anchor='sw')
        # ===============================================================#

        # ==========================QUESTION PAGE 2====================================#

        self.label2_gap_filling = tk.Label(self.question2_page,
                                           text=f'Question 2: {self.subject_object_list[name].get_gap_filling_question_list()[1]}',
                                           font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label2_gap_filling.pack(ipady=25, fill='x')

        next_btn_2 = tk.Button(self.question2_page, text='NEXT', font=MIDDLEFONT, command=self.question2_to_3)
        next_btn_2.pack()
        next_btn_2.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_2 = tk.Button(self.question2_page, text='BACK', font=MIDDLEFONT, command=self.question2_to_1)
        back_btn_2.pack()
        back_btn_2.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        self.label2_entry = tk.Label(self.question2_page, text='Write your answer in the gap below', font=MIDDLEFONT,
                                     bg='lightblue')
        self.label2_entry.pack()
        self.label2_entry.place(relx=0.37, rely=0.35, anchor='sw')
        question2_entry = tk.Entry(self.question2_page, width=50)
        question2_entry.pack()
        question2_entry.place(relx=0.37, rely=0.375, anchor='sw')
        # ===============================================================#


        # ==========================QUESTION PAGE 3====================================#

        self.label3_gap_filling = tk.Label(self.question3_page,
                                           text=f'Question 3: {self.subject_object_list[name].get_gap_filling_question_list()[2]}',
                                           font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label3_gap_filling.pack(ipady=25, fill='x')

        next_btn_3 = tk.Button(self.question3_page, text='NEXT', font=MIDDLEFONT, command=self.question3_to_4)
        next_btn_3.pack()
        next_btn_3.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_3 = tk.Button(self.question3_page, text='BACK', font=MIDDLEFONT, command=self.question3_to_2)
        back_btn_3.pack()
        back_btn_3.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        self.label3_entry = tk.Label(self.question3_page, text='Write your answer in the gap below', font=MIDDLEFONT,
                                     bg='lightblue')
        self.label3_entry.pack()
        self.label3_entry.place(relx=0.37, rely=0.35, anchor='sw')
        question3_entry = tk.Entry(self.question3_page, width=50)
        question3_entry.pack()
        question3_entry.place(relx=0.37, rely=0.375, anchor='sw')
        # ===============================================================#



        # ==========================QUESTION PAGE 4====================================#
        self.label4_gap_filling = tk.Label(self.question4_page,
                                           text=f'Question 4: {self.subject_object_list[name].get_gap_filling_question_list()[3]}',
                                           font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label4_gap_filling.pack(ipady=25, fill='x')

        next_btn_4 = tk.Button(self.question4_page, text='NEXT', font=MIDDLEFONT, command=self.question4_to_5)
        next_btn_4.pack()
        next_btn_4.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_4 = tk.Button(self.question4_page, text='BACK', font=MIDDLEFONT, command=self.question4_to_3)
        back_btn_4.pack()
        back_btn_4.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        self.label4_entry = tk.Label(self.question4_page, text='Write your answer in the gap below', font=MIDDLEFONT,
                                     bg='lightblue')
        self.label4_entry.pack()
        self.label4_entry.place(relx=0.37, rely=0.35, anchor='sw')
        question4_entry = tk.Entry(self.question4_page, width=50)
        question4_entry.pack()
        question4_entry.place(relx=0.37, rely=0.375, anchor='sw')
        # ===============================================================#


        # ==========================QUESTION PAGE 5====================================#
        self.label5_gap_filling = tk.Label(self.question5_page,
                                           text=f'Question 5: {self.subject_object_list[name].get_gap_filling_question_list()[4]}',
                                           font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label5_gap_filling.pack(ipady=25, fill='x')


        back_btn_5 = tk.Button(self.question5_page, text='BACK', font=MIDDLEFONT, command=self.question5_to_4)
        back_btn_5.pack()
        back_btn_5.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')


        self.label5_entry = tk.Label(self.question5_page, text='Write your answer in the gap below', font=MIDDLEFONT,
                                     bg='lightblue')
        self.label5_entry.pack()
        self.label5_entry.place(relx=0.37, rely=0.35, anchor='sw')
        question5_entry = tk.Entry(self.question5_page, width=50)
        question5_entry.pack()
        question5_entry.place(relx=0.37, rely=0.375, anchor='sw')

        self.submit_btn_gap_filling = tk.Button(self.question5_page, text='SAVE & SUBMIT', font=LARGEFONT,
                                                wraplength=200, command=partial(self.submit_gap_filling_question, name,
                                                                                question1_entry, question2_entry,
                                                                                question3_entry,
                                                                                question4_entry, question5_entry))

        self.submit_btn_gap_filling.pack()
        self.submit_btn_gap_filling.place(relx=1, rely=1, relwidth=0.3, relheight=0.15, anchor='se')



        # ===============================================================#






    def true_false_questions_in_questions_frame(self,name):
        self.subject_object_list[name].set_true_false_question_list()
        rndm.shuffle(self.subject_object_list[name].get_true_false_question_list())
        self.clear_frame(self.question1_page)
        self.clear_frame(self.question2_page)
        self.clear_frame(self.question3_page)
        self.clear_frame(self.question4_page)
        self.clear_frame(self.question5_page)
        self.question_type_page.pack_forget()
        self.question1_page.pack(fill='both', expand=1)

        question1_option = tk.StringVar()
        question2_option = tk.StringVar()
        question3_option = tk.StringVar()
        question4_option = tk.StringVar()
        question5_option = tk.StringVar()
        # ==============================================================================================#

        # ===================QUESTION PAGE 1============================================================================#
        self.label1_true_false = tk.Label(self.question1_page,
                                   text=f'Question 1: {self.subject_object_list[name].get_true_false_question_list()[0]}',
                                   font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label1_true_false.pack(ipady=25, fill='x')

        next_btn_1 = tk.Button(self.question1_page, text='NEXT', font=MIDDLEFONT, command=self.question1_to_2)
        next_btn_1.pack()
        next_btn_1.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        var = 0
        rndm.shuffle(self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[0]].get_option_list())
        self.radio_btn_q1_true_false = []
        for options in self.true_false_question_object_list[
            self.subject_object_list[name].get_true_false_question_list()[0]].get_option_list():
            radio_btn_q1 = tk.Radiobutton(self.question1_page, text=options, variable=question1_option,
                                          value=options, font=MIDDLEFONT, bg='lightblue',
                                          activebackground='lightblue', wraplength=750)
            self.radio_btn_q1_true_false.append(radio_btn_q1)
            radio_btn_q1.pack()
            radio_btn_q1.place(relx=1, rely=0.2 + var, relwidth=1, relheight=0.1, anchor='ne')
            var += 0.11

        # ==============================================================================================#

        # ===================QUESTION PAGE 2============================================================================#
        self.label2_true_false = tk.Label(self.question2_page,
                                   text=f'Question 2: {self.subject_object_list[name].get_true_false_question_list()[1]}',
                                   font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label2_true_false.pack(ipady=25, fill='x')

        next_btn_2 = tk.Button(self.question2_page, text='NEXT', font=MIDDLEFONT, command=self.question2_to_3)
        next_btn_2.pack()
        next_btn_2.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_2 = tk.Button(self.question2_page, text='BACK', font=MIDDLEFONT, command=self.question2_to_1)
        back_btn_2.pack()
        back_btn_2.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var2 = 0
        rndm.shuffle(self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[1]].get_option_list())
        self.radio_btn_q2_true_false = []
        for options2 in self.true_false_question_object_list[
            self.subject_object_list[name].get_true_false_question_list()[1]].get_option_list():
            radio_btn_q2 = tk.Radiobutton(self.question2_page, text=options2, variable=question2_option,
                                          value=options2, font=MIDDLEFONT, bg='lightblue',
                                          activebackground='lightblue', wraplength=750)
            self.radio_btn_q2_true_false.append(radio_btn_q2)
            radio_btn_q2.pack()
            radio_btn_q2.place(relx=1, rely=0.2 + var2, relwidth=1, relheight=0.1, anchor='ne')
            var2 += 0.11
        # ==============================================================================================#

        # ===================QUESTION PAGE 3============================================================================#
        self.label3_true_false = tk.Label(self.question3_page,
                                   text=f'Question 3: {self.subject_object_list[name].get_true_false_question_list()[2]}',
                                   font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label3_true_false.pack(ipady=25, fill='x')

        next_btn_3 = tk.Button(self.question3_page, text='NEXT', font=MIDDLEFONT, command=self.question3_to_4)
        next_btn_3.pack()
        next_btn_3.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_3 = tk.Button(self.question3_page, text='BACK', font=MIDDLEFONT, command=self.question3_to_2)
        back_btn_3.pack()
        back_btn_3.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var3 = 0
        rndm.shuffle(self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[2]].get_option_list())
        self.radio_btn_q3_true_false = []
        for options3 in self.true_false_question_object_list[
            self.subject_object_list[name].get_true_false_question_list()[2]].get_option_list():
            radio_btn_q3 = tk.Radiobutton(self.question3_page, text=options3, variable=question3_option,
                                          value=options3, font=MIDDLEFONT, bg='lightblue',
                                          activebackground='lightblue', wraplength=750)
            self.radio_btn_q3_true_false.append(radio_btn_q3)
            radio_btn_q3.pack()
            radio_btn_q3.place(relx=1, rely=0.2 + var3, relwidth=1, relheight=0.1, anchor='ne')
            var3 += 0.11
        # ==============================================================================================#

        # ===================QUESTION PAGE 4============================================================================#
        self.label4_true_false = tk.Label(self.question4_page,
                                   text=f'Question 4: {self.subject_object_list[name].get_true_false_question_list()[3]}',
                                   font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label4_true_false.pack(ipady=25, fill='x')

        next_btn_4 = tk.Button(self.question4_page, text='NEXT', font=MIDDLEFONT, command=self.question4_to_5)
        next_btn_4.pack()
        next_btn_4.place(relx=1, rely=1, relwidth=0.2, relheight=0.1, anchor='se')

        back_btn_4 = tk.Button(self.question4_page, text='BACK', font=MIDDLEFONT, command=self.question4_to_3)
        back_btn_4.pack()
        back_btn_4.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')

        var4 = 0
        rndm.shuffle(self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[3]].get_option_list())
        self.radio_btn_q4_true_false = []
        for options4 in self.true_false_question_object_list[
            self.subject_object_list[name].get_true_false_question_list()[3]].get_option_list():
            radio_btn_q4 = tk.Radiobutton(self.question4_page, text=options4, variable=question4_option,
                                          value=options4, font=MIDDLEFONT, bg='lightblue',
                                          activebackground='lightblue', wraplength=750)
            self.radio_btn_q4_true_false.append(radio_btn_q4)
            radio_btn_q4.pack()
            radio_btn_q4.place(relx=1, rely=0.2 + var4, relwidth=1, relheight=0.1, anchor='ne')
            var4 += 0.11
        # ==============================================================================================#

        # ===================QUESTION PAGE 5============================================================================#
        self.label5_true_false = tk.Label(self.question5_page,
                                   text=f'Question 5: {self.subject_object_list[name].get_true_false_question_list()[4]}',
                                   font=MIDDLEFONT, bg='lightblue', wraplength=750)
        self.label5_true_false.pack(ipady=25, fill='x')

        back_btn_5 = tk.Button(self.question5_page, text='BACK', font=MIDDLEFONT, command=self.question5_to_4)
        back_btn_5.pack()
        back_btn_5.place(relx=0, rely=1, relwidth=0.2, relheight=0.1, anchor='sw')
        self.submit_btn_true_false = tk.Button(self.question5_page, text='SAVE & SUBMIT', font=LARGEFONT, wraplength=200,
                                        command=partial(self.submit_true_false_question, name=name,
                                                        option1=question1_option,
                                                        option2=question2_option, option3=question3_option,
                                                        option4=question4_option
                                                        , option5=question5_option))
        self.submit_btn_true_false.pack()
        self.submit_btn_true_false.place(relx=1, rely=1, relwidth=0.3, relheight=0.15, anchor='se')
        var5 = 0
        rndm.shuffle(self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[4]].get_option_list())
        self.radio_btn_q5_true_false = []
        for options5 in self.true_false_question_object_list[
            self.subject_object_list[name].get_true_false_question_list()[4]].get_option_list():
            radio_btn_q5 = tk.Radiobutton(self.question5_page, text=options5, variable=question5_option,
                                          value=options5, font=MIDDLEFONT, bg='lightblue',
                                          activebackground='lightblue', wraplength=750)
            self.radio_btn_q5_true_false.append(radio_btn_q5)
            radio_btn_q5.pack()
            radio_btn_q5.place(relx=1, rely=0.2 + var5, relwidth=1, relheight=0.1, anchor='ne')
            var5 += 0.11

    # ==============================================================================================#


    # ====FUNCTION TO SUBMIT FOR MULTIPLE CHOICE QUESTIONS=======#

    def submit_multiple_choice_question(self,name,option1,option2,option3,option4,option5):
        correct_count= 0
        if option1.get() == self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[0]].get_answer():
            correct_count +=1
        if option2.get() == self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[1]].get_answer():
            correct_count += 1
        if option3.get() == self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[2]].get_answer():
            correct_count +=1
        if option4.get() == self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[3]].get_answer():
            correct_count +=1
        if option5.get() == self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[4]].get_answer():
            correct_count +=1

        messagebox.showinfo('SCORE BOARD', f'YOUR SCORE IS: {correct_count}/5')

        self.submit_btn_mcq.config(state='disabled')
        self.label1_mcq.config(text=f'Question 1: {self.subject_object_list[name].get_multiple_choice_question_list()[0]} \n \n'
                                    f'Description: {self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[0]].get_description()}')
        for button1 in self.radio_btn_q1_mcq:
            button1.config(state='disabled')

        self.label2_mcq.config(text=f'Question 2: {self.subject_object_list[name].get_multiple_choice_question_list()[1]} \n \n'
                                    f'Description: {self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[1]].get_description()}')
        for button2 in self.radio_btn_q2_mcq:
            button2.config(state='disabled')

        self.label3_mcq.config(text=f'Question 3: {self.subject_object_list[name].get_multiple_choice_question_list()[2]} \n \n'
                                    f'Description: {self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[2]].get_description()}')
        for button3 in self.radio_btn_q3_mcq:
            button3.config(state='disabled')

        self.label4_mcq.config(text=f'Question 4: {self.subject_object_list[name].get_multiple_choice_question_list()[3]} \n \n'
                                    f'Description: {self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[3]].get_description()}')
        for button4 in self.radio_btn_q4_mcq:
            button4.config(state='disabled')

        self.label5_mcq.config(text=f'Question 5: {self.subject_object_list[name].get_multiple_choice_question_list()[4]} \n \n'
                                    f'Description: {self.mc_question_object_list[self.subject_object_list[name].get_multiple_choice_question_list()[4]].get_description()}')

        for button5 in self.radio_btn_q5_mcq:
            button5.config(state='disabled')
        done_btn = tk.Button(self.question5_page, text='Main Menu', font=MIDDLEFONT,
                                  command=partial(self.go_to_main_menu, self.question5_page))
        done_btn.pack()
        done_btn.place(relx=1, rely=0.85, relwidth=0.3,relheight=0.15, anchor='se')

        seen_time_list = cursor.execute("SELECT seen_times FROM mc_question WHERE question_text=?",
                                            [self.subject_object_list[name].get_multiple_choice_question_list()[0]]).fetchall()
        seen1 = seen_time_list[0][0]
        seen1 +=1
        cursor.execute("UPDATE mc_question SET seen_times=? WHERE question_text=?",[seen1,self.subject_object_list[name].get_multiple_choice_question_list()[0]])

        seen_time_list2 = cursor.execute("SELECT seen_times FROM mc_question WHERE question_text=?",
                                            [self.subject_object_list[name].get_multiple_choice_question_list()[1]]).fetchall()
        seen2 = seen_time_list2[0][0]
        seen2 +=1
        cursor.execute(
            "UPDATE mc_question SET seen_times=? WHERE question_text=?",[seen2,self.subject_object_list[name].get_multiple_choice_question_list()[1]])

        seen_time_list3 = cursor.execute("SELECT seen_times FROM mc_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_multiple_choice_question_list()[2]]).fetchall()
        seen3 = seen_time_list3[0][0]
        seen3 +=1
        cursor.execute(
            "UPDATE mc_question SET seen_times=? WHERE question_text=?",[seen3,self.subject_object_list[name].get_multiple_choice_question_list()[2]])

        seen_time_list4 = cursor.execute("SELECT seen_times FROM mc_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_multiple_choice_question_list()[3]]).fetchall()
        seen4= seen_time_list4[0][0]
        seen4 += 1
        cursor.execute(
            "UPDATE mc_question SET seen_times=? WHERE question_text=?",[seen4,self.subject_object_list[name].get_multiple_choice_question_list()[3]])

        seen_time_list5 = cursor.execute("SELECT seen_times FROM mc_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_multiple_choice_question_list()[4]]).fetchall()
        seen5 = seen_time_list5[0][0]
        seen5 += 1
        cursor.execute(
            "UPDATE mc_question SET seen_times=? WHERE question_text=?",[seen5,self.subject_object_list[name].get_multiple_choice_question_list()[4]])

        subject_report_list = cursor.execute("SELECT attempts,total_score,lowest_score_out_of_five,highest_score_out_of_five FROM subject WHERE subject_name=?",
                                         [name]).fetchall()
        subject_total_attempts = subject_report_list[0][0]
        subject_total_attempts +=1
        subject_total_score = subject_report_list[0][1]
        subject_total_score += correct_count
        subject_lowest_score = subject_report_list[0][2]
        if subject_lowest_score >= correct_count:
            subject_lowest_score = correct_count
        subject_highest_score = subject_report_list[0][3]
        if subject_highest_score <= correct_count:
            subject_highest_score = correct_count


        cursor.execute(
            "UPDATE subject SET attempts=?,total_score=?,lowest_score_out_of_five=?,highest_score_out_of_five=? WHERE subject_name=?",
            [subject_total_attempts,subject_total_score,subject_lowest_score,subject_highest_score, name])

        connection.commit()



    # =====================================================================#

    # ====FUNCTION TO SUBMIT FOR TRUE/FALSE QUESTIONS=======#

    def submit_true_false_question(self,name,option1,option2,option3,option4,option5):
        correct_count= 0
        if option1.get() == self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[0]].get_answer():
            correct_count +=1
        if option2.get() == self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[1]].get_answer():
            correct_count += 1
        if option3.get() == self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[2]].get_answer():
            correct_count +=1
        if option4.get() == self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[3]].get_answer():
            correct_count +=1
        if option5.get() == self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[4]].get_answer():
            correct_count +=1

        messagebox.showinfo('SCORE BOARD', f'YOUR SCORE IS: {correct_count}/5')

        self.submit_btn_true_false.config(state='disabled')
        self.label1_true_false.config(text=f'Question 1: {self.subject_object_list[name].get_true_false_question_list()[0]} \n \n'
                                    f'Description: {self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[0]].get_description()}')
        for button1 in self.radio_btn_q1_true_false:
            button1.config(state='disabled')

        self.label2_true_false.config(text=f'Question 2: {self.subject_object_list[name].get_true_false_question_list()[1]} \n \n'
                                    f'Description: {self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[1]].get_description()}')
        for button2 in self.radio_btn_q2_true_false:
            button2.config(state='disabled')

        self.label3_true_false.config(text=f'Question 3: {self.subject_object_list[name].get_true_false_question_list()[2]} \n \n'
                                    f'Description: {self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[2]].get_description()}')
        for button3 in self.radio_btn_q3_true_false:
            button3.config(state='disabled')

        self.label4_true_false.config(text=f'Question 4: {self.subject_object_list[name].get_true_false_question_list()[3]} \n \n'
                                    f'Description: {self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[3]].get_description()}')
        for button4 in self.radio_btn_q4_true_false:
            button4.config(state='disabled')

        self.label5_true_false.config(text=f'Question 5: {self.subject_object_list[name].get_true_false_question_list()[4]} \n \n'
                                    f'Description: {self.true_false_question_object_list[self.subject_object_list[name].get_true_false_question_list()[4]].get_description()}')

        for button5 in self.radio_btn_q5_true_false:
            button5.config(state='disabled')
        done_btn = tk.Button(self.question5_page, text='Main Menu', font=MIDDLEFONT,
                                  command=partial(self.go_to_main_menu, self.question5_page))
        done_btn.pack()
        done_btn.place(relx=1, rely=0.85, relwidth=0.3,relheight=0.15, anchor='se')

        seen_time_list = cursor.execute("SELECT seen_times FROM true_false_question WHERE question_text=?",
                                            [self.subject_object_list[name].get_true_false_question_list()[0]]).fetchall()
        seen1 = seen_time_list[0][0]
        seen1 +=1
        cursor.execute("UPDATE true_false_question SET seen_times=? WHERE question_text=?",[seen1,self.subject_object_list[name].get_true_false_question_list()[0]])

        seen_time_list2 = cursor.execute("SELECT seen_times FROM true_false_question WHERE question_text=?",
                                            [self.subject_object_list[name].get_true_false_question_list()[1]]).fetchall()
        seen2 = seen_time_list2[0][0]
        seen2 +=1
        cursor.execute(
            "UPDATE true_false_question SET seen_times=? WHERE question_text=?",[seen2,self.subject_object_list[name].get_true_false_question_list()[1]])

        seen_time_list3 = cursor.execute("SELECT seen_times FROM true_false_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_true_false_question_list()[2]]).fetchall()
        seen3 = seen_time_list3[0][0]
        seen3 +=1
        cursor.execute(
            "UPDATE true_false_question SET seen_times=? WHERE question_text=?",[seen3,self.subject_object_list[name].get_true_false_question_list()[2]])

        seen_time_list4 = cursor.execute("SELECT seen_times FROM true_false_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_true_false_question_list()[3]]).fetchall()
        seen4= seen_time_list4[0][0]
        seen4 += 1
        cursor.execute(
            "UPDATE true_false_question SET seen_times=? WHERE question_text=?",[seen4,self.subject_object_list[name].get_true_false_question_list()[3]])

        seen_time_list5 = cursor.execute("SELECT seen_times FROM true_false_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_true_false_question_list()[4]]).fetchall()
        seen5 = seen_time_list5[0][0]
        seen5 += 1
        cursor.execute(
            "UPDATE true_false_question SET seen_times=? WHERE question_text=?",[seen5,self.subject_object_list[name].get_true_false_question_list()[4]])

        subject_report_list = cursor.execute("SELECT attempts,total_score,lowest_score_out_of_five,highest_score_out_of_five FROM subject WHERE subject_name=?",
                                         [name]).fetchall()
        subject_total_attempts = subject_report_list[0][0]
        subject_total_attempts +=1
        subject_total_score = subject_report_list[0][1]
        subject_total_score += correct_count
        subject_lowest_score = subject_report_list[0][2]
        if subject_lowest_score >= correct_count:
            subject_lowest_score = correct_count
        subject_highest_score = subject_report_list[0][3]
        if subject_highest_score <= correct_count:
            subject_highest_score = correct_count


        cursor.execute(
            "UPDATE subject SET attempts=?,total_score=?,lowest_score_out_of_five=?,highest_score_out_of_five=? WHERE subject_name=?",
            [subject_total_attempts,subject_total_score,subject_lowest_score,subject_highest_score, name])

        connection.commit()
    # =====================================================================#


    #=============================FUNCTION TO SUBMIT GAP FILLING QUESTION=========================================#
    def submit_gap_filling_question(self,name,entry1,entry2,entry3,entry4,entry5):
        correct_count = 0
        if entry1.get() == self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[0]].get_answer():
            correct_count +=1
        if entry2.get() == self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[1]].get_answer():
            correct_count +=1
        if entry3.get() == self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[2]].get_answer():
            correct_count +=1
        if entry4.get() == self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[3]].get_answer():
            correct_count +=1
        if entry5.get() == self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[4]].get_answer():
            correct_count +=1

        messagebox.showinfo('SCORE BOARD', f'YOUR SCORE IS: {correct_count}/5')

        self.submit_btn_gap_filling.config(state='disabled')
        self.label1_gap_filling.config(
            text=f'Question 1: {self.subject_object_list[name].get_gap_filling_question_list()[0]} \n \n'
                 f'Description: {self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[0]].get_description()}')

        self.label2_gap_filling.config(
            text=f'Question 2: {self.subject_object_list[name].get_gap_filling_question_list()[1]} \n \n'
                 f'Description: {self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[1]].get_description()}')

        self.label3_gap_filling.config(
            text=f'Question 3: {self.subject_object_list[name].get_gap_filling_question_list()[2]} \n \n'
                 f'Description: {self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[2]].get_description()}')

        self.label4_gap_filling.config(
            text=f'Question 4: {self.subject_object_list[name].get_gap_filling_question_list()[3]} \n \n'
                 f'Description: {self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[3]].get_description()}')

        self.label5_gap_filling.config(
            text=f'Question 5: {self.subject_object_list[name].get_gap_filling_question_list()[4]} \n \n'
                 f'Description: {self.filling_gap_question_object_list[self.subject_object_list[name].get_gap_filling_question_list()[4]].get_description()}')



        for entries in [entry1,entry2,entry3,entry4,entry5]:
            entries.config(state='disabled')

        done_btn = tk.Button(self.question5_page, text='Main Menu', font=MIDDLEFONT,
                             command=partial(self.go_to_main_menu, self.question5_page))
        done_btn.pack()
        done_btn.place(relx=1, rely=0.85, relwidth=0.3, relheight=0.15, anchor='se')

        seen_time_list = cursor.execute("SELECT seen_times FROM gap_filling_question WHERE question_text=?",
                                        [self.subject_object_list[name].get_gap_filling_question_list()[0]]).fetchall()
        seen1 = seen_time_list[0][0]
        seen1 += 1
        cursor.execute("UPDATE gap_filling_question SET seen_times=? WHERE question_text=?",
                       [seen1, self.subject_object_list[name].get_gap_filling_question_list()[0]])

        seen_time_list2 = cursor.execute("SELECT seen_times FROM gap_filling_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_gap_filling_question_list()[1]]).fetchall()
        seen2 = seen_time_list2[0][0]
        seen2 += 1
        cursor.execute(
            "UPDATE gap_filling_question SET seen_times=? WHERE question_text=?",
            [seen2, self.subject_object_list[name].get_gap_filling_question_list()[1]])

        seen_time_list3 = cursor.execute("SELECT seen_times FROM gap_filling_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_gap_filling_question_list()[2]]).fetchall()
        seen3 = seen_time_list3[0][0]
        seen3 += 1
        cursor.execute(
            "UPDATE gap_filling_question SET seen_times=? WHERE question_text=?",
            [seen3, self.subject_object_list[name].get_gap_filling_question_list()[2]])

        seen_time_list4 = cursor.execute("SELECT seen_times FROM gap_filling_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_gap_filling_question_list()[3]]).fetchall()
        seen4 = seen_time_list4[0][0]
        seen4 += 1
        cursor.execute(
            "UPDATE gap_filling_question SET seen_times=? WHERE question_text=?",
            [seen4, self.subject_object_list[name].get_gap_filling_question_list()[3]])

        seen_time_list5 = cursor.execute("SELECT seen_times FROM gap_filling_question WHERE question_text=?",
                                         [self.subject_object_list[name].get_gap_filling_question_list()[4]]).fetchall()
        seen5 = seen_time_list5[0][0]
        seen5 += 1
        cursor.execute(
            "UPDATE gap_filling_question SET seen_times=? WHERE question_text=?",
            [seen5, self.subject_object_list[name].get_gap_filling_question_list()[4]])

        subject_report_list = cursor.execute(
            "SELECT attempts,total_score,lowest_score_out_of_five,highest_score_out_of_five FROM subject WHERE subject_name=?",
            [name]).fetchall()
        subject_total_attempts = subject_report_list[0][0]
        subject_total_attempts += 1
        subject_total_score = subject_report_list[0][1]
        subject_total_score += correct_count
        subject_lowest_score = subject_report_list[0][2]
        if subject_lowest_score >= correct_count:
            subject_lowest_score = correct_count
        subject_highest_score = subject_report_list[0][3]
        if subject_highest_score <= correct_count:
            subject_highest_score = correct_count

        cursor.execute(
            "UPDATE subject SET attempts=?,total_score=?,lowest_score_out_of_five=?,highest_score_out_of_five=? WHERE subject_name=?",
            [subject_total_attempts, subject_total_score, subject_lowest_score, subject_highest_score, name])

        connection.commit()







    #=============================================================================================================#








    #=========FUNCTIONS TO SWAP BETWEEN QUESTION FRAMES=========================#
    def question1_to_2(self):
        self.question1_page.pack_forget()
        self.question2_page.pack(fill='both', expand=1)

    def question2_to_3(self):
        self.question2_page.pack_forget()
        self.question3_page.pack(fill='both', expand=1)

    def question3_to_4(self):
        self.question3_page.pack_forget()
        self.question4_page.pack(fill='both', expand=1)

    def question4_to_5(self):
        self.question4_page.pack_forget()
        self.question5_page.pack(fill='both', expand=1)

    def question5_to_4(self):
        self.question5_page.pack_forget()
        self.question4_page.pack(fill='both', expand=1)

    def question4_to_3(self):
        self.question4_page.pack_forget()
        self.question3_page.pack(fill='both', expand=1)

    def question3_to_2(self):
        self.question3_page.pack_forget()
        self.question2_page.pack(fill='both', expand=1)

    def question2_to_1(self):
        self.question2_page.pack_forget()
        self.question1_page.pack(fill='both', expand=1)
    # =====================================================================#

    # ====FUNCTION TO CHANGE MAIN MENU FRAME TO STOP CODE REPEATING=======#
    def go_to_main_menu(self,frame_name):
        frame_name.pack_forget()
        self.main_page.pack(fill='both', expand=1)
    # =====================================================================#

    # ====FUNCTION TO CHANGE QUIZ FRAME TO STOP CODE REPEATING=======#
    def go_to_quiz_frame(self,frame_name):
        frame_name.pack_forget()
        self.quiz_page.go_to_main_menu.pack(fill='both', expand=1)
    # =====================================================================#
    # ====FUNCTION TO CHANGE QUIZ FRAME TO STOP CODE REPEATING=======#
    def go_to_module_frame(self,frame_name):
        frame_name.pack_forget()
        self.module_page.pack(fill='both', expand=1)
    # =====================================================================#

    #ZAHID
    def go_to_admin_frame(self,frame_name):
        frame_name.pack_forget()
        self.admin_page.pack(fill='both', expand=1)

    def go_to_add_frame(self,frame_name):
        frame_name.pack_forget()
        self.add_page.pack(fill='both', expand=1)

    def go_to_update_frame(self,frame_name):
        frame_name.pack_forget()
        self.update_page.pack(fill='both', expand=1)

    def go_to_delete_frame(self,frame_name):
        frame_name.pack_forget()
        self.delete_page.pack(fill='both', expand=1)

    # doent work properly
    def go_to_question_frame_add(self,frame_name):
        frame_name.pack_forget()
        self.question_page.pack(fill='both', expand=1)

    


    

    
