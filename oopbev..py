class Diak:
    def __init__(self,_nev,_ota):
        self.nev=_nev
        self.oktazon=_ota
    def __init_(self,_nev):
        self.nev=_nev
        self.oktazon=''
    def getNev(self):
        return self.nev
    def set0ta(self,_ota):
        self.oktazon=_ota
    def kiir(self):
        print("A nevem",self.nev)
        print('Oktattási azonosítom',self.oktazon)    

GZ = Diak()
BL = Diak('Kis Béla','998953454')
MT = Diak('Cserepes Márta','568943215')
GZ.nev="Tóth Géza"
GZ.oktazon='2115215551412'
print(GZ.nev)
MCS = Diak('Marcell Csík','1233456785')


GZ = Diak("Tóth Géza","123456789")
print(GZ.getNev())
GZ.kiir()
GZ.set0ta('123456789')
GZ.kiir()
BL.kiir()
MT.kiir()
MCS.kiir()