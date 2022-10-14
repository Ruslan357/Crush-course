ingredient = ""
while True:
    ingredient = input('Please enter an ingredient ')
    if ingredient == 'quit':
        break
    else:
        print(f'The {ingredient} is added to the pizza')
