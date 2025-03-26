# Írjuk ki 5ször hogy "hello word"
#for cv in range(kezdő,zároérték-1,léptetés):
# művelet
for _ in range(10):
    print ("HELLO WORD")
for i in range(1,11):
    print (i,end='\t')

print(" ")
for i in range(50,5,-5):
    print (i,end='\t')
    
gyümőlcsők=('alma','körte','narancs','dio','tom','Marci')

for gyümi in gyümőlcsők:
    print(gyümi,end='\t')


#előltesztelő ciklus
#while feltétel
# művelet
#kérjunk be 50nél nagyobb számot!
print(" ")
szam= int(input("kérek egy 50nél nagyobb számot"))
while szam<=50 or szam>100:
    print("hibás számit adtál meg te buzi!")
    szam= int(input("kérek egy 50nél nagyobb számot"))
print("ugyes vagy !!! a szám a ",szam)
# random genrátor
import random
for_ in range (10):
    print(random.random()) #0-1 között
    print(random.randint())
