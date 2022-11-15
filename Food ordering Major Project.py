#The main motto of this code is to  make a basic interface of a random  " Pseudo-desicion-making-programme-in-a-restraunt".
print('Hello user, What do you want to eat today ?')
print('1- order starters, 2- order Main course, 3- Order deserts, 4- try the mouth watering flavours of our latest sodas')#the main course descision
d1=int(input(" Mind putting in your number here? : "))
if d1==1:
  print("That's what i'd do first too! Please select the item number from this starters list!!" )
  l1=["Taco bells special tacos", "mcdonalds hot sauce fries, KFC starter kit",  "Dominos paratha pizza starter kit"] # main course, option 1 has 4 options
  print("1.", l1[0])
  print("2.", l1[1])
  print("3.", l1[2])
  print(" Please select your order number from the above options, press '4' to go back to main menu")
  d11=int(input(" Order Number: "))
  if d11==1:
    print(" Please select the type of tacos from our various options: ")
    print("1. Mexican tomato ")
    print("2. Indian cheese burst")
    print("3. To go back ")
    d111=int(input(" Please select your type of taco : "))
    if d111==1 or d111==2:
      print(" Your order has been taken. Please collect them near you nearest offline store, order Number: XXXXYYYYZZZZ. Order Total= xyz$ ")
    elif d111==3:
       l1=["Taco bells special tacos", "mcdonalds hot sauce fries, KFC starter kit",  "Dominos paratha pizza starter kit"] # main course, option 1 has 4 options
  print("1.", l1[0])
  print("2.", l1[1])
  print("3.", l1[2])
  print(" Please select your order number from the above options, press '4' to go back to main menu")
  d1112=int(input(" Order Number: "))
  if d1112==1 or d1112==2:
        print(" Your order has been taken. Please collect them near you nearest offline store, order Number: XXXXYYYYZZZZ. Order Total= xyz$ ")
  elif d1112==3:
          print("Too many cancellations, Please restart you order")
  if d1==2:
    print("Please select the type of  hot sauce fries you want ")
    print("1. Veggie roast ")
    print("2. Paneer shashlik ")
    print("3. Chicken kebab hot sauce fries ")
    print("4. To Go back ")
    d112=int(input(" Which sauce fries do you want to savour today? : "))
    if d122==1 or  d122==2 or d122==3:
      print(" Your order has been taken. Please collect them near you nearest offline store, order Number: XXXXYYYYZZZZ. Order Total= xyz$ ")
    elif d122==4:
        print("Please select the type of  hot sauce fries you want ")
    print("1. Veggie roast ")
    print("2. Paneer shashlik ")
    print("3. Chicken kebab hot sauce fries ")
    print("4. To Go back ")
    d1121=int(input(" Which sauce fries do you want to savour today? : "))
    if d1221==1 or  d1221==2 or d1221==3:
      print(" Your order has been taken. Please collect them near you nearest offline store, order Number: XXXXYYYYZZZZ. Order Total= xyz$ ")
    elif d1221==4:
      print("Too many cancellations, Please restart you order")

    

      

  
      
    
    
  




