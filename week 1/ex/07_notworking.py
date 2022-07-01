num = []
oddSum = []
evenSum = []
# def innum(num):
#     check = ""
#     while check != "stop":
#         num1 = int(input("Input a number:"))
#         num.append(num1)
#         check = input("Input stop to stop:")
#         print(num)
def innum(num):
    check = ""
    while check != "stop":
        try:
            num1 = int(input("input number:"))
            num.append(num1)
            print(num)
        except ValueError:
            print("Not a valid number")
        check = input("Input stop to stop:")
def oddandeven(num):
    for i in num:
        if i % 2 == 1:
            oddSum.append(i)
        else:
            evenSum.append(i)
    print(oddSum)
    print(evenSum)

innum(num)
oddandeven(num)