def sum_of_list(*list):
    y = 0
    for num in list:
        y += num
    print(y)
my_list = [20,15,10,30]
sum_of_list(*my_list)