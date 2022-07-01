age = int(input("Please enter your age:"))
if age >= 18:
    print("You are eligible to vote")
elif age < 0:
    print("Age must be a positive digit")
else:
    print("You aren't adult yet... Sorry can't vote")