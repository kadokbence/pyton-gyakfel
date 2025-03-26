import math

szam = 10
print("a szám értéke:",szam, type(szam))
#print ("Kérem adja meg a nevét: ",end=' ')
neve = input("Kérem adja meg a nevét:")
print ("ŰDVÖZÖLEK kedves",neve)
szam = float (input("kérek egy számot"))
print("A megabdott szám kétszerese: ",szam*2, type(szam))
sugar=23.56
print ("kör kerulete:",2*sugar*math.pi)
print ("kör terulete:",math.pow(sugar,2)*math.pi)

#négyzet (tört) és téglalap (egész/tört) kerület és területe
#egyenéő szárú háromszög kör kerület és területe
szam = float (input("kérek egy számot:"))
print ("A megadott szám a négyzet kerülete",szam*4, type(szam))
szam = float (input("kérek egy számot:"))
print ("A megadott szám a négyzet kerülete",szam*4,math.trunc, type(szam))



szam = float (input("kérek egy számot:"))
print ("A megadott szám a négyzet kerülete",szam*szam, type(szam))
