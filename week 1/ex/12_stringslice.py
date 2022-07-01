str = input("Input a text:")
def slicing(str):
    if str == "":
        print("The string is empty.")
    else:
        s1 = str[0:len(str)//2]
        s2 = str[len(str)//2:]
        print(s1)
        print(s2)
slicing(str)