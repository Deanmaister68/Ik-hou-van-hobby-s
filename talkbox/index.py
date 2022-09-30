
print("Welkom bij ons evenamentenbureau.")
name = input("Wat is je naam? ")
print("Hallo " + name + "," + "dankjewel voor je komst.")
print()
asortiment = "workshop gitaar \n" + "workshop gamen \n" + "workshop coderen \n"
print("Ons aanbod aan workshops:-")
print(asortiment)
workshop = input("Kies je workshop: ")
print("Een" , workshop  , "is 10EUR pp")
order = "voor hoeveel personen wilt u de " + workshop + "?: "
print(order)
aantal_personen = input()
aantal_personen = int(aantal_personen)

totaal = 10*aantal_personen


while workshop not in asortiment:
  print("Deze workshop is niet beschikbaar")
  workshop = input("Kies workshop: ")
  
print("Uw bestelling van" , totaal , "EUR")
print("Hallo" , name , "we hebben uw bestelling van" , aantal_personen , "personen voor" , workshop , "voor u klaar!")