def and_operation(x, y):
    lst = []
    list1 = []
    list2 = []
    try:

        print(f"and_operation({x, y})")

        hexnum1 = x

        hexnum2 = y

        decnum1 = int(hexnum1, 16)

        decnum2 = int(hexnum2, 16)

        binnum1 = bin(decnum1).replace("0b", "")

        binnum2 = bin(decnum2).replace("0b", "")

        for i in binnum1:
            list1.append(i)
        for j in binnum2:
            list2.append(j)
        for t in range(len(list1)):
            listadd = (int(list1[t]) + int(list2[t]))
            lst.append(listadd)
        print(f"{binnum1} \n{binnum2} \n\n")
        print(lst)

    except ValueError:

        print("This is not a hexa-decimal number")


and_operation("33", "3D")
