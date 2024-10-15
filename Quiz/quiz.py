class Question:
    def __init__(self, questionText, answer):
        self.questionText = questionText
        self.answer = answer
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'

quizQuestions = [
    Question("Question 1. What city is the capital of Australia", "Canberra"),
    Question("Question 2. What city is the capital of Japan", "Tokyo"),
    Question("Question 3. How many islands does the Philippines have", "7100"),
    Question("Question 4.  Who developed Python Programming Language?","Guido van Rossum"),
    Question("Question 5. Is Python case sensitive when dealing with identifiers?", "Yes"),
    Question("Question 6. What is the correct extension of the Python file?",".py"),
    Question("Question 7. Is Python code compiled or interpreted","Both"),
    Question("Question 8. What is used to define a block of code in Python language?","Indentation"),
    Question("Question 9. Which keyword is used for function in Python language?","def"),
    Question("Question 10. Which character is used to give single-line comments in Python?","#")
]
print("****************************************************")
print("****************************************************")


for question in quizQuestions:
    print(f"{question.questionText}?")
    userInput = input("Answer:")

    if (userInput.lower() == question.answer.lower()):
        print("That is correct!")
    else:
        print(f"Sorry, the correct answer is {question.answer}.")
print("------------------------*****------------------------")        