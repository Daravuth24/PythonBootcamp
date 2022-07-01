str = input("Input a string:")
def firstlast(str):
    if str == "":
        print("The string is empty.")
    else:
        s1 = str[0]
        s2 = str[-1]
        print(f"First Character: {s1}")
        print(f"Last Character: {s2}")
firstlast(str)