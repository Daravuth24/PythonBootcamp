def write_file(name, content):
    while True:
        choice1 = input(f"Are you sure you want to replace {name}?[Y/N]")
        try:
            while True:

                if choice1.upper() == "Y":
                    filecreate = open(name, "w")
                    filecreate.write(content)
                    return 1

                elif choice1.upper() == "N":
                    return 0

                else:
                    print("Invalid Option")
                    break

        except FileExistsError:
            continue


write_file("test_write.txt", "Hello World")
