from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank =[]
for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))
print(question_bank[1].text)
quiz = QuizBrain(question_bank)
while(quiz.still_has_questions()): 
    quiz.nextQuestion()
    

