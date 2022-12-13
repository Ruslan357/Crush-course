filename = "guest_book.txt"

with open(filename, 'w') as file_obgect:
    run = True
    while run:
        name = input('Enter the name... ')
        print(f'Hello, {name}!')
        if name == 'exit':
            run = False
        else:
            file_obgect.write(f'Hello, {name}!\n')
