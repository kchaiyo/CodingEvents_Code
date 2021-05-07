import itertools
def readInput():
	with open('input.txt') as f:
		inputText = f.readlines()
	return list(map(lambda x:int(x),inputText))

def partOne(inputNumbers):
	for i,j in itertools.permutations(inputNumbers,2):
		if i+j==2020:
			print(i*j)
			break
	else:
		print('Part A: No output')

def partTwo(inputNumbers):
	for i,j,k in itertools.permutations(inputNumbers,3):
		if i+j+k==2020:
			print(i*j*k)
			break
	else:
		print('Part B: No output')

if __name__ == "__main__":
	inputNumbers = readInput()
	partOne(inputNumbers)
	partTwo(inputNumbers)