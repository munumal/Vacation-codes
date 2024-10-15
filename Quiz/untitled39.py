# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:24:28 2024

@author: Musaddique
"""

import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, questionText, answer):
        self.questionText = questionText
        self.answer = answer

    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'

quizQuestions = [
    Question("What city is the capital of Australia", "Canberra"),
    Question("What city is the capital of Japan", "Tokyo"),
    Question("How many islands does the Philippines have", "7100")
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text=quizQuestions[self.current_question].questionText)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = quizQuestions[self.current_question].answer.lower()
        if user_answer == correct_answer:
            messagebox.showinfo("Result", "That is correct!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Sorry, the correct answer is {quizQuestions[self.current_question].answer}.")
        self.answer_entry.delete(0, tk.END)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(quizQuestions):
            self.question_label.config(text=quizQuestions[self.current_question].questionText)
        else:
            messagebox.showinfo("Quiz Completed", f"You've completed the quiz! Your score is {self.score}/{len(quizQuestions)}.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
