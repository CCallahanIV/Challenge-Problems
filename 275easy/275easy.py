def elementTest(inputData):

	#convert both strings to lower case to simplify analysis
	name = inputData[0].lower()
	symbol = inputData[1].lower()

	#Perform tests as detailed in problem statement
	#Print statements were used for debugging
	if len(symbol) != 2:
		print("Failed Test 1")
		return False

	elif symbol[0] not in name or symbol[1] not in name:
		print("Failed Test 2")
		return False

	elif name.index(symbol[0]) > name.index(symbol[1]):
		print("Failed Test 3")
		return False

	elif symbol[0]==symbol[1] and name.count(symbol[0]) < 2:
		print("Failed Test 4")
		return False

	else:
		return True

input = [('Spenglerium', 'Ee'),
		 ('Zeddemorium', 'Zr'),
		 ('Venkmine', 'Kn'),
		 ('Stantzon', 'Zt'),
		 ('Melintzum','Nn'),
		 ('Tullium','Ty')]

for item in input:
	print(item[0], item[1], elementTest(item))

