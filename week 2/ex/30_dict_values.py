def dict_values(dictionary):
    item = dictionary.items()
    for key, value in item:
        print(key, ":", *value)
        print("*****")

dict_values(({120: ("Visal", "Borey", "Sovann"),
              130: ("Hout","Mouyleng","Pidor"),
              140: ("Nary","Misora", "Masaki") }))