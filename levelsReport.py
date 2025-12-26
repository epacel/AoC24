file = "input_test.txt"
def intListDiffCheck(list):
    currentInt = list[0]
    check = [1,2,3]
    for i in list[1:]:
        if not abs(currentInt - i) in check:
            return False
        else:
            currentInt = i
    return True

def cleanAList(list):
    ci = list[0]
    nlist = [list[0]]
    o = True
    for i in list[1:]:
        if ci > i: # a greater than b should be false
            if o:
                nlist.append(i)
                o = False
            else:
                pass
        else:
            nlist.append(i)
    print(nlist)
    return nlist



with open(file) as f:
    safeReport = []
    for line in f:
        innerListStr = [i for i in line.split(' ')]
        innerList = list(map(int, innerListStr))

        a = innerList == sorted(innerList)
        d = innerList == sorted(innerList, reverse=True)

        if a:
            alist = cleanAList(innerList)
            safeReport.append(intListDiffCheck(alist))
        elif d:
            safeReport.append(intListDiffCheck(innerList))
        else:
            # print("o")
            safeReport.append(False)

    print(safeReport)
    print(safeReport.count(True))