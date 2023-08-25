# Gregory Campbell  lab10-9     February 23, 2022
"""
    The Question class holds data for trivia questions. It has attributes for
    a trivia question, four possible answers, and the number of the correct
    answer (1, 2, 3, or 4), and the necessary accessors, mutators, and __init__
    method.
"""
class Question():
    # the __init__ method initializes a question object
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
         self.__question = question
         self.__answer1 = answer1
         self.__answer2 = answer2
         self.__answer3 = answer3
         self.__answer4 = answer4
         self.__correct_answer = correct_answer

    # mutator methods
    # each of these assigns values to the attribute fields
    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    # accessor methods
    # each of these returns the values of the attribute fields
    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct_answer(self):
        return self.__correct_answer

    # the __str__ method returns a string displaying the question and possible answers
    def __str__(self):
        return f'---------------\n\n{self.__question}\n\n1. {self.__answer1}\n\n2. {self.__answer2}\n\n3. {self.__answer3}\n\n4. {self.__answer4}\n'

