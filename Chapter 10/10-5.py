filename = "Why do you like to program.txt"

with open(filename, 'w') as file_obgect:
    run = True
    while run:
        answer = input('Why do you like to program? ')
        if answer == 'exit':
            run = False
        else:
            file_obgect.write(answer)
