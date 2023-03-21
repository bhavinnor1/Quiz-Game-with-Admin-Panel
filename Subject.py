from functools import partial
import tkinter as tk
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
class Subject:

    def __init__(self,subject_name):
        self.subject_name = subject_name



        self._multiple_choice_questions = []
        self._gap_filling_questions = []
        self._true_false_questions = []


        
        
    def set_multiple_choice_question_list(self):
        self._multiple_choice_questions = []
        self.database_list_1 = cursor.execute("SELECT question_text FROM mc_question WHERE subject_name=?",
                                              [self.subject_name]).fetchall()

        for subjects_lists in self.database_list_1:
            for subject in subjects_lists:
                self._multiple_choice_questions.append(subject)

    def get_multiple_choice_question_list(self):
        return self._multiple_choice_questions


    def set_gap_filling_question_list(self):
        self._gap_filling_questions = []
        self.database_list_2 = cursor.execute("SELECT question_text FROM gap_filling_question WHERE subject_name=?",
                                              [self.subject_name]).fetchall()

        for subjects_lists2 in self.database_list_2:
            for subject2 in subjects_lists2:
                self._gap_filling_questions.append(subject2)

    def get_gap_filling_question_list(self):
        return self._gap_filling_questions


    def set_true_false_question_list(self):
        self._true_false_questions = []
        self.database_list_3 = cursor.execute("SELECT question_text FROM true_false_question WHERE subject_name=?",
                                              [self.subject_name]).fetchall()

        for subjects_lists3 in self.database_list_3:
            for subject3 in subjects_lists3:
                self._true_false_questions.append(subject3)

    def get_true_false_question_list(self):
        return self._true_false_questions









