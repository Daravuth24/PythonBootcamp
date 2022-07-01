stri = input("Input a string:")
def asciialpha(stri):
    if stri == "":
        print("The string is empty.")
    else:
        for i in stri:
            ascii = ord(i)
            print(f"{i}:{ascii}")
asciialpha(stri)