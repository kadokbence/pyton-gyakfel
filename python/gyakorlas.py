#készitsen programot, amely celsius értéket vált át Farentheité
mertek = input("Mértékegység:(C/F): ").upper()
while mertek !="C" and mertek !="F":
    print("nem megfelő mértékegység")
    mertek = input("Mértékegység:(C/F): ").upper()
fok =int(input("Mennyi a kiinduló egység: "))
#Far = (C*1,8)+32
#C = (Far-32)/1,8
if mertek=='C':
    far = (fok*1.8)+32
    print(f"{fok} C° az átváltva {far}Farentheité lesz")
elif mertek=='F':
   c = (fok-32)/1.8
   print(f"{fok}Farentheit az átváltva {c}C° lesz ")
else:
    print("nem megfeleő")


#Generáljunk egy -100 és 100 köti számot és határozza meg hogy őőő  pozitiv vagy 0-e?
    
import random
szam = random.randint(-100,100)
if szam > 2:
    print("ez a szám pozitiv")
print(f"{szam//10} tízesek")
