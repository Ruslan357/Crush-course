filename = "learning_python.txt"

with open(filename) as file_obgect:
    for line in file_obgect:
        print(line.replace('Python', 'C').strip())
