import re

file = "input_day3.txt"
# file = "input_day3.txt"

t = 0
with open(file) as f:
    print(f)
    txt = ""
    for line in f:
        txt += line

    ntxt = ""
    dnt = txt.split("don't()")
    ntxt += dnt[0]
    for d in dnt:
        if "do()" in d:
            dos = d.split("do()")[1:]
            print(dos)
            for x in dos:
                ntxt += x

    m = re.findall("mul\(\d{1,3},\d{1,3}\)", ntxt, re.DOTALL)
    for i in m:
        j = re.findall("\d{1,3}", i, re.DOTALL)
        k = int(j[0]) * int(j[1])
        t += k

print(t)