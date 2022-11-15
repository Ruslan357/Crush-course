class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The name of restaurant is {self.restaurant_name.title()}')
        print(f'The cuisine type is {self.cuisine_type}\n')

    def open_restaurant(self):
        print('The restaurant is open!')


american_rest = Restaurant('true burger bar', 'american')
korean_rest = Restaurant('kin kao', 'korean')
indian_rest = Restaurant('rangoli', 'indian')

american_rest.describe_restaurant()
korean_rest.describe_restaurant()
indian_rest.describe_restaurant()
