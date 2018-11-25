# take the name, phone, address from 
# keyboard of n number of training institute

# for holding the n number of the institutes
intitutes = []
moreInstitue = True
while moreInstitue :
	name = input("enter the name: ")
	# take the value of other params like name
	institute = {'name': name}
	intitutes.append(institute)
	choice = input("Do you want to continue (y/n): ")
	if choice == 'y':
		moreInstitue = True
	elif choice == 'n':
		moreInstitue = False
	pass
else:
	print(intitutes)


