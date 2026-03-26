questions = ("In human anatomy, what does the 'hallux' refer to?",
             "How many cards are in a standard deck of playing cards?",
             "What is the only planet in our solar system to rotate clockwise on its axis?")

options = (("A.foot","B.big toe","C.shoulder"),
           ("A.42","B.56","C.52"),
           ("A.venus","B.earth","C.moon"))

answers = ("B","C","A")
guesses = []
score = 0
question_number = 0

print("-----------------------")
for question in questions:
    print(f"{question_number+1}) "+question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        print(f"You guessed {guess}! is correct")
        score += 1
    else:
        print("You guessed incorrectly. Try again.")

    question_number += 1
    print("-----------------------")

for i,guess in enumerate(guesses,start=1):
    print(f"your guesses for question {i}) {guess}")
print("\n-----------------------")

for i,answer in enumerate(answers,start=1):
    print(f"The answers for the question {i}) {answer}")
print("\n-----------------------")

tot_score = (score /question_number)*100
print(f"Your total score is {tot_score:.2f}%")