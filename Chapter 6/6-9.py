favorite_places = {'dima': ['dolomites', 'yellowstone', 'milford sound'],
                   'elena': ['red center', 'bruges'],
                   'max': ['tromso', 'loire valley', 'santorini']}
for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite places:")
    for pl in place:
        print(f'{pl.title()}')
    print()
