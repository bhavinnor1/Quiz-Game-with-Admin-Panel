
from functools import partial
import tkinter as tk
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

class Module:

    def __init__(self,module_name):
        
        self.module_name = module_name
        self.module_correct_count = 0
        self.module_incorrect_count = 0
        self._subjects = []




    def module_increment_corrects(self):
        self.module_correct_count += 1

    def module_increment_incorrects(self):
        self.module_incorrect_count += 1

    def set_subject_list(self):
        self._subjects = []
        self.database_list = cursor.execute("SELECT subject_name FROM subject WHERE module_name=?",
                                            [self.module_name]).fetchall()

        for data in self.database_list:
            for values in data:
                self._subjects.append(values)

    def get_subject_list(self):
        return self._subjects
