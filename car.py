class Car:
 def __init__(self, car_brand, car_color):
        self.brand = car_brand
        self.color = car_color

 def honk(self):
        print(f"beep beep! I am a {self.color} {self.brand}.")

my_first_car = Car("Benz","White")
my_second_car = Car("Venza","Black")
print(my_first_car.brand)
print(my_second_car.color)
my_second_car.honk()
my_first_car.honk()