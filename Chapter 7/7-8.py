sandwich_orders = ['classic', 'meat', 'fish', 'vegetarian', 'kids']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print('\nA list of the sandwiches prepared:')
for sandwich in finished_sandwiches:
    print(sandwich)
