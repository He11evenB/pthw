# assigns 100 to the int variable cars
cars = 100
# assigns 4.0 to the float variable space_in_a_car
space_in_a_car = 4.0
# assigns 30 to the int drivers
drivers = 30
# assigns 90 to the int passengers
passengers = 90
# assigns the result of 100 - 30 into an int variable
cars_not_driven = cars - drivers
# assigns the int variable stored in drivers of 30 to variable cars_driven
cars_driven = drivers
# assigns the result of 30 x 4.0 into a float variable named carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# assigns the result of 90 / 30 into variable named average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
