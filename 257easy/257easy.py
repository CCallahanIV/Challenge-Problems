import re

'''Reddit Daily Challenge 257 easy
In which years were the most presidents alive?
Input: presidents.txt'''

#Open text file and read contents into list of lines without the first line
f = open('presidents.txt','r')
presData = f.read().splitlines()[1:]

#Initialize empty string and dictionary
yearsAlive=[]
presDict={}

#Pull out years of life for each president
for line in presData:
	yearsAlive.append(re.findall('\d{4}', line))

#Iterate through each year pair and update dictionary for each president
for years in yearsAlive:
	if len(years)==1:
		for i in range(int(years[0]), 2017):
			if i not in presDict:
				presDict[i]=0

			presDict[i]+=1

	else:
		for i in range(int(years[0]), int(years[1])):
			if i not in presDict:
				presDict[i]=0

			presDict[i]+=1

#Find max value within dictionary
maxAlive = max(presDict.values())
print(maxAlive)

#Print all years for which the maximum number of presidents are alive
for k in presDict:
	if presDict[k]==maxAlive:
		print(k)