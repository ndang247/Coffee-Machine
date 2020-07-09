water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cup_of_coffee = int(input("Write how many cups of coffee you will need:\n"))

# amount of possible cup of coffee machine can make
# if the amount of cup(s) each ingredient can make are all equal
possible_cup = int((water+milk+coffee_beans)/(200+50+12))

# required amount to make N cup(s) of coffee
water_required = cup_of_coffee * 200
milk_required = cup_of_coffee * 50
coffee_beans_required = cup_of_coffee * 15

# the amount of cup(s) each ingredient can make 
water_for_coffee = int(water/200)
milk_for_coffee = int(milk/50)
coffee_beans_for_coffee = int(coffee_beans/15)

# min cup(s) of coffee the machine can make based on ingredients
min_cups_can_make = min(water_for_coffee, milk_for_coffee, coffee_beans_for_coffee)

available_cups = min_cups_can_make - cup_of_coffee

# this block will execute if one or more ingredient is less than the required
if water < water_required or milk < milk_required or coffee_beans < coffee_beans_required:
    if water_for_coffee == milk_for_coffee and water_for_coffee == coffee_beans_for_coffee and milk_for_coffee == coffee_beans_for_coffee:
        print("No, I can make only", possible_cup, "cup(s) of coffee")

    elif water_for_coffee < milk_for_coffee and water_for_coffee < coffee_beans_for_coffee:
        print("No, I can make only", min_cups_can_make, "cup(s) of coffee")

    elif milk_for_coffee < water_for_coffee and milk_for_coffee < coffee_beans_for_coffee:
        print("No, I can make only", min_cups_can_make, "cup(s) of coffee")
    else:
        print("No, I can make only", min_cups_can_make, "cups of coffee")

# this block will execute if all of the ingredient is more than the required
elif water >= water_required and milk >= milk_required and coffee_beans >= coffee_beans_required:
    if water_for_coffee > cup_of_coffee and milk_for_coffee > cup_of_coffee and coffee_beans_for_coffee > cup_of_coffee:
        print("Yes, I can make that amount of coffee (and even", available_cups, "more than that)")
    elif water_for_coffee >= cup_of_coffee and milk_for_coffee >= cup_of_coffee and coffee_beans_for_coffee >= cup_of_coffee:
        print("Yes, I can make that amount of coffee")