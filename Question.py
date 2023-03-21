import sqlite3

'''
******* DELETE THIS DOCSTRING**************

PUT SET METHODS FOR DATABASE AND GET METHODS FOR THE LIST THAT HAS BEEN SET
AND PUT SOME COMMON ATTRIBUTES FROM CHILD CLASSES TO SUPER CLASSES


'''


connection = sqlite3.connect('database.db')
cursor = connection.cursor()


class Question:
    def __init__(self,question_name):
        self.question_name = question_name
        self.options = []









class MutlipleChoice(Question):
    def __init__(self,question_name):
        super().__init__(question_name)


    def get_description(self):
        database_list = cursor.execute(
            "SELECT answer_description FROM mc_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.description = database_list[0][0]
        return self.description


    def get_answer(self):

        database_list = cursor.execute(
            "SELECT option_answer FROM mc_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.answer = database_list[0][0]
        return self.answer

    def get_options_list(self):
        self.options = []
        database_list = cursor.execute(
            "SELECT option1, option2, option3, option_answer FROM mc_question WHERE question_text=?",
            [self.question_name]).fetchall()

        for option_list in database_list:
            for options in option_list:
                self.options.append(options)

        return self.options




class GapFilling(Question):
    def __init__(self,question_name):
        super().__init__(question_name)

    def get_description(self):
        database_list = cursor.execute(
            "SELECT answer_description FROM gap_filling_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.description = database_list[0][0]
        return self.description



    def get_answer(self):
        database_list = cursor.execute(
            "SELECT option_answer FROM gap_filling_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.answer = database_list[0][0]
        return self.answer





class TrueFalse(Question):
    def __init__(self,question_name):
        super().__init__(question_name)

    def get_description(self):
        database_list = cursor.execute(
            "SELECT answer_description FROM true_false_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.description = database_list[0][0]
        return self.description

    def get_answer(self):

        database_list = cursor.execute(
            "SELECT option_answer FROM true_false_question WHERE question_text=?",
            [self.question_name]).fetchall()

        self.answer = database_list[0][0]
        return self.answer

    def get_option_list(self):
        self.options = []
        self.database_list = cursor.execute(
            "SELECT option1, option_answer FROM true_false_question WHERE question_text=?",
            [self.question_name]).fetchall()

        for option_list in self.database_list:
            for options in option_list:
                self.options.append(options)

        return self.options