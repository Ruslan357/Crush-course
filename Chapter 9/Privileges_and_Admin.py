from User import User


class Privileges():
    def __init__(self):
        self.privileges = ['allowed to add messages', 'allowed to delete users', 'allowed ban users']

    def show_privileges(self):
        print('Privileges of admins:')
        for privilege in self.privileges:
            print(f'{privilege}')


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

    def show_privileges(self):
        print('Privileges of admins:')
        for privilege in self.privileges:
            print(f'{privilege}')
