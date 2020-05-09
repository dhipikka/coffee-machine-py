msg = """The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money"""
# available quantities
water = 400
milk = 540
beans = 120
cups = 9
money = 550
print(msg)
print()
# asking for user input
print("Write action (buy, fill, take):")
action = input()
# buying a coffee
def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    type = input()    
    def makeEspresso():
        global water,beans,money,cups,milk
        water = water - 250
        beans = beans - 16
        money = money + 4
        cups = cups - 1
    def makeLatte():
        global water,beans,money,cups,milk
        water = water - 350
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups -1
    def makeCappuccino():
        global water,beans,money,cups,milk
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups -1
    if type == "1":
        makeEspresso()
    elif type == "2":
        makeLatte()
    else:
        makeCappuccino()
# taking the money from the machine
def take():
    global money
    print("I gave you $" + str(money))
    money = 0
# filling the coffee machine
def fill():
    global water,beans,cups,milk
    print("Write how many ml of water do you want to add:")
    water_filled = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_filled = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans_filled = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups_added = int(input())
    water = water + water_filled
    milk = milk + milk_filled
    beans = beans + beans_filled
    cups = cups + cups_added
if action == "buy":
    buy()
elif action == "take":
    take()
else:
    fill()
print()
print("The cofee machine has:")
print(str(water) + " of water")
print(str(milk) + " of milk")
print(str(beans) + " of coffee beans")
print(str(cups) + " of disposable cups")
print(str(money) + " of money")
