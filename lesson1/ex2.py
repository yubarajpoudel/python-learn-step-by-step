'''
this program will take the two value height and the weight from the keyboard
display the bmi value in the monitor
'''

# take the height and weight from the keyboard
height = int(input("Enter the height in feet : \t"))
weight = int(input("Enter the weight in the kilogram : \t"))
bmi = height/weight**2

print("Your bmi value is {}".format(str(bmi)))
