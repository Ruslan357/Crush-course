filename = "learning_python.txt"

with open(filename) as file_obgect:
    print(file_obgect.read())

with open(filename) as file_obgect:
    my_list = file_obgect.readlines()
    for line in my_list:
        print(line.strip())

with open(filename) as file_obgect:
    for line in file_obgect:
        print(line.strip())
    print()
