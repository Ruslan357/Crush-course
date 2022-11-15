class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.city = city

    def describe_user(self):
        print('Information about the user:')
        print(f'First name: {self.first_name.title()}')
        print(f'Last name: {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'City: {self.city.title()}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!\n')


user_1 = User('dmitry', 'tsaruk', '20', 'rivne')
user_2 = User('ruslan', 'morozov', '27', 'kiyv')
user_3 = User('julia', 'pozdnyakova', '38', 'odessa')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
