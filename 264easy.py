challengeInput ='''    sum = i + sum;
  {
  }
  int sum = 0
  for (int i = 0; i <= 100; ++i)
  std::cout << sum;
  return 0;
{
}
#include <iostream>
int main()'''

def codeSort(inputString):

	outList = []
	inList = inputString.splitlines()

	for line in inList:
		if '#include' in line:
			outList.insert(0, line)



print(codeSort(challengeInput))	