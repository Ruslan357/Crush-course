sandwich_orders = ['classic', 'pastrami', 'meat', 'pastrami', 'fish', 'pastrami', 'vegetarian', 'kids']
finished_sandwiches = []

print('Sorry, but in our cafe ended the pastrami\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print('\nA list of the sandwiches prepared:')
for sandwich in finished_sandwiches:
    print(sandwich)
