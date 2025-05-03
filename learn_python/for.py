listOfNames = ["angel","luiz","tutu","leticia","natalia","analy","karine","juliana","elepepeparaco","machado","jhesua"]

for k in listOfNames:
    if k == listOfNames[-1]:
        print(k, len(k), "\n")
    else:
        print(k, len(k), end=", ")
        
    

for k in range(0, 15, 5):
        print(str(k))

print()
#coleccion enumerada
colec = {}

for k in range(len(listOfNames)):
    colec[listOfNames[k]] = k+1

print(colec)