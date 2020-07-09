water_in_machine = 400
milk_in_machine = 540
coffee_beans_in_machine = 120
disp_cups_in_machine = 9
money_in_machine = 550

def machine_state():
    print("The coffee machine has:")
    print(water_in_machine, "of water")
    print(milk_in_machine, "of milk")
    print(coffee_beans_in_machine, "of coffee beans")
    print(disp_cups_in_machine, "of disposable cups")
    print(money_in_machine, "of money")

def action():
    machine_state()
    print()
    choice = input("Write action (buy, fill, take):\n")
    if choice == "buy":
        buy()
    elif choice == "fill":
        fill()
    elif choice == "take":
        take()

def buy():
    coffee_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if coffee_choice == "1":
        global water_in_machine
        water_in_machine -= 250
        global milk_in_machine
        milk_in_machine -= 0
        global coffee_beans_in_machine
        coffee_beans_in_machine -= 16
        global disp_cups_in_machine
        disp_cups_in_machine -= 1
        global money_in_machine
        money_in_machine += 4
        print()
        machine_state()
    elif coffee_choice == "2":
        water_in_machine -= 350
        milk_in_machine -= 75
        coffee_beans_in_machine -= 20
        disp_cups_in_machine -= 1
        money_in_machine += 7
        print()
        machine_state()
    elif coffee_choice == "3":
        water_in_machine -= 200
        milk_in_machine -= 100
        coffee_beans_in_machine -= 12
        disp_cups_in_machine -= 1
        money_in_machine += 6
        print()
        machine_state()

def fill():
    water_to_add = int(input("Write how many ml of water do you want to add:\n"))
    milk_to_add = int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans_to_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
    disp_cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    global water_in_machine
    global milk_in_machine
    global coffee_beans_in_machine
    global disp_cups_in_machine
    water_in_machine += water_to_add
    milk_in_machine += milk_to_add
    coffee_beans_in_machine += coffee_beans_to_add
    disp_cups_in_machine += disp_cups_to_add
    print()
    machine_state()

def take():
    global money_in_machine
    print("I will give you $" + str(money_in_machine))
    print()
    money_in_machine -= money_in_machine
    print()
    machine_state()

action()
