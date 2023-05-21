from data import *

# TODO: 5. Process coins. (If we have enough resources for make ordered coffee than calculate price.)
price = 0
result = 0


def check_coins(orders, quarter=0, dime=0, nickle=0, penni=0):
    """First parameter taking input order e.g ('latte')
    than calculating total money of coins
    after that checking order's price and coin total
    return True or False"""
    global result
    result = (0.25*quarter)+(0.10*dime)+(0.05*nickle)+(0.01*penni)
    global price
    price = MENU[orders]["cost"]
    if result > price:
        return True
    else:
        return False


# TODO: 3. Print report of all resources.
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def data_format(dictionary):
    water1 = dictionary["water"]
    milk1 = dictionary["milk"]
    coffee1 = dictionary["coffee"]
    return f"Water: {water1}\nMilk: {milk1}\nCoffee: {coffee1}\nMoney: ${money}"

# TODO: 4. Check resources sufficient? (After the user order and type of coffee check for enough resources)

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


machine = True


while machine:
    print(logo, info)
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "espresso":
        espresso_water = MENU["espresso"]["ingredients"]["water"]
        espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        if espresso_coffee < coffee and espresso_water < water:
            # TODO: 6. Check transaction successful? (If there is not enough money for order give feedback about that)
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            if check_coins(order, quarters, dimes, nickles, pennies):
                change = round(result - price, 2)
                # TODO: 7. Make a coffee (Print resources before the coffee than print again after the coffee)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
                money += price
                water -= espresso_water
                coffee -= espresso_coffee
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry not enough resources for make this order.")
    elif order == "latte":
        latte_water = MENU["latte"]["ingredients"]["water"]
        latte_milk = MENU["latte"]["ingredients"]["milk"]
        latte_coffee = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        if latte_coffee < coffee and latte_milk < milk and latte_water < water:
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            if check_coins(order, quarters, dimes, nickles, pennies):
                change = round(result - price, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
                money += price
                water -= latte_water
                milk -= latte_milk
                coffee -= latte_coffee
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry not enough resources for make this order.")
    elif order == "cappuccino":
        cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
        cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
        cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["cappuccino"]["cost"]
        if cappuccino_coffee < coffee and cappuccino_milk < milk and cappuccino_water < water:
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            if check_coins(order, quarters, dimes, nickles, pennies):
                change = round(result - price, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
                money += price
                water -= cappuccino_water
                milk -= cappuccino_milk
                coffee -= cappuccino_coffee
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry not enough resources for make this order.")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif order == "off":
        machine = False
        print("Good Bye...")
    elif order == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")
