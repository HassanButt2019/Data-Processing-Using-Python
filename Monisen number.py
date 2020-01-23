
def PrimeNumber(number):
    if number <= 1:
        return False
    for i in range(2 , number):
        if number % i == 0:
            return False
    return True



def MonisenNumber(p):
    if PrimeNumber(p) == True:
        M = 2 ** p - 1
        if PrimeNumber(M) == True:
           return True
    return False

MNumber = []
for i in range (1 , 25):
    if MonisenNumber(i) == True:
        MNumber.append(2 ** i - 1)


print(MNumber[5])

