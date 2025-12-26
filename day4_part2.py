import numpy as np
import re
file = "input_day4_part2.txt"
allrows = []

with open(file) as f:
    x = 0
    y = 0

    ws = []

    for line in f:
        x = len(line)
        y += 1
        ws.append(list(line.strip()))
    # print(ws)

    for i in range(y-2):
        for j in range(x-2):
            if i+2 < x or j+2 < y:
                x_tl = ws[i][j]
                x_tr = ws[i][j+2]
                x_m = ws[i+1][j+1]
                x_bl = ws[i+2][j]
                x_br = ws[i+2][j+2]

            # print(f"{i},{j+2}   {x_tl}{x_m}{x_br}")
            # print(f"{i},{j+2}   {x_bl}{x_m}{x_tr}")
            allrows.append([f"{x_tl}{x_m}{x_br}",f"{x_bl}{x_m}{x_tr}"])

count = 0
print(allrows)
for r in allrows:
    matchstr = "MAS"
    # print(r[0][::-1])
    x = False
    y = False
    if r[0] == matchstr or r[0][::-1] == matchstr:
        print(r[0])
        x = True
    if r[1] == matchstr or r[1][::-1] == matchstr:
        y = True

    if x and y:
        count += 1

    # count += len([m.start() for m in re.finditer('(?=MAS)', r)])
#
print(count)
#
#     for i in range(1-x, x): #get all the diagonal strings
#         line = ""
#
#         d = wsarr.diagonal(i).tolist()
#         line.join(str(e) for e in d)
#
#         for e in d:
#             line += e
#         appendStrToList(allrows, line)
#
#     revwsarr = np.array(revws)
#     for i in range(1 - x, x):  # get all the diagonal strings
#         line = ""
#
#         d = revwsarr.diagonal(i).tolist()
#         line.join(str(e) for e in d)
#
#         for e in d:
#             line += e
#         appendStrToList(allrows, line)
#
# count = 0
# for r in allrows:
#     count += len([m.start() for m in re.finditer('(?=XMAS)', r)])

# print(allrows)
# print(count)

