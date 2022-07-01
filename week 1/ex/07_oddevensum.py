num = input("Input a number:")
evenSum = []
oddSum = []
def checkevenodd(num):
    try:
        for j in range (1, int(num)):
            if j % 2 == 1:
                oddSum.append(j)
        print(f"Sum of odd numbers = {sum(oddSum)}")
    except ValueError:
        print("Invalid Input")
        print("Sum of odd numbers = 0")
    try:
        for i in range (1,int(num)):
            if i % 2 == 0:
                evenSum.append(i)
        print(f"Sum of even numbers = {sum(evenSum)}")
    except ValueError:
        print("Sum of even numbers = 0")

checkevenodd(num)