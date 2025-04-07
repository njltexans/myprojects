#Creating a quiz game 

questions = ("What is the capital of France? ", 
             "Who was the 2011 MBA MVP? ",
             "Who was the second president of the United States? ",
             "What is the largest cryptocurrency in the world currently, by market cap? ",
             "What is the color of the angry bird that splits into three seperate birds when the screen is tapped? ")

options = (("A) Paris ", "B) London ", "C) Berlin ", "D) Madrid "), 
           ("A) Lebron James ", "B) Kobe Bryant ", "C) Kevin Durant ", "D) Derrick Rose "), 
           ("A) George Washington ", "B) John Adams ", "C) Thomas Jefferson ", "D) James Madison "), 
           ("A) Bitcoin ", "B) Ethereum ", "C) Ripple ", "D) Litecoin "), 
           ("A) Red ", "B) Yellow ", "C) Blue ", "D) Green "))

answers = ("A", "C", "B", "A", "A")
guesses = []
score = 0

question_number = 0


for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("That is COOOORRRREEEECCCTTT!")
        print(f"Your current score is {score}/{question_number + 1}")
    else:
        print("I am sorry buddy but that is not the correct answer :(")
        print(f"The correct answer is {answers[question_number]}")
        print(f"Your current score is {score}/{question_number + 1}")  
    

    question_number += 1

print("--------------------------------------------------------------------------------")
print("    Here are the quiz results! The MOMENT YOU'VE BEEN WAITING FOR!    ")
print("--------------------------------------------------------------------------------")
print(f"Your final score on this AWESOME quiz was {score} out of {len(questions)}")
if score == len(questions):
    print("WOW got a perfect score! You are way smarter then the average bear!")
elif score >= 3:
    print("Not to shabby, you're about as smart as the average bear")
else:
    print("Yikes, you better get back in the library and spend less time on TikTok. (You are not smarter then the average bear)")
print("-----------------------------")
