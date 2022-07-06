def search_in_tuple(num,sno):
    for i in range (0,len(num)):
        if num[i] == sno:
            return i
    else:
        return -1

element_position = search_in_tuple((20,15,10,30),10)
if element_position == -1:
    print("Element not found in the tuple")
else:
    print(f"Element found at Index: {element_position}")