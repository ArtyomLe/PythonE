# =============================================

s = "Молоко"
count = 0

for i in range(len(s)):
    if(s[i] == "о"):
        count += 1
print(f"Букв \"о\" в слове \"{s}\" = {count}")
# Букв "о" в слове "Молоко" = 3
# =============================================

strIn = "Малоко"
strOut = ""

print(f"До: {strIn}")

for i in range(len(strIn)):
    if(i == 1):
        strOut += "о"
    else:                   # Без этой строчки на выводе после получим только букву "о"
        strOut += strIn[i]  # Каждый раз когда индекс строки не равен 1 добавляется текущий элемент из strIn
strIn = strOut
print(f"После: {strIn}")
# До: Малоко
# После: Молоко
# ===============================================

messageIn = "АП"
messageOut = ""

if(messageIn[0] == "А"):
    messageOut += messageIn[1]
print(messageOut)

print("\n")

# ================================================
s = "ЙЙЙАПАРАИАВАЕФЫВФЫВАТ"
p1 = 0

while(p1 < len(s)):
    if (s[p1] == "А"):
        count += 1
        print(f"{s[p1 + 1]}", end="")
        p1 += 2
    else:
        p1 += 1
