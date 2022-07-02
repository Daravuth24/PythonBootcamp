upr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lwr_letters = "abcdefghijklmnopqrstuvwxyz"
while True:
    userinput = input("Press 1 to encode\nPress 2 to decode\n")
    print("Enter the string to encode:")

    def translate():
        message = input("")
        translated = ''
        for char in message:
            if char.isupper():
                transChar = (upr_letters.find(char) + 13) % 26
                translated += upr_letters[transChar]
            elif char.islower():
                transChar = (lwr_letters.find(char) + 13) % 26
                translated += lwr_letters[transChar]
            else:
                translated += char
        if userinput == "1":
            print(f"The encoded text: {translated}")
        else:
            print(f"The decoded text is: {translated}")
    translate()
    if input("Do you want to continue? [Y/N]") == 'N':
        break
