'''
prime number calculation between 1 and 100
'''

for i in range(3, 100):
	for j in range (2, i):
		if(i % j == 0):
			break
		
	if(i == j+1):
		print("%s is prime number"%(i))	