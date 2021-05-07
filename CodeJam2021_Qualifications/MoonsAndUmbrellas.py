def readTestcase():
    line = input()
    numberOfCases = int(line.strip())
    for caseNumber in range(numberOfCases):
        line = input()
        x, y, s = line.strip().split()
        yield caseNumber+1, (int(x),int(y),s)

def subproblem(s,x,y,i,j):
    isLead = i<=0
    isLast = j>=len(s)
    n = j-i
    if isLead and isLast:
        #anything is fine, given that same answer is used
        optimalSegmentString = 'C'*n
    elif isLead:
        #use following symbol
        optimalSegmentString = s[j]*n
    else:
        #use leading symbol
        optimalSegmentString = s[i-1]*n
    return optimalSegmentString

def problem(caseInput):
    x,y,s = caseInput
    i = 0
    outString = []
    while i < len(s):
        if s[i]=='?':
            j = i+1
            while j < len(s):
                if s[j]=='?':
                    j = j+1
                else:
                    break
            n = j-i
            ss = subproblem(s,x,y,i,j)
            outString.append(str(ss))
            i = j
        else:
            outString.append(s[i])
            i = i + 1
    sss = ''.join(outString)
    return calculateCost(sss,x,y)

def calculateCost(ss,x,y):
    cost = 0
    for i in range(1,len(ss)):
        if ss[i-1] == 'C' and ss[i] == 'J':
            cost = cost + x
        if ss[i-1] == 'J' and ss[i] == 'C':
            cost = cost + y
    return cost

def main():
    testcases = readTestcase()
    for caseNumber, caseInput in testcases:
        output = problem(caseInput)
        print(f"Case #{caseNumber}: {output}")

if __name__ == '__main__':
    main()
    