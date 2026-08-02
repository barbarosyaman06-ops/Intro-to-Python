#is entered letter a caiptal letter or not


myNumber=input("Enter a letter: ")
if(len(myNumber)!=1):
    print("Please enter only one letter.")
else:
    if(myNumber.isalpha()):
        if(myNumber.isupper()):
            case="capital"
        else:
            case="small"
        vowels="AEIOUaeiou"
        if(myNumber in vowels):
            letter_type="vowel"
        else:
            letter_type="consonant"
        print(f"Entered letter {myNumber} is a {letter_type} and {case} letter")
    else:
        print(f"Entered letter {myNumber} is not a letter")

