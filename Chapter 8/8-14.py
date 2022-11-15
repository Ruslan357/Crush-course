def car(company, model, **car_info):
    '''creates a dictionary that contains car information'''
    car_info['company'] = company
    car_info['model'] = model
    return car_info


information = car('audi', 'A6', colour='white', additional_functionality='does not have')
print(information)
