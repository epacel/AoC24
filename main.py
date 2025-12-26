
list1 = []
list2 = []
listDiff = []
def sortInputToLists(file):
    with open(file) as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(' ')]
            list1.append(int(inner_list[0]))
            list2.append(int(inner_list[-1]))
    list1.sort()
    list2.sort()

def totalDiffOf2Lists(listx, listy):
    for i in range(len(listx)):
        listDiff.append(abs(listy[i] - listx[i]))

    totalDist = 0
    for d in listDiff:
        totalDist += d
    return totalDist


def getListsSimilarityScore(listx, listy):
    simScore = 0
    for i in listx:
        numi = listy.count(i)
        simScore += i * numi
    return simScore

def totalSafeReports(file):
    totalSafe = []
    with open(file) as f:
        for line in f:
            safe = True
            inner_list = [elt.strip() for elt in line.split(' ')]
            level = int(inner_list[0])
            safeValues = [1,2,3]

            for i in range(len(inner_list)-1):
                dif = level - int(inner_list[i+1])
                if dif in safeValues:
                    level = int(inner_list[i+1])
                else:
                    safe = False

            totalSafe.append(safe)

    print(totalSafe.count(True))


totalSafeReports("input_day2.txt")
# sortInputToLists("input_day1.txt")
# print(totalDiffOf2Lists(list1, list2))
# print(getListsSimilarityScore(list1, list2))


