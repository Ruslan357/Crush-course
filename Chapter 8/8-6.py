def city_country(city, country):
    '''format and returns text'''
    temp = f'"{city.title()}, {country.title()}"'
    return temp


text = city_country('kiyv', 'ukraine')
print(text)

text = city_country('london', 'great britain')
print(text)

text = city_country('paris', 'france')
print(text)