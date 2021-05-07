def readTestcase():
    line = input()
    numberOfCases = int(line.strip())
    for caseNumber in range(numberOfCases):
        line = input()
        n,c = tuple(map(lambda x: int(x),line.split()))
        yield caseNumber+1, (n,c)

def problem(n,c):
    pass


def reversort(n,l):
    #print(n,l)
    cost = 0
    for i in range(1,len(l)):
        #find position of number i, set found index to j(zero-index)
        for j in range(i-1,len(l)):
            if l[j]==i:
                break
        l_front = l[:i-1]
        l_mid = l[i-1:j+1]
        l_back = l[j+1:]
        l = l_front + list(reversed(l_mid))+l_back
        cost = cost + (j+1) - i + 1
    return cost

def main():
    testcases = readTestcase()
    for caseNumber, caseInput in testcases:
        output = problem(*caseInput)
        print(f"Case #{caseNumber}: {output}")

if __name__=='__main__':
    main()