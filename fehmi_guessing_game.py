import random

random_number=random.randint(1,100)

score=100
remaining_attempt=5
attempt_count=0

print("Please Guess a Number Between 1 And 100!")
print(f"Your Starting Score is {score}")


while (remaining_attempt>0):
    guessed_number=int(input("Please Guess: "))
    if (guessed_number<1 or guessed_number>100):
        print("Please Enter a Number Between 1 And 100!")
        continue
    attempt_count+=1
    if (guessed_number==random_number):
        print(f"Congratulations! You Have Guessed The Number On Your {attempt_count}.attempt")
        print(f"Your total score is {score}")
        break
    elif(guessed_number<random_number):
        print("Try a Larger Number!")
    else:
        print("Try a Smaller Number!")
    remaining_attempt-=1
    score-=15
    if(remaining_attempt>0):
        print(f"Remaining Attempts: {remaining_attempt}")
        print(f"Current Score: {score}")
    else:
        print("GAME OVER")
        print(f"Your Score Is {score}")
      
        
