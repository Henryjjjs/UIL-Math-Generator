import random
from abc import ABC, abstractmethod

answer_choices = 5
questions = 25

class Question:
    def __init__(self, question, answer_choice_list, correct_index):
        self.question = question
        self.answer_choice_list = answer_choice_list
        self.correct_index = correct_index


class QuestionGenerator(ABC):

    @abstractmethod
    def generate_value(self):
        pass

    @abstractmethod
    def generate_text(self, values):
        pass

    @abstractmethod
    def generate_answer(self, values):
        pass

    def generate_question(self):
        answers = []
        correct_index = random.randint(0, answer_choices - 1)
        correct_value = self.generate_value()
        question = self.generate_text(correct_value)

        for i in range(0, answer_choices):
            if i == correct_index:
                answers.append(self.generate_answer(correct_value))
            else:
                answers.append(self.generate_answer(self.generate_value()))

        return Question(question, answers, correct_index)
