import math

#possible conversions:
# rd, dr
# cf, fc
# ck, kc
# fk, kf

def conversions(toConvert):
	#slice input string into components, convert string to int.
	conv = toConvert[-2:]
	num = float(toConvert[:-2])
	#Declare output variables
	convNum = 0
	outUnit = ''

	if conv == 'rd':
		convNum = round(num*180/math.pi,2)
		outUnit ='d'

	elif conv == 'dr':
		convNum = round(num*math.pi/180,2)
		outUnit = 'r'

	elif conv == 'cf':
		convNum = round(num*9/5 + 32,2)
		outUnit = 'f'

	elif conv == 'fc':
		convNum = round((num-32)*5/9,2)
		outUnit = 'c'

	elif conv == 'ck':
		convNum = round(num + 273.15,2)
		outUnit = 'k'

	elif conv == 'kc':
		convNum = round(num - 273.15,2)
		outUnit = 'c'

	elif conv == 'fk':
		convNum = round((num + 459.67)*5/9,2)
		outUnit = 'k'

	elif conv == 'kf':
		convNum = round(num * 9/5 - 459.67,2)
		outUnit = 'f'

	else:
		return 'No candidate for conversion.'

	return str(convNum)+outUnit

while True:
	toConvert = input('Enter number to be converted, q to quit: ')
	if toConvert != 'q':	
		print(conversions(toConvert))
	elif toConvert == 'q':
		break
