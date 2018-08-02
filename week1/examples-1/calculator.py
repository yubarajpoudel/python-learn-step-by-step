# simple calculator
# performs the basic mathematical operations
# Continue to perform the airthematic operation untill user press the y key

'''
Define variable to hold the two input number
one variable to hold the choice
one variable to hold the operator
'''

a = 0
b = 0
choice = 'y'
result = 0
ops = '+'

print("\t\t calculator \t\t\n")
print("----------------------------------\n")

while choice == 'y' :
	#ask user to enter the number
	a = int(input("Enter the first number ")) # int is added to convert the input value of keyboard string to integer
	b = int(input("\nEnter the second number "))

	ops = input("What you like to do ? (+,-,/,*): ")

	# this condition apply the airthematic operation in the basis of user choice
	if ops == '+':
		result = a+b
	elif ops == '-':
		result = a-b
	elif ops == '/':
		result = a/b
	else:
		result = a*b

	print("output = {}".format(str(result)))

	choice = input("Do you want to Continue ?(y/n): ")

else :
	print("Thanks for using our calculator")
