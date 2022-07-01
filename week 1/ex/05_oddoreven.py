num = ""
def oddoreven(num):
    num = input("Input a number:")
    try:
        if int(num) % 2 == 0:
            print("The number you have entered is Even")
        elif int(num) % 2 == 1:
            print("The number you have entered is Odd")
    except ValueError:
        print("Not a valid Number")
oddoreven(num)
