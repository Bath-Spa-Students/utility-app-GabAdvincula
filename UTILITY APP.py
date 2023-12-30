# Printing ASCII art for the Sushi Bar                                                             
print("""
 ______  __    __  ______  __    __ ______        _______   ______  _______  
 /      \|  \  |  \/      \|  \  |  |      \      |       \ /      \|       \ 
|  $$$$$$| $$  | $|  $$$$$$| $$  | $$\$$$$$$      | $$$$$$$|  $$$$$$| $$$$$$$\
| $$___\$| $$  | $| $$___\$| $$__| $$ | $$        | $$__/ $| $$__| $| $$__| $$
 \$$    \| $$  | $$\$$    \| $$    $$ | $$        | $$    $| $$    $| $$    $$
 _\$$$$$$| $$  | $$_\$$$$$$| $$$$$$$$ | $$        | $$$$$$$| $$$$$$$| $$$$$$$\
|  \__| $| $$__/ $|  \__| $| $$  | $$_| $$_       | $$__/ $| $$  | $| $$  | $$
 \$$    $$\$$    $$\$$    $| $$  | $|   $$ \      | $$    $| $$  | $| $$  | $$
  \$$$$$$  \$$$$$$  \$$$$$$ \$$   \$$\$$$$$$       \$$$$$$$ \$$   \$$\$$   \$$
   """)                                                                           
                                                                              
                                                                              
                                                                    

    

    
                                                                                          

print(""" 
____________________________________________
|############################################|
|#|                           |##############|
|#|  =====  ..--''`  |~~``|   |##|````````|##|
|#|  |   |  \     |  :    |   |##| Exact  |##|
|#|  |___|   /___ |  | ___|   |##| Change |##|
|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|
|#|  \__//   \__//    \__//   |##|________|##|
|#|===========================|##############|
|#|```````````````````````````|##############|
|#| =.._      +++     //////  |##############|
|#| \/  \     | |     \    \  |#|`````````|##|
|#|  \___\    |_|     /___ /  |#| _______ |##|
|#|  / __\\  /|_|\   // __\   |#| |1|2|3| |##|
|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|
|#|===========================|#| |7|8|9| |##|
|#|```````````````````````````|#| ``````` |##|
|#| ..--    ______   .--._.   |#|[=======]|##|
|#| \   \   |    |   |    |   |#|  _   _  |##|
|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|
|#|  / __\  |/ __\   // __\   |#| |||  `  |##|
|#|  \__//   \__//  /_\__//   |#|  ~      |##|
|#|===========================|#|_________|##|
|#|```````````````````````````|##############|
|############################################|
|#|||||||||||||||||||||||||||||####```````###|
|#||||||||||||PUSH|||||||||||||####\|||||/###|
|############################################|
\\\\\\\\\\\\\\\\\\\\\\///////////////////////
 |________________________________|CR98|___|            
""")                                                                                  
                                                                                                     
                                                                                                                                                                                                                    
                                                                                                                                                                                                                                   
# Function to print a menu header                                                                                                                                                                                                                               
def print_menu_header(header_text):
    print("=" * 35)
    print(f"{header_text:^35}")
    print("=" * 35)

# Welcoming message
print ("""\nWelcome to my Sushi Bar Machine!!!!Explore a variety of fresh and delicious sushi options available at your fingertips!!!!\n""")

# Printing the Dish Menu
print_menu_header("MENU -  Dish")
print("       List of Dish:")
print("|Number 1 | California roll = 20.50 AED")
print("|Number 2 | Rainbow roll = 22.50 AED")
print("|Number 3 | Salmon roll = 23.AED")
print("|Number 4 | Tuna roll = 21 AED")
print("|Number 5 | Dynamite  = 24 AED")
print("|Number 6 | Prawn star = 20.75 AED")
print("|Number 7 | Cucumber maki = 22 AED")
print("|Number 8 | Shrimp tempura roll = 21 AED")
print("|Number 9 | Nigiri = 25 AED")
print("|Number 10 | Gunkan maki = 23 AED ")


# Taking user input for selecting a dish
Dish = float(input("Please select a dish. If none, press 0: "))

# Conditionals for each dish choice selected by the user
# Each block checks the selected dish, prompts for money, and calculates change
# The process continues until the user inserts enough money or cancels the order
# Similar logic is repeated for Side Dishes, Cold Beverages, and Hot Beverages

if Dish == 1:
    print("You have chosen California Roll")
    print("Cost: 20.50 AED")
    cost = 20.50

    while True:
        money_in = float(input("Insert amount here: "))
        money_out = money_in - cost

        if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
        else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
      
elif Dish  == 2:
  print("You have selected Rainbow Roll ")
  print("Cost: 22.50 AED")
  cost = 20.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of\n", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
      


elif Dish  == 3:
  print("You have selected Salmon Roll")
  print("Cost: 23.50 AED")
  cost = 23.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 4:
  print("You have selected Tuna Roll")
  print("Cost: 21 AED")
  cost = 21

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 5:
  print("You have selected Dynamite")
  print("Cost: 24 AED")
  cost = 24

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            
elif Dish  == 6:
  print("You have selected Prawn star")
  print("Cost: 20.75 AED")
  cost = 20.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 7:
  print("You have selected Cucumber maki")
  print("Cost: 22 AED")
  cost = 22

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 8:
  print("You have selected Shrimp tempura roll")
  print("Cost: 21 AED")
  cost = 21

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 9:
  print("You have selected Nigiri")
  print("Cost: 25 AED")
  cost = 25

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 10:
  print("You have selected Gunkan maki")
  print("Cost: 23 AED")
  cost = 23

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Dish  == 0:
  print("Options for Dish has been declined.")

else:
  print("You have entered an invalid number.")

# Printing the Side Dish Menu
print_menu_header("MENU - Side Dish")
print("       List of Side Dish:")
print("|Number 11 | Miso soup = 10 AED")
print("|Number 12 | Edamame = 9 AED")
print("|Number 13 | Spinnach = 6 AED")
print("|Number 14 | Fried pickles = 7 AED")
print("|Number 15 | Tempeh  = 6 AED")
print("|Number 16 | Cold Cucumber salad = 7 AED")

Side_dish = float(input("Please select a side dish. If none, press 0: "))

if Side_dish == 11:
  print("You have selected Miso soup ")
  print("Cost: 10 AED")
  cost = 10

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            
elif Side_dish == 12:
  print("You have selected Edamame")
  print("Cost: 9 AED")
  cost = 9

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Side_dish == 13:
  print("You have selected Spinnach")
  print("Cost: 6 AED")
  cost = 6

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Side_dish == 14:
  print("You have selected Fried Pickles ")
  print("Cost: 7 AED")
  cost = 7

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Side_dish == 15:
  print("You have selected Tempeh ")
  print("Cost: 6 AED")
  cost = 6

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Side_dish == 16:
  print("You have selected Cold Cucumber Salad  ")
  print("Cost: 7 AED")
  cost = 7

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Side_dish == 0:
  print("Choosing Side Dish Had Been Skipped.")

else:
  print("You have entered an invalid number.")




# Printing the Cold Beverage Menu
print_menu_header("MENU -  Cold Beverage")
print("       List of Cold Beverages:")
print("|Number 17 | Bottled water = 2.50 AED")
print("|Number 18 | Ginger Ale = 3.50 AED")
print("|Number 19 | Ice tea = 4 AED")
print("|Number 20 | Coca cola = 3.50 AED")
print("|Number 21 | Sprite = 3.50 AED")
print("|Number 22 | Sparkling water = 4 AED")


Cold_beverage = int(input("Please select a cold beverage. If none, press 0: "))

if Cold_beverage == 17:
  print("You have selected Bottled water ")
  print("Cost: 2.50 AED")
  cost = 23

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            

elif Cold_beverage == 18:
  print("You have selected Ginger Ale")
  print("Cost: 3.50 AED")
  cost = 3.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Cold_beverage == 19:
  print("You have selected Ice Tea")
  print("Cost: 4 AED")
  cost = 4

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Cold_beverage == 20:
  print("You have selected Coca Cola ")
  print("Cost: 3.50 AED")
  cost = 3.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Cold_beverage == 21:
  print("You have selected Sprite ")
  print("Cost: 3.50 AED")
  cost = 3.50

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Cold_beverage == 22:
  print("You have selected Cold Cucumber Salad  ")
  print("Cost: 4 AED")
  cost = 4

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")

elif Cold_beverage == 0:
  print("Choosing Cold Beverage Had Been Skipped.")

else:
  print("You have entered an invalid number.")


# Printing the Hot Beverage Menu  
print_menu_header("MENU -  Hot Beverage")
print("       List of Hot Beverages:")
print("|Number 23 | Genmaicha - Brown rice tea = 13 AED")
print("|Number 24 | Sencha - Classic green tea = 13 AED")
print("|Number 25 | Kuromamecha - Black soybean tea = 14 AED")
print("|Number 26 | Matcha tea = 12 AED")
print("|Number 27 | Herbal tea = 10 AED")

Hot_beverage = int(input("Please select a hot0 beverage. If none, press 0: "))  

if Hot_beverage == 23:
  print("You have selected Genmaicha - Brown rice tea ")
  print("Cost: 13 AED")
  cost = 13

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")



elif  Hot_beverage == 24:
  print("You have selected Sencha - Classic green tea")
  print("Cost: 13 AED")
  cost = 13

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")


elif  Hot_beverage == 25:
  print("You have Kuromamecha - Black soybean tea")
  print("Cost: 14 AED")
  cost = 14

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            
elif  Hot_beverage == 26:
  print("You have selected Match tea")
  print("Cost: 12 AED")
  cost = 12

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            
elif  Hot_beverage == 27:
  print("You have selected  Herbal tea")
  print("Cost: 10 AED")
  cost = 10

  while True:
       money_in = float(input("Insert amount here: "))
       money_out = money_in - cost

       if money_in >= cost:
            print("== Processing ==")
            print("== Please wait ==")
            print("\nItem received and change of", money_out, "AED")
            break
       else:
            print("The amount you have input is insufficient.")
            print("Please insert a minimum of", cost, "AED")
            
            
elif Hot_beverage == 0:
  print("Choosing Hot beverage Had Been Skipped.")

else:
  print("You have entered an invalid number.")
  

print("=" * 35)
print("\nThank you for purchasing! Have a nice day!")
print("\nThank you for choosing us for your sushi cravings!")


# Printing a decorative UAE One Dirham note
print("""
___________________________________
|#######====================#######|
|#(1)*UNITED ARAB EMIRATES*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DIRHAM===========##|
------------------------------------
     """)
     