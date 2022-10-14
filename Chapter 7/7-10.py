places = []

while True:
    place = input('\nIf you could visit only one mission in the world, where would you go? ')
    places.append(place)

    answer = input('do you want to continue with the survey? (y/n) ')
    if answer == 'n':
        break

print('\nList of places:')
for place in places:
    print(place)
