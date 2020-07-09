water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cup_of_coffee = int(input("Write how many cups of coffee you will need:\n"))

possible_cup = int((water+milk+coffee_beans)/(200+50+12))

water_for_one = cup_of_coffee * 200
milk_for_one = cup_of_coffee * 50
coffee_for_one = cup_of_coffee * 15

if water < water_for_one or milk < milk_for_one or coffee_beans < coffee_for_one:
    if int(water/200) == int(milk/50) and int(water/200) == int(coffee_beans/15) and int(milk/50) == int(coffee_beans):
        print("No, I can make only", possible_cup, "cup(s) of coffee")

    elif int(water/200) < int(milk/50) and int(water/200) < int(coffee_beans/15):
        print("No, I can make only", int(water/200), "cup(s) of coffee")

    elif int(milk/50) < int(water/200) and int(milk/50) < int(coffee_beans/15):
        print("No, I can make only", int(milk/50), "cup(s) of coffee")
    else:
        print("No, I can make only", int(coffee_beans/15), "cups of coffee")

elif water > water_for_one or milk > milk_for_one or coffee_beans > coffee_for_one:
    if int(water/200) > cup_of_coffee and int(milk/50) > cup_of_coffee and int(coffee_beans/15) > cup_of_coffee:
        print("Yes, I can make that amount of coffee (and even", min(int(water/200), int(milk/50), int(coffee_beans/15)) - cup_of_coffee, "more than that)")
    elif int(water/200) >= cup_of_coffee and int(milk/50) >= cup_of_coffee and int(coffee_beans/15) >= cup_of_coffee:
        print("Yes, I can make that amount of coffee")