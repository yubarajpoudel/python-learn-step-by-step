def firstWrong():
	print("-------------")
	print("  |      |")
	print("	 |      O")
	print("  |")
	print("  |")
	print("  |")
	print("--------")


def secondWrong():
	print("-------------")
	print("  |      |")
	print("	 |      O")
	print("  |	   /|\\")
	print("  |      |")
	print("  |")
	print("--------")

def thirdWrong():
	print("-------------")
	print("  |      |")
	print("	 |      O")
	print("  |	   /|\\")
	print("  |     / \\")
	print("  |")
	print("--------")


questionAnswer = [{'q':'what is spelling of python?','a':'python'},
				  {'q':'what is spelling of python?','a':'python'},
				  {'q':'what is spelling of python?','a':'python'},
				  {'q':'what is spelling of python?','a':'python'},
				  {'q':'what is spelling of python?','a':'python'}]
mistake = 0
for qa in questionAnswer:
	if mistake == 3:
		break
	answer = input(qa['q'] + ": ")
	if answer == qa['a']:
		print("You made correct anwer")
	else:
		mistake +=1
		if mistake == 1
			firstWrong()
		elif mistake == 2:
			secondWrong()
		else:
			thirdWrong()

else:
	print("game over")