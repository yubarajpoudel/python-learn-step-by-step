'''
this is the simple tool that calculate the compound interest of the user
provide principal, time and rate by the user
'''

def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

print(greet.__doc__)

principal = int(input("Enter the principal amount: "))
time = int(input("\n Enter the time period: "))
rate = int(input("\n Enter the rate: "))

compoundInterest = 1+rate/4
compoundInterest = compoundInterest ** (4*time)
compoundInterest = principal * compoundInterest
print("your compoundInterest is {}".format(compoundInterest))