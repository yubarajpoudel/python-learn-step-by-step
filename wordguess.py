# Algortihms to solve 
'''
	1. Create the list of the question words
	2. check the entered letters againist the answers
	3. if the user entered correct answer ask the next
	4. else keep on asking the same untill the user press the right character
'''
import os
words = {
		 'AN_M_L': ['i','a'],
		 'D_NCE_': ['a','r']
		 }
	
for key in words.keys():
	print(key)
	correctCount = 2
	predictedAnswer = []
	while(correctCount > 0):
		answer = input("Guess the character : ")
		if answer in words[key] and answer not in predictedAnswer:
			print("correct answer")
			predictedAnswer.append(answer)
			correctCount -= 1			
		else:
			print("try again, you may have predicted already or might be wrong prediction")
	else:
		print("Congratulation, proceed to next question")
		input("\nPress any key to next")
		os.system('clear') 

else:
	print("Game over")




