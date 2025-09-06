# add/remove item
# check availability of an item

class Restaurant:
    '''
        Restaurant that contain an initial menu item list
        Methods: add_item, remove_item, check_item
    '''
    menu = ["Pizza", "Burger", "Pasta", "Salad"]

    def add_item(self, item):
        '''
            Adds an item to the restuarant menu
        '''
        self.menu.append(item)
        print(f'Updated menu: {self.menu}')

    # Handles item that doesn't exists
    def remove_item(self, item):
        '''
            Removes an item from the restuarant menu if it exists
        '''
        if item in self.menu:
            self.menu.remove(item)

    def check_item(self, item):
        '''
            Checks availability of an item in the menu
        '''
        availability = 'available' if item in self.menu else 'not available'
        print(f'Availability: "{item} is {availability}"')
        

restaurant = Restaurant()
restaurant.add_item('Tacos')
restaurant.remove_item('Salad')
restaurant.check_item('Pizza')