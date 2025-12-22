

class QuizBrain:
    def __init__(self, question_list):
        self.number = 0
        self.question_list = question_list
        self.score =0
    def still_has_questions(self):
        return self.number < len(self.question_list)
    def nextQuestion(self):
        current_question = self.question_list[self.number]
        ans = input(
            f"Q{self.number + 1}: {current_question.text} (True or False): "
        )

        if ans.lower() == current_question.answer.lower():
            self.score+=1
            print(f"You are correct! 🎉 {self.score}/{self.number+1}")

        else:
            print("You are wrong 😬")
        self.number+=1
    def finished_quiz():
        print("You finished the quiz")
        print(f"Your score : {self.score}/{self.number+1}")
    

    
            
        