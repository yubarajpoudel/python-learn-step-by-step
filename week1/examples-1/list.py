# list
names = ['raju','shyam']
length_names = len(names)
print("size of the names is {}".format(length_names))

# add the element in the list names
names.append("hari")
length_names = len(names)
print("size of the names after adding hari is {}".format(length_names))

print(names)

# let insert the element in the second postion of the names list
names.insert(1, "santosh")

print("after inserting the hari at second position : {} ".format(names))

santosh_at = names.index("santosh")
print("santosh is at {} ".format(santosh_at))

# print all the value of the list

for name in names:
	print(name)

for i in range(0, length_names):
	print(names[i])

# extending the list
other_names = ['jiwan', 'narayan', 'sita']
names.extend(other_names)
print("after extending the list")
print(names)

# Dictionary
student = {'name':'raju',
			'time':'2 hrs',
			'course': 'django and python',
			'fee': 5000,
			'hasVeichle': True
			}

# print the value of the dictionary with key
print(student['course'])

student_all_key = student.keys()
print(student_all_key)
student_all_value = student.values()
print(student_all_value)

# iterate in the dictionary
for key in student.keys():
	print("{} : {}".format(key, student[key]))


# change the value of the dictionary
student['course'] = 'Advanced Java'
print(student)

# lets add the key that doesnot exist in the dictionary student
student['gender'] = "male"

print("after adding gender")
print(student)

# delete the key course
del(student['course'])
# after deleting the key course
print(student) 
# convert the student to list
student = list(student)
# after converting to the list
print(student)

# check the key is exist in the dictionary or not
isCourseExists = "courses" in student
print("course exists in student  : {} ". format(isCourseExists))





