# program to find the division on the basis of the grade
# read the marks from the keyboard
# keep on asking untill the user press the key y

#flag to check to continue whether to continue the programe or terminate
cont = True

# continue till user press y for yes
while cont:
	marks = int(input("enter the marks obtained. "))
	if(marks <= 100 and marks >=80):
		print("distinction")
	elif(marks<80 and marks >=60):
		print("First division")
	elif(marks<60 and marks >=45):
		print("Second division")
	elif(marks < 45 and marks >= 32):
		print("Third division")
	else:
		print("You are failed")

	repeat = input("Do you want to continue (y/n)?: ")
	cont = (repeat == 'y') # if user press y it will return true




