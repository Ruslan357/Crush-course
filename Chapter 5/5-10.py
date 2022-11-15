current_users = ['User_1', 'User_2', 'User_3', 'User_4', 'User_5']
current_users_copy = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5']
new_users = ['user_23', 'USER_2', 'user_576', 'user_78', 'user_5']

for name in new_users:
    if name in current_users or name.lower() in current_users_copy:
        print('The user must select a new name')
    else:
        print('This name is still free')
