a=int(input("kérek egy számot"))
b=int(input("kérek egy másik számot"))
if a>10:
    a=a-5
if b%2==0:
    print ("páros")
else:
    print ("páratlan")
if a==b:
    print("A két szám gyenlő")
elif a>b:
    print("Nagyobb",a)
else:
    print("nagyobb",b)
jegy=int(input("hányast kaptál?? "))
match jegy:
    case '1':print("elégtelen")
    case '2':print("elégséges")
    case '3':print("közepes")
    case '4':print("jó")
    case '5':print("jeles")
    case _:print("Ilyen jegy magyar honban nem létezik")

