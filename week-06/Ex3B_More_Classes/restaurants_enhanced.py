class Restaurant:
    """Represent a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        amount = int(input("How many customers served today? "))
        self.number_served += amount

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers") 

    def customer_rating(self):
        while True:
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5? "))
                if 1 <= rating <+ 5:
                    break
                print("Please enter a number from 1 to 5.")
            except ValueError:
                print("Please enter a whole number from 1 to 5.")

        self.customer_ratings.append(rating)
        average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for this restaurant is {average:.1f}.")

restaurant1 = Restaurant("Wendy's", "burgers")
restaurant2 = Restaurant("Taco Bell", "American food")
restaurant3 = Restaurant("Applebee's", "American food")

for restaurant in (restaurant1, restaurant2, restaurant3):
        restaurant.print_num_served()
        restaurant.add_num_served()
        restaurant.add_num_served()
        restaurant.print_num_served()

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

restaurant1.customer_rating()
restaurant1.customer_rating()

restaurant2.customer_rating()
restaurant2.customer_rating()

restaurant3.customer_rating()
restaurant3.customer_rating()



