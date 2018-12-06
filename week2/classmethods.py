# class methods
# A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.

# The difference between a static method and a class method is:

# Static method knows nothing about the class and just deals with the parameters
# Class method works with the class since its parameter is always the class itself.
class Product:
	name = "sample"
	price=0

	def __init__(self, name, price):
		self.name = name
		self.price = price
	
	@staticmethod
	def addData(name, price):
		return Product(name, price)

	@classmethod
	def addDetail(self, name, price):
		return self(name, price)

	def showDetail(self):
		return ("Product : {pName} price: {pPrice}".format(pName = self.name, pPrice = self.price))

product1 = Product("laptop", 50000)
print(product1.showDetail())

product2 = Product.addData("water", 20)
print(product2.showDetail())

product3 = Product.addDetail("Television", 340000)
print(product3.showDetail())

