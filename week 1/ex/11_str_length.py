def lenstr():
    str = input("Enter a string:")
    if str == "":
        print("The string is empty.")
    else:
        print(str)
        print(len(str))

lenstr()