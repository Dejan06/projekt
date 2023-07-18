class Meni:
    def __init__(self, ime,cijena):
        self.ime=ime
        self.cijena=cijena
    def info(self):
        return self.ime  + str(self.cijena) + "kuna"  
    def ukupna_cijena(self, count):
        ukupno=self.cijena*count 
        if count >=3:
            ukupno*=0.9
        return round(ukupno)
class Hrana(Meni):
    def __init__(self, ime, cijena, broj_kalorija):
        super().__init__(ime,cijena)
        self.broj_kalorija=broj_kalorija
    def info(self):
        return self.ime  + str(self.cijena)+  "kuna"+ str(self.broj_kalorija) + "kcal"
    def info_kalorija(self):
        print("kcal" + str(self.broj_kalorija))
class Piće(Meni):
    def __init__(self, ime, cijena, količina):
        super().__init__(ime,cijena)
        self.količina=količina
    def info(self):
        return self.ime  + str(self.cijena)+":kuna"+ str(self.količina) + "mL"
    
hrana1=Hrana("Pizza", 5, 550)
hrana2=Hrana("Burek", 3, 330)
hrana3=Hrana("Čokoladna torta", 6, 660)
hrane=[hrana1,hrana2,hrana3]

piće1=Piće("Kava", 2, 180)
piće2=Piće("Pan", 4, 500)
piće3=Piće("Sok od naranče", 3, 2000)
pića=[piće1,piće2,piće3]     
print("Hrana")
index=0
for hrana in hrane:
    print(str(index)+":" + hrana.info())
    index +=1
    

print("Piće")

index=0
for piće in pića:
    print(str(index)+"," + piće.info())
    index +=1

print("..............................")
narudžba_hrane=int(input("Unesite broj hrane:"))
odbrana_hrana=hrane[narudžba_hrane]

narudžba_pića=int(input("Unesite broj pića:"))
odbrano_piće=pića[narudžba_pića]
count=int(input("Koliko želite naručiti?"))
rezultat=odbrana_hrana.ukupna_cijena(count)+odbrano_piće.ukupna_cijena(count)
print("Platit ćete " + str(rezultat) + " kuna")