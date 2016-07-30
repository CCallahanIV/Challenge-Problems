input = '''12
····
VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT'''

lines = input.splitlines()
indent = lines[1]
numLines = int(lines[0])
output = ['']*numLines  #Initialize output array


for i in range(numLines):
	line = lines[i+2].strip(r'·» \t\s')		#Strip unwanted characters
	output[i] = output[i] + line 			#Add text to output array

	#Check for Opening indentation terms, apply indentation to every line below that line
	if line.startswith('FOR') or line.startswith('IF'):
		for j in range(numLines-i-1):
			output[i+j+1] = indent + output[i+j+1]

	#Check for Closing terms, substract indentation from every line below and including that line
	if line.startswith('NEXT') or line.startswith('ENDIF'):
		for j in range(numLines-i):
			output[i+j] = output[i+j][4:]

#Print output as string formatted with endlines.
print("\n".join(output))




	