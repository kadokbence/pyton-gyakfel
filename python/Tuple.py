tanulok = []
tanarok = ["Madarasz","Prohásztka"]
tanulok.append("Köteles")
print(tanulok)
tanulok.append("István")
print(tanulok)
tanarok.insert(1,"Krasznahorkai")
print(tanarok)
for tanar in tanarok:
    print(tanar)
tanulok.append(True)
print(tanulok)
tanulok.remove(True)
print(tanarok.index("Madarasz"))
##Kerjunk be a felhasználotol 20 számot 
#100 és 320 között(Figyeljen a helyes érték megadására!)
#az értékeket tárolja el egy sorozatba.
sorozat=[]
szam = int(input("kérek egy számot"))
for i in range(5):
    while szam <100 or szam >320:
        print("hibás érték",end='')
        szam = int(input("kérek egy számot"))
    sorozat.append(szam)
    szam = int(input(f"kérek egy a {i+1}-dik következő számot"))
print(sorozat)
# vegyuk ki a sorozatbol a legnagyobb elemet
legnagyobb= max(sorozat)
sorozat.remove(legnagyobb)
print(sorozat)
legkisseb = min(sorozat)
sorozat.remove(legkisseb)
print(sorozat)








