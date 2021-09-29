count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            for h in range(10):
                                sum1 = a+b+c+d
                                sum2 = e+f+g+h
                                if(sum2):
                                    if(sum1 % sum2 == 0):
                                        count += 1
                                        print(f"{a}{b}{c}{d}{e}{f}{g}{h}")
print(f"Кол-во выигрышных билетов: {count}")

