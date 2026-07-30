#if else statements to determine Letter Scores

midterm_score=int(input("Please enter your midterm score: "))
final_score=int(input("Please enter your final score: "))

letter_score=(midterm_score*0.4)+(final_score*0.6)


if (letter_score>=50):
    if (50<letter_score and letter_score<=60):
        print("Your letter score is DC")
    elif (60<letter_score and letter_score<=70):
        print("Your letter score is CC")
    elif (70<letter_score and letter_score<=80):
        print("Your letter score is BC")
    elif (80<letter_score and letter_score<=85):
        print("Your letter score is BB")
    elif (85<letter_score and letter_score<=90):
        print("Your letter score is BA")
    elif (90<letter_score and letter_score<=100):
        print("Your letter score is AA, Well done!")
    
else:
    print("Your letter score is VF. You have failed the class")


