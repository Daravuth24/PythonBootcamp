str = input("Input a string:")
def uprlow(str):
    if str == "":
        print("The string is empty.")
    else:
        s1 = str[0:len(str) // 2]
        s2 = str[len(str) // 2:]
        print(s1.upper(), end ="")
        print(s2.lower())
uprlow(str)