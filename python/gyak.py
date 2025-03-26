#Generáljunk egy -100 és 100 köti számot és határozza meg hogy őőő  pozitiv vagy 0-e?
    
import random
szam = random.randint(-100,100)
if szam > 2:
    print("ez a szám pozitiv")
elif szam == 0:
    print("a szám 0")
else:
    print()
print(f"{szam//10} tízesek")
