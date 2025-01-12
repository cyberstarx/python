questions = ("What's your favorite color?: ", 
             "How many bones are present in the human body?: ",
             "Who is the Prime Minister of India?: ",
             "In which continent is India situated?: ",
             "What is the color of the sky?: ")

options = (("A. Blue","B. White","C. Pink","D. Black"),
        ("A. 206","B. 200","C. 191","D. 29"), 
        ("A. Someone","B. The PM","C. No Ome","D. Rasputin"), 
        ("A. Asia","B. Africa","C. Australia","D. America"),
        ("A. Blue","B. Purple","C. White","D. Yellow"))

answers = ("D", "A", "B", "A", "A")
guesses = []
score = 0
question_num= 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("Incorrect :(")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("---------------")
print("RESULTS")
print("---------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int (score/ len(questions) * 100)
print(f"Your score is: {score}%")