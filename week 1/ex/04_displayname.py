name = input("Input your name:")
amount = int(input("Input number of times to print:"))

if amount > 0:
    for i in range(amount):
        print(name)
else:
    print("No name entered")