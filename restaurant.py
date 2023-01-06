class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + " is a " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + " is now open")

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers
            print(self.number_served)
        else:
            print("Cannot reduce amount of cusomers served.")

    def increment_number_served(self, new_customers):
        self.number_served += new_customers
        print(self.number_served)



restaurant1 = Restaurant("abraham", "café")



restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(4)

##Returns error because you cannot have served less people
restaurant1.set_number_served(2)


restaurant1.set_number_served(6)
restaurant1.increment_number_served(3)



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "mint", "banana"]

    def print_icecream_flavor(self):
        print(self.flavors)

icecreamstand1 = IceCreamStand("bob's icecream stand", "Ice cream stand")
icecreamstand1.print_icecream_flavor()