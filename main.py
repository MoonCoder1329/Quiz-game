import random
from data import question_data

def choice_question():
    result = 0
    total = 0
    for item in range(0, len(question_data)):
        result+=1
        choice = question_data[item]
        choice_text = choice["text"]
        choice_answer = choice["answer"]
        answer = input(f"{choice_text} (True/False): ").capitalize()
        if answer == choice_answer:
            total += 1
            print("You got it right\n"
                  f"The correct answer was: {choice_answer}\n"
                  f"Your current score is: {total}/ {result}")
        elif answer != choice_answer:
            print(f"That's wrong\n"
                  f"The correct answer was: {choice_answer}\n"
                  f"Your current score is: {total}/ {result}\n")
    print(f"Your Score {total} / {result}")

start = True
while start:
    choice_question()
    continue_game = input ("Do you want to play again?: ( Y / N): ").lower()
    if continue_game == "n":
        print("Take care, see you again. The game is over.")
        start = False


