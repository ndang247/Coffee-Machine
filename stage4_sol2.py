water, milk, beans, cups, money = 400, 540, 120, 9, 550
def print_state():
    print(f'''
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of coffee cups
{money} of money
''')

def coffee_machine():
    print_state()
    global water, milk, beans, cups, money
    action = input("Write action (buy, fill, take): ")
    if action == "buy":
        cof_choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if cof_choice == 1:
            water, beans, cups, money = water - 250, beans - 16, cups - 1, money + 4
        elif cof_choice == 2:
            water, milk, beans, cups, money = water - 350, milk - 75, beans - 20, cups - 1, money + 7
        elif cof_choice == 3:
            water, milk, beans, cups, money = water - 200, milk - 100, beans - 12, cups - 1, money + 6
    elif action == "fill":
        water += int(input("Write how many ml of water do you want to add: "))
        milk += int(input("Write how many ml of milk do you want to add: "))
        beans += int(input("Write how many grams of coffee beans do you want to add: "))
        cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    elif action == "take":
        print(f"I gave you ${money}")
        money = 0
    print_state()

coffee_machine()

"""water = int(input("Write how many ml of water the coffee machine has: ")) // 200
milk = int(input("Write how many ml of milk the coffee machine has: ")) // 50
beans = int(input("Write how many grams of coffee beans the coffee machine has: ")) // 15
coffee_inp = int(input("Write how many cups of coffee you will need: "))
coffee = min(water, milk, beans)
if coffee == coffee_inp:
    print("Yes, I can make that amount of coffee")
elif coffee > coffee_inp:
    print(f"Yes, I can make that amount of coffee (and even {coffee - coffee_inp} more than that)")
elif coffee < coffee_inp:
    print(f"No, I can make only {coffee} cups of coffee")"""
