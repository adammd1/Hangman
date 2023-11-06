guess = input("Enter a single letter")
if len(guess)== 1 & guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
