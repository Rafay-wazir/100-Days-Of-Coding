from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

Quiz = QuizBrain(question_bank)


while Quiz.still_has_questions():
    Quiz.next_question()

print("You Have Completed The Quiz. ")
print(f"You Final Score Is {Quiz.score}/{Quiz.question_number}")