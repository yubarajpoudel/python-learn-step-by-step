''''

Simple quiz app developed by the python trainee group from the broadway

'''
######################################################
###############	Simple quiz app ######################
########## @Author: Yubaraj Poudel ###################
######################################################

'''
 1. first read the json file for question and answer
 2. all the question and answer are stored in the json format
'''
'''
	for 50 50 options
	1 right answer compulsary
	among 3 others 1 option in random 
	
	sollution
	1. we have four option
	2. first take the right answer out of four option
	3. delete that right option from the list
	4. out of 3 wrong answer take one option by generating random index ranging from 0 to 2
'''
import json
import os
import time
import random
optionMap = {'a': "a1",
			 'b': "a2",
			 'c': "a3",
			 'd': "a4"
			 }

def fiftyFifty(question_ansDict):
	keysList = list(question_ansDict.keys())
	fiftyFiftyDict = {'q':question_ansDict['q'],
					  'ca':question_ansDict['ca'],
					  }
	correctAnswerKey = optionMap[question_ansDict['ca']]
	fiftyFiftyDict[correctAnswerKey] = question_ansDict[correctAnswerKey]
	keysList.pop(keysList.index('q'))
	keysList.pop(keysList.index('ca'))
	keysList.pop(keysList.index(correctAnswerKey))				  
	while len(keysList) > 1:		
		randomIndex = random.randint(0,len(keysList)-1)			
		keysList.pop(randomIndex)
	else:
		fiftyFiftyDict[keysList[0]] = question_ansDict[keysList[0]]	
	return fiftyFiftyDict

def showOptionAnswer(question_dict, isFiftyFifty):
	print("\n\n\n{questionNo} {question}".format(questionNo = i+1, question=question_dict['q']))
	keyMap = {'a1':'a','a2':'b','a3':'c','a4':'d'}
	optionBuilder = ""
	for key, value in question_dict.items():
		if key == 'ca' or key == 'q':
			continue	
		optionBuilder+= keyMap[key] + "/"	
		print("{optionNo} ) {option}".format(optionNo=key, option=value))
	if isFiftyFifty:
		answer = input("\n Enter the option ({}) ".format(optionBuilder))
	else:
		answer = input("\n Enter the option (a/b/c/d) or h for helpline: ")
	return answer

with open("qa.json", "r") as qa:
	questionSet = qa.read()
	# json saved in the file is jsonArray hence loads() this function converts it into list
	questionsList = json.loads(questionSet)
	rightAnswer = 0
	for i in range(len(questionsList)):
		question_dict = questionsList[i]
		answer = showOptionAnswer(question_dict, False)		
		if answer == 'h':
			os.system("clear")
			question_dict = fiftyFifty(question_dict)
			answer = showOptionAnswer(question_dict, True)
		if question_dict['ca'] == answer:
			print("You predicted right answer")
			rightAnswer +=1
		else:
			print("\nYour answer is wrong")
			print("\nCorrect answer is {correctAnswer}".format(correctAnswer=question_dict['ca'])) 	
		time.sleep(1)		
		os.system("clear")

	else:
		print("\n Game Over")
		print("You made {} right. Your score is {} ".format(rightAnswer, str(rightAnswer*10)))


