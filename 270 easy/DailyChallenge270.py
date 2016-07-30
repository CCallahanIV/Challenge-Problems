

#Read text from file
f = open('input', 'r')
input = f.readlines()

oldArray = []
maxLen = 0

#Build formatted list, determine max length
for line in input:
	line = line.rstrip('\n')
	if len(line) > maxLen:
		maxLen = len(line)
	oldArray.append(line)

print(oldArray)

for i in range(maxLen):
	for line in oldArray:
		if len(line) < maxLen:
			print(line[i], end=' ')
		else:
			print(' ', end =' ')
	print('')





