names = ['Dmitry', 'Ruslan', 'admin', 'Marry', 'Olga']
for name in names:
    if name == 'admin':
        print(f'Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for login in again.')
