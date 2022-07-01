str = input("Input a text:")
def slicing(str):
    s1 = str[0:len(str)//2]
    s2 = str[len(str)//2:]
    print(s1)
    print(s2)
slicing(str)