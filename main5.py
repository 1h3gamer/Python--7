import random

class fruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red",
                     "orange":"orange",
                     "watermelon":"green",
                     "bananan":"yellow",
                     "grapes":"purple",
                     "blackberry":"black"}
        
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer=input()

            if(user_answer.lower()==color):
                print("Your answer is correct")
            else:
                print("Your answer is incorrect")

            option = int(input("Enter 0 if you wqant to play again otherwise enter 1: "))
            if option == 1:
                break

print("Welcome to the fruit quiz")
fq = fruitQuiz()
fq.quiz()