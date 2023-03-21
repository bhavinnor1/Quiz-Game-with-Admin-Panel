
from Subject import *
from functools import partial
import tkinter as tk
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
class Quiz:
    def __init__(self):

        self._modules = []
        self.correct_count = 0
        self.incorrect_count = 0



    def set_module_list(self):
        self._modules = []
        self.database_list = cursor.execute("SELECT * FROM module").fetchall()

        for modules_lists in self.database_list:
            for module in modules_lists:
                self._modules.append(module)

    def get_module_list(self):
        return self._modules


