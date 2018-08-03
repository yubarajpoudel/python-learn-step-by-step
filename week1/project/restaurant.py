'''
programme to calculate the bill of the restaurant

'''
# These are two dictionaries that hold the information about the menu
menuMap = {'1':'momo', '2':'chowmein', '3':'tea'}
menu = {'momo':100, 'chowmein':150, 'tea':50}

def printMenu():
	'''
	Thiw will display the menu in the top to allow the user not to mistake duing the menu entry
	'''
	first = True
	i = 0
	for menuItem in menu.keys():
		i+=1
		if not first:
			print(",", end='')

		print("{id}. menuItem ".format(id=i), end='')
		first = False



def addOrder():
	order=[]
	cont = True
	while cont:
		order.append(input("Costumer order"))
		check = input("\nDo you want to continue ? (y/n): ")
		cont = (check == 'y')
		pass
	return order

def caluclateTotal(myOrders):
	print("\n\n\t\tCash Bill\n")
	totalBilled = 0
	for mOrder in myOrders:
		print(menuMap[mOrder]+"\t\tRs." +str(menu[menuMap[mOrder]]))
		totalBilled += menu[menuMap[mOrder]]

	print("\n------------------------------------------------")
	print("Your total bill amount = Rs.{}".format(totalBilled))
	vat = totalBilled*0.13
	serviceCharge = (totalBilled+vat)*0.25
	print("\t\tVAT(13%) = Rs."+str(vat))
	print("\t\tService charge(25%) = Rs." + str(serviceCharge))

	print("\t\tTotal = Rs."+ str(totalBilled+vat+serviceCharge)+ "\n\n")


print("\t\tBroadWay restaurant\t\t")
print("\n.............................................")
printMenu()
input("\n\nPress any key to continue.")
order = addOrder()		
caluclateTotal(order)







