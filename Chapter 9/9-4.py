class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of restaurant is {self.restaurant_name.title()}')
        print(f'The cuisine type is {self.cuisine_type}')
        print(f'Number of reserved tables: {self.number_served}\n')

    def set_numbers_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def open_restaurant(self):
        print('The restaurant is open!')


restaurant = Restaurant('puzata hata', 'ukrainian')
restaurant.describe_restaurant()

restaurant.number_served = 5
restaurant.describe_restaurant()

restaurant.set_numbers_served(10)
restaurant.describe_restaurant()

restaurant.increment_number_served(5)
restaurant.describe_restaurant()
