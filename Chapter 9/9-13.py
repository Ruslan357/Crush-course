from collections import OrderedDict

terms = OrderedDict()
terms['Integer (int)'] = 'Whole number'
terms['Float (float)'] = 'Decimal number'
terms['String (str)'] = 'Text'
terms['Boolean (bool)'] = 'True / False'
terms['List (list)'] = ' A “container” that can store any kind of values. ' \
                       'You can create a list with square brackets e.g.'

for term in terms.keys():
    print(f'{term} : {terms[term]}')
