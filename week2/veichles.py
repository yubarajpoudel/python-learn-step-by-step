from inherit import Car, Bike
bike1 = Bike("Bazaz", 200000, 150, 120, 'blue')
print(bike1.get_companyName())
print(bike1.getPriceAfterTax())

car1 = Car("Toyota", 2500000, 1200, 150, 'ac,musicsystem', 'left')
print(car1.get_companyName())
print(car1.getPriceAfterTax())