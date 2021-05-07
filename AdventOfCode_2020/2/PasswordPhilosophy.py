def readInput():
    with open('input.txt') as f:
        inputLines = f.readlines()
    return list(map(lambda x: x.strip(),inputLines))

def partOne(inputLines):
    countValid = 0
    for row in inputLines:
        amounts, key, pw = row.split(' ',3)
        amounts = amounts.split('-',2)
        amountMin = int(amounts[0])
        amountMax = int(amounts[1])
        key = key[0]
        countChar = 0
        for i in range(len(pw)):
            if pw[i]==key:
                countChar = countChar + 1
        if amountMin <= countChar <= amountMax:
            countValid = countValid + 1
    print(countValid)

def partTwo(inputLines):
    countValid = 0
    for row in inputLines:
        positions, key, pw = row.split(' ',3)
        positions = positions.split('-',2)
        positionLower = int(positions[0])
        positionUpper = int(positions[1])
        key = key[0]
        if (pw[positionLower-1]==key)!=(pw[positionUpper-1]==key):
            countValid = countValid+1
    print(countValid)

if __name__ == "__main__":
    inputLines = readInput()
    partOne(inputLines)
    partTwo(inputLines)