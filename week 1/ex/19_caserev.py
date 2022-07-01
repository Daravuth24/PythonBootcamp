stri = input("Enter a string:")
def caserev(stri):
    newstr = ""
    for i in range(len(stri)):
        if stri == "":
            print("The string is empty.")
        elif stri[i].isupper():
            newstr += stri[i].lower()
        elif stri[i].islower():
            newstr += stri[i].upper()
    print(newstr)
caserev(stri)
