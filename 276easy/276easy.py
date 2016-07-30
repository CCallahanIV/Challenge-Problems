# Print a rectangle with three inputs: a word (string), a width, and a height.

def printRectangle(word, width, height):
	lenWord = len(word)
	output = ""

	#Calculate character length and height of rectangle based on length of given string (word)
	rectWidth = lenWord*width - (width-1)
	rectHeight = lenWord*height - (height-1)

	#create empty rectangle of correct dimensions to populate
	rectangle = [[" "]*rectWidth for i in range(rectHeight)]

	for x in range(width):
		for y in range(height):

			if (x+y)%2 == 0:
				lword = word[::-1]
			else:
				lword = word

		for i in range(lenWord):
			rectangle[x+i][0] = lword[i] #Top
			rectangle[0][y+i] = lword[i] #Left
			rectangle[x+i][y*(lenWord-1)] = lword[lenWord - 1 - i] #Bottom
			rectangle[x*(lenWord)-1][y+i] = lword[lenWord - 1 - i]#Right

	print("\n".join([" ".join(line) for line in rectangle]) + "\n")

printRectangle('rekt', 2, 1)