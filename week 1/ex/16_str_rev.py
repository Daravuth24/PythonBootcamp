str = input("Input a string:")
def strrev(str):
    if str == "":
        print("The string is empty.")
    else:
        s1 = str[(len(str) // 2)-1::-1]
        s2 = str[len(str) // 2:]
        print(s1, end="")
        print(s2)
strrev(str)