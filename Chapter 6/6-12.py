cities = {'lviv': {'country': 'ukraine', 'population': '721 301 '},
          'new york': {'country': 'usa', 'population': '8380000'},
          'london': {'country': 'great britain', 'population': '8982000'}}
for city, inf in cities.items():
    print(f'{city}: ')
    for k, v in inf.items():
        print(f'{k} - {v}')
    print()
