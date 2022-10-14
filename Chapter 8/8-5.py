def describe_city(name,country='Ukraine'):
    '''format and show text'''
    print(f'{name.title()} is a {country.title()}')


describe_city('kyiv')
describe_city('london')
describe_city('paris')