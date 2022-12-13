filename = "guest.txt"

with open(filename, 'w') as file_obgect:
    massage = input('Enter the name...')
    file_obgect.write(massage)
