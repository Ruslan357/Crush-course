names = ['Dima', 'Evgeniy', 'Olga', 'Sasha', 'Artem', 'Igor']
for i in names:
    print(f'Hello, {i} ! I invite you to dinner')

print(f"\n{names[2]} can't come")
del names[2]
print(names)

print('\nWe found a big dining table!\n')
names.insert(0, 'Lera')
names.insert(4, 'Katya')
names.append('Sergey')
for i in names:
    print(f'Hello, {i} ! I invite you to dinner')

print('Unfortunately, we can only invite two guests')

while len(names) > 2:
    massage = names.pop()
    print(f"{massage}, i'm sorry that I can't invite youto dinner.")

for i in names:
    print(f'{i}, you are  still invited to dinner!')

    del names[1]
    del names[0]

    print(names)