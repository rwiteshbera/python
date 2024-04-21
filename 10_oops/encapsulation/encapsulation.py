class Car:
    def __init__(self, make, model, year):
        self._make = make    # protected attribute
        self._model = model  # protected attribute
        self.__year = year   # private attribute
 
    # public method to access private attribute
    def get_year(self):
        return self.__year

    # public method to set private attribute
    def set_year(self, year):
        self.__year = year

    # public method to display car details
    def display(self):
        print(f"Car: {self._make} {self._model}, Year: {self.__year}")


# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Accessing public method to get private attribute
print("Year of the car:", my_car.get_year())

# Trying to access private attribute directly (will result in an error)
# print(my_car.__year)

# Modifying private attribute using public method
my_car.set_year(2023)
print("Modified year of the car:", my_car.get_year())

# Displaying car details using a public method
my_car.display()
