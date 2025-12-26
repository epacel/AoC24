import numpy as np
import re
file = "input_day4.txt"
allrows = []

def appendStrToList(l, s):
    x = s.strip()
    y = s[::-1].strip()
    l.append(x)
    l.append(y)

with open(file) as f:
    x = 0
    y = 0

    ws = []
    revws = []

    for line in f: #get all the horizontal strings and create 2d array of wordsearch
        x = len(line)
        y += 1
        ws.append(list(line.strip()))
        revws.append(list(line[::-1].strip()))
        appendStrToList(allrows, line)
    # print(f"{x}, {y}")
    # print(ws)

    for i in range(y): #get all the verticle strings
        line = ""
        for j in range(x):
            line += ws[j][i]
        appendStrToList(allrows, line)

    wsarr = np.array(ws)
    for i in range(1-x, x): #get all the diagonal strings
        line = ""

        d = wsarr.diagonal(i).tolist()
        line.join(str(e) for e in d)

        for e in d:
            line += e
        appendStrToList(allrows, line)

    revwsarr = np.array(revws)
    for i in range(1 - x, x):  # get all the diagonal strings
        line = ""

        d = revwsarr.diagonal(i).tolist()
        line.join(str(e) for e in d)

        for e in d:
            line += e
        appendStrToList(allrows, line)

count = 0
for r in allrows:
    count += len([m.start() for m in re.finditer('(?=XMAS)', r)])

# print(allrows)
print(count)

