pet_1 = {'cat': 'jen'}
pet_2 = {'dog': 'phil'}
pet_3 = {'parrot': 'sarah'}
pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for k, v in pet.items():
        print(f'{v.title()} has a {k.title()}')
