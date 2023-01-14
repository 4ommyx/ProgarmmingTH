sc1 = int(input(""))
sc2 = int(input(""))
sc3 = int(input(""))

if (sc1>=0 and sc1<=30) and (sc2>=0 and sc2<=30) and (sc3>=0 and sc3<=40) :

    total = sc1+sc2+sc3
else:
    pass

if total >=80 and total <=100:
    print("A")
elif total >=75 and total <=79:
    print("B+")
elif total >=70 and total <=74:
    print("B")
elif total >=65 and total <=69:
    print("C+")
elif total >=60 and total <=64:
    print("C")
elif total >=55 and total <=59:
    print("D+")
elif total >=50 and total <=54:
    print("D")
else:
    print("F")
    