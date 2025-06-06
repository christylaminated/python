#check voter eligibility
age = int(input("How old are you? ")) #age is an integer
x = 18 - age #x is an integer, 18-age is the number of years left to vote
if age >= 18: #if age is greater than or equal to 18
    print("Congratulations! You are eligible to vote. Go make a difference!")
else: #if age is less than 18
    print(f"Oops! You’re not eligible yet. But hey, only {x} more years to go!")

