print("--------Welcome to Bill Splitter App--------")
print("Enter your details.....")
# Ask for bill amount and total no. of peoples
bill = float(input("Enter your bill amount: "))
persons = int(input("How many people you are: "))

# edge cases
if persons <=0:
    print("There should be atleat 1 people to split the bill!")
else:
    # Calculate and disply the result
    split = (bill/persons)
    print(f"Your total bill amount was {bill}")
    print(f"Each of {persons} people pays: {split:.2f}")

# Greetings 
print("Thanks see you again!!")