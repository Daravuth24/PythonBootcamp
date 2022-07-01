num = input("Input a number:")
oddSum = []
evenSum = []
def checkoddeven(num):
    try:
        for j in range(1, int(num)):
            if j % 2 == 1:
                oddSum.append(j)
        print(f"Average of odd numbers = {sum(oddSum) / len(oddSum)}")
    except ValueError:
        print("Invalid Input")
    try:
        for i in range(1, int(num)):
            if i % 2 == 0:
                evenSum.append(i)
        print(f"Average of even numbers = {sum(evenSum)/len(evenSum)}")
    except ValueError:
        print("")

checkoddeven(num)

