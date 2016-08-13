#Challenge 255 Easy
#Light Switches - track the state of light switches for given ranges of switching.

f = open('switchdata.txt','r')
data = f.read().splitlines()

#Create initial state
lightArray = [0]*int(data[0])

#Strip first line
data = data[1:]

#loop through each scenario from input
for line in data:
	line = line.split()

	#Loop through the ranges in the array and perform the switch.
	for i in range(int(line[0]), int(line[1])+1):
		if lightArray[i] == 0:
			lightArray[i] = 1
		else:
			lightArray[i] = 0

print(lightArray)