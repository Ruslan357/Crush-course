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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['plombir', 'sorbet', 'sherbet', 'milk']

    def list_of_icecreams(self):
        for icecream in self.flavors:
            print(f'{icecream.title()}')


restaurant = IceCreamStand('umka', 'icecream')
restaurant.list_of_icecreams()
