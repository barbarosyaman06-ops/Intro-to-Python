import random

random_number=random.randint(1,100) #generates a number in the selected interval
remaining_attempts=5 #the player has 5 guesses.
score=100 #starter score
attempt_count=0 #guesses attempted
print("Guess a number between 1 and 100")
print(f"Your starter score is {score}")


while remaining_attempts>0:
    guessed_number=int(input("Guessed Number: "))
    attempt_count+=1

    if guessed_number==random_number:
        print(f"You have guessed the random number! Congrats\nScore: {score}\n Attempts: {attempt_count}")
        break
    elif guessed_number!=random_number:
        print("Please Try Again!")
        attempt_count+=1
        score -=10
        remaining_attempts-=1
else:
    print("Game Over You Have Run Out Of Attempts.")
    print(f"The Secret Number Was: {random_number}")