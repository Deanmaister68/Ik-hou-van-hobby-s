
print("Welkom bij ons evenamentenbureau.")
name = input("Wat is je naam? ")
print("Hallo " + name + "," + "dankjewel voor je komst.")
print()
menu = "Gitaar \n" + "gamen \n" + "coderen \n"
print("Ons aanbod aan workshops:-")
print(menu)
customer_food = input("Kies je workshop.: ")
print("Een" , customer_food  , "is of 10,50EUR")
order = "voor hoeveel " + customer_food + " personen wilt u deze workshop: "
print(order)



while customer_food not in menu:
  print("This food is not available")
  customer_food = input("Enter your food: ")
  
print("Your order is of" , total , "$")
print("Hey" , name , "we'll have your order of" , number_of_coffee , customer_food , "ready for you!!")