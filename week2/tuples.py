# tuple is moreover like the list
# list is basically used for homogenous data type
# tuple is used for hetergenous data type

a = ('test', 1, 'sample')

# for accessing the data from the tuple
for data in a:
	print(data)

# Why we use the tuple ?
#  tuples are immutable
# for constants list we use the tuple

# for declaring the tuple with single item it is bit tricky
a = ('hello',)
print(a)

# change the value in the tuple
b = (1,5,6,7,8,)
print("orginal b = {}".format(b))
# b[3] = 9
# print(b)

# this will throw the error because tuple doesnot support the assignment

c = ((3,4), 5, 7, (3,5,6,7))
print(c[3][2])

# checking the size
print(len(c))

# tupe concatenation
e = a+b
print(e)

# slice the tuple
# for eg

names = ('ram','sita','hari','laxmi','shiva', 'parbati')
# slice the names from second index value to 4th index value
print(names[2:4])
print(names[-3:])

# we can declare the tuple without bracket aswell
test = 3,4,5,6
print(type(test))


# set
test = {"hello", "set"}
print(test)
print(type(test))
test.add("hello")
print(test)

# other way of defining set
weekDay = set(["Sunday", "Monday", "Tuesday"])
print(type(weekDay))

for weekName in weekDay:
	print(weekName)














