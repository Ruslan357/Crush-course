pizzas = ['Carbonara', 'Mozzarella', 'Pepperoni']
friend_pizzas = pizzas[:]
pizzas.append('Cheese')
friend_pizzas.append('Meat')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)