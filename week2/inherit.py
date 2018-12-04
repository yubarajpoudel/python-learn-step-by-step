class TransportItem:
	company_name = ""
	price=0
	horsepower = 0
	top_speed = 0

	def __init__(self, company_name, price, horsepower, top_speed):
		self.company_name = company_name
		self.price = price
		self.top_speed = top_speed
		self.horsepower = horsepower
		pass

	def get_companyName(self):
		return self.company_name 

class Car(TransportItem):
	fullbody_features = ''
	driver_handed = ''
	def __init__(self, company_name, price, horsepower, top_speed, fullbody_features, driver_handed):
		super().__init__(company_name, price, horsepower, top_speed)
		self.fullbody_features = fullbody_features
		self.driver_handed = driver_handed
		pass

	def getFullBodyFeatures(self):
		return self.fullbody_features

	def getPriceAfterTax(self):
		priceAfterTax = 3 * self.price
		return priceAfterTax

class Bike(TransportItem):
	color='red'
	def __init__(self, company_name, price, horsepower, top_speed, color):
		super().__init__(company_name, price, horsepower, top_speed)
		self.color = color
		pass

	def getColor(self):
		return self.color

	def getPriceAfterTax(self):
		return self.price * 2

# 	def get_companyName(self):
# 		return self.company_name 
