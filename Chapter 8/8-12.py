def sandwich(*ingredients):
    '''Shows list of ingredients for sandwich'''
    print('The list of ingredients in a sandwich:')
    for ingredient in ingredients:
        print(f'- {ingredient}')
    print()


sandwich('bread', 'cheese', 'meat', 'tomato', 'cucumber', 'onions', 'sauce')
sandwich('bread', 'sausage', 'cucumber', 'onions', 'sauce')
sandwich('bread', 'fish', 'sauce', 'onions')
