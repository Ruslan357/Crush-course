friend_1 = {'first_name': 'Evgeny', 'last_name': 'Starostenko', 'age': '27', 'city': 'Kyiv'}
friend_2 = {'first_name': 'Dima', 'last_name': 'Tsaruk', 'age': '20', 'city': 'Rivne'}
friend_3 = {'first_name': 'Ulia', 'last_name': 'Pozdnyakova', 'age': '38', 'city': 'Kyiv'}
people = [friend_1, friend_2, friend_3]

for friend in people:
    for val in friend.values():
        print(f'{val} ', end=' ')
    print()
