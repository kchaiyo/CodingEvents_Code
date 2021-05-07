import sys

def initialBreak(l):
    answerSet = {}
    for i in range(len(l)-2):
        ask = [l[i], l[i+1], l[i+2]]
        print('{} {} {}'.format(*ask))
        answer = int(input())
        if answer == -1:
            sys.exit(1)
        ask.remove(answer)
        if answer not in answerSet.keys():
            answerSet[answer] = []
        answerSet[answer].append(set(ask))
    return answerSet

def bipartiteSidePair(sidePairList):
    #if len(sidePairList)==0:   #not gonna happened
    sideA = [sidePairList[0][0]]
    sideB = [sidePairList[0][1]]
    for i in range(len(sidePairList)-1):
        common = sidePairList[i]&sidePairList[i+1]
        if len(common)!=1:
            sys.exit(2) #more than one common element found, invalid assumption
        if common[0] in sideA:
            sideB.append((sidePairList[i+1]-common)[0])
        elif common[0] in sideB:
            sideA.append((sidePairList[i+1]-common)[0])
        else:
            sys.exit(3) #common element not found in each side
    return sideA, sideB

def makeOrderedList(anchor,sideA,sideB):
    if len(sideA)==1:
        listSideA = [sideA[0]]
    else:
        listSideA = list(reversed(makeOrderedList_oneside(anchor,sideA)))
    if len(sideB)==1:
        listSideB = [sideB[0]]
    else:
        listSideB = makeOrderedList_oneside(anchor,sideB)
    return listSideA + [anchor] + listSideB

def makeOrderedList_oneside(anchor, blob):
    print('{} {} {}'.format(anchor, blob[0], blob[1]))
    answer = int(input())
    if answer == -1:
        sys.exit(1)
    if answer == blob[0]:
        notAnswer = blob[1]
    else if answer == blob[1]:
        notAnswer = blob[0]
    orderedList = [anchor, answer, notAnswer]
    #insert remaining elements
    for i in range(2,len(blob)):
        for j in range(len(orderedList)-1):
            print('{} {} {}'.format(blob[i],orderedList[j],orderedList[j+1]))
            answer = int(input())
            if answer == -1:
                sys.exit(1)
            if answer == blob[i]:
                orderedList.insert(index=j+1,blob[i])
                break
    return orderedList[1:]  #remove anchor from this list

def joinOrderedList(listA, listB):
    #find common elements
    ce_i = []
    ce_j = []
    ce_v = []
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] == listB[j]:
                ce_i.append(i)
                ce_j.append(j)
                ce_v.append(listA[i])
                break
    if len(ce_i) == 0:
        sys.exit(3) # distinct list, can not join
    
    if len(ce_j)>1 and ce_j[0]>ce_j[1]:
        #list B opposit side of list A, reverse the list B
        return joinOrderedList(listA, list(reversed(listB)))
    #start new ordered list by joining sublists before first common element
    ol = joinOrderedList_rightAnchor(
        ce_v[0],
        listA[_:ce_i[0]],
        listB[_:ce_j[0]]
        )
    #for each pair of common elements, use left side anchor to join ordered list
    for idx in range(len(ce_i)-1):
        ol = ol + [ce_v[idx+1]] + joinOrderedList_rightAnchor(
            ce_v[idx+1],
            listA[ce_i[idx]+1:ce_i[idx+1]],
            listB[ce_i[idx]+1:ce_i[idx+1]]
            )
    #after last common element, use last common element as anchor (left-sided) and join the remaining list
    ol = ol + [ce_v[-1]] + list(reversed(joinOrderedList_rightAnchor(
        ce_v[-1],
        list(reversed(listA[ce_i[-1]+1:])),
        list(reversed(listB[ce_j[-1]+1:]))
        )))
    return ol

def joinOrderedList_edge(anchor, listA, listB):
    #assume anchor was on the left of input list
    if len(listA)==0:
        return listB
    elif len(listB)==0:
        return listA
    else:
        if len(listA) < len(listB):
            listA, listB = listB, listA
        output = [anchor, *listA]
        for i in range(len(listB)):
            if listB[i] in output:
                continue
            j = 0
            while j < len(output)-1:
            #for j in range(len(output)-1):
                print('{} {} {}'.format(listB[i],output[j],output[j+1]))
                answer = int(input())
                if answer == -1:
                    sys.exit(1)
                if answer == listB[i]:
                    break
                j = j + 1
            orderedList.insert(index=j+1,listB[i])
        return output[1:]

def joinOrderedList_rightAnchor(anchor, listA, listB):
    #using scheme from joinOrderedList_edge to implement this function
    raise NotImplementedError

if __name__ == '__main__':
    t, n, q = tuple(lambda x: int(x), input().strip().split())
    for case in range(t):
        initialList = list(range(1,n+1))
        initialList = list(map(lambda x:(x,),initialList))
        initialBreakSet = initialBreak(initialList)
        partialOrderedList = []
        for k,v in initialBreakSet:
            twoSideListA, twoSideListB = bipartiteSidePair(v)
            ol = makeOrderedList(k,twoSideListA, twoSideListB)
            partialOrderedList.append(ol)
        mainList = next(partialOrderedList)
        for subsequentList in partialOrderedList:
            mainList = joinOrderedList(mainList, subsequentList)
        #print(mainList)
        #TODO
