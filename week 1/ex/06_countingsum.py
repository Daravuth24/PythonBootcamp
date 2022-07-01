sum1 = []
def usernum(sum1):
    check = ""
    while check != "stop":
        try:
            num = int(input("input number:"))
            sum1.append(num)
            print(sum1)
        except ValueError:
            print("Not a valid number")
        check = input("Input stop to stop:")
def sumofnum(sum1):
    sum1 = sum(sum1)
    print(f"The sum is: {sum1}")
usernum(sum1)
sumofnum(sum1)