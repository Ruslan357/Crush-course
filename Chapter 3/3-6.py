names = ['Dima', 'Evgeniy', 'Olga', 'Sasha', 'Artem', 'Igor']
for i in names:
    print(f'Hello, {i} ! I invite you to dinner')

print(f"\n{names[2]} can't come")
del names[2]
print(names)

print('\nWe found a big dining table!\n')
names.insert(0, 'Lera')
names.insert(len(names)/2, 'Katya')
names.append('Sergey')
for i in names:
    print(f'Hello, {i} ! I invite you to dinner')
