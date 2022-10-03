#talkbox voor ons evenamenten bureau

print("Welkom bij ons evenamentenbureau.")
name = input("Wat is je naam?\n")
print("Hallo " + name + ", " + "dankjewel voor je komst.")
print()
asortiment = "gitaar \n" + "gamen \n" + "progameren \n" + "fitnissen \n" + "auto spotten \n" + "wandelen \n"
print("Ons aanbod aan workshops:-")
print(asortiment)
workshop = input("Kies je workshop: ")

print("Een " + "workshop" , workshop  , "is 10EUR pp")
order = "voor hoeveel personen wilt u de workshop " + workshop + "?: "
print(order)
aantal_personen = input()
aantal_personen = int(aantal_personen)

totaal = 10*aantal_personen

datum = input("Wanneer wilt u dat deze workshop plaats vind? \n")
tijd = input("Hoelaat wilt u dat deze workshop plaats vind? \n")
plaats = input("Waar wilt u waar deze workshop zig afspeeld \n")

while workshop not in asortiment:
  print("Deze workshop is niet beschikbaar")
  workshop = input("Kies workshop: ")
  
print("Uw bestelling is dan" , totaal , "EUR")

bevesteging = input("Wilt u door gaan met uw bestelling? \n" + "ja of nee \n")
if bevesteging == "nee" :
  print("Well fuck you then!")
else:
  print("Hallo" , name , "we hebben uw bestelling van" , aantal_personen ,
   "personen voor de workschop" , workshop , "voor", datum , "om" , tijd , "ontvangen!")

