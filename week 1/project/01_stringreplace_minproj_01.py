def stringreplace_min_proj():
    paragraph = input("Please input a paragraph:\n")
    print(paragraph)
    search_string = input("Please input a Search String:\n")
    x = paragraph.count(search_string)
    print(f"There are {x} occurrences.")
    choice = ""
    while choice.upper() != "N":
        choice = input("Do you want to replace the text [Y/N]?\n")
        if choice.upper() == "Y":
            string_new = input("Please input a replacement string:\n")
            paragraph_new = paragraph.replace(search_string, string_new)
            print(f"{x} words has been replaced from the paragraph")
            print(paragraph_new)
            break
        elif choice.upper() == "N":
            choice2 = input("Oh! you don't like to replace, Do you want to check again? [Y/N]\n")
            if choice2.upper() == "Y":
                stringreplace_min_proj()
            elif choice2.upper() == "N":
                break
        else:
            print("Please give proper input.")
            continue


stringreplace_min_proj()