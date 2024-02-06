j = input("voce esta em jejum s/n?")
t = input("trigliceres? ")
t = int(t) #coverter pra int
if j == 's':
    if t > 150:
        print ("Está alto !")
    else:
        print ("Está normal !")
else:
    if t > 175:
         print ("Está alto !")
    else:
        print ("Está normal !")