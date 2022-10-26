class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print('Information about the user:')
        print(f'First name: {self.first_name.title()}')
        print(f'Last name: {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'City: {self.city.title()}\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!\n')


user_1 = User('ruslan', 'morozov', '27', 'kiyv')
print(user_1.login_attempts)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
