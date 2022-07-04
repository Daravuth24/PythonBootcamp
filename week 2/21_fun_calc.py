def fun_calc(num1, num2, operator):
    if operator == "+":
        y = num1 + num2
        return print("Product:\n", y, "\n", "Process:", num1, "+", num2, "=", y)
    elif operator == "-":
        y = num1 - num2
        return print("Product:\n", y, "\n", "Process:", num1, "-", num2, "=", y)
    elif operator == "*":
        y = num1 * num2
        return print("Product:\n", y, "\n", "Process:", num1, "*", num2, "=", y)
    elif operator == "/":
        y = num1 / num2
        return print("Product:\n", y, "\n", "Process:", num1, "/", num2, "=", y)
    else:
        return -1
fun_calc(50,2,"*")