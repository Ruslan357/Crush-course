favorite_languages = {
    'jen': 'python',
    'sarah': 'ruby',
    'edward': 'c',
    'phil': 'python',
    'jack': 'c++',
    'mark': '',
    'silvia': ''
}

for name in sorted(favorite_languages.keys()):
    if favorite_languages[name] != '':
        print(f'{name.title()}, thank you for pavticipating in the survey')
    else:
        print(f'{name.title()}, I suggest you join the survey')
