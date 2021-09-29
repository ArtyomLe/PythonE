sIn = ""
sOut = ""

p1 = 0
while(p1 < len(sIn)):
    if (sIn[p1] == "А" or sIn[p1] == "Б"):
        sOut += sIn[p1+1]
        p1 += 2
    else:
        p1 += 1
print(sOut)