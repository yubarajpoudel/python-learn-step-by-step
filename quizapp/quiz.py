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
import json
import os
import time
#import pyttsx
with open("qa.json", "r") as qa:
	questionSet = qa.read()
	# json saved in the file is jsonArray hence loads() this function converts it into list
	questionsList = json.loads(questionSet)
	rightAnswer = 0
	#engine = pyttsx.init()
	for i in range(len(questionsList)):
		question_dict = questionsList[i]
		print("\n\n\n{questionNo} {question}".format(questionNo = i+1, question=question_dict['q']))
		#engine.say("\n\n\n{questionNo} {question}".format(questionNo = i+1, question=question_dict['q']))
		#engine.runAndWait()
		print("a){optionA}\nb){optionB}\nc){optionC}\nd){optionD}".format(optionA = question_dict['a1'], optionB=question_dict['a2'], optionC=question_dict['a3'], optionD=question_dict['a4']))
		answer = input("\n Enter the option (a/b/c/d) : ")
		if question_dict['ca'] == answer:
			print("You predicted right answer")
			rightAnswer +=1
		else:
			print("\nYour answer is wrong")
			print("\nCorrect answer is {correctAnswer}".format(correctAnswer=question_dict['ca'])) 	
		time.sleep(5)		
		os.system("clear")

	else:
		print("\n Game Over")
		print("You made {} right. Your score is {} ".format(rightAnswer, str(rightAnswer*10)))


