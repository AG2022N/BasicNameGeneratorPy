from os import system, name
import random

def clear():
	if name == 'nt':
		_ = system('cls')
	#else:
	#	_ = system('clear')
		
while True:
	Counter = 0
	print("Type 1 to generate male names")
	print("Type 2 to generate female names")
	print("Type 3 to exit")
	UserChoice = int((input)("Choose: "))
	
	clear()
	if UserChoice == 3:
		quit()

	if UserChoice == 1:
		firstNamePath = ("namesMale.txt")
		outputPath = ("outputMale.txt")
	elif UserChoice == 2:
		firstNamePath = ("namesFemale.txt")
		outputPath = ("outputFemale.txt")
	
	maxGen = int(input("Type the number of names to generate: "))
	while Counter != maxGen:
		firstName = random.choice(open(firstNamePath, "r").readlines()).replace("\n", "")
		lastName = random.choice(open("namesLast.txt", "r").readlines()).replace("\n", "")
		name = str(firstName) + " " + str(lastName)
		f = open(outputPath, "a")
		f.write(name + "\n")
		f.close()
		print(name)
		Counter = Counter+1
	input("###Finished###")
	clear()
