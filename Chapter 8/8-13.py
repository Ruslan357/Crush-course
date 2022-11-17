def build_profile(first, last, **user_info):
    '''creates a dictionary that contains user information'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Ruslan', 'Morozov', location='Ukraine', field='medicine')
print(user_profile)
