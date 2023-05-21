MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


logo = """
 _____        __  __           ___  ___           _     _            
/  __ \      / _|/ _|          |  \/  |          | |   (_)           
| /  \/ ___ | |_| |_ ___  ___  | .  . | __ _  ___| |__  _ _ __   ___ 
| |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ )
| \__/\ (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
 \____/\___/|_| |_| \___|\___| \_|  |_/\__,_|\___|_| |_|_|_| |_|\___|                                                                    
"""
info = """
Type 'report' for check resources.
Type 'off' for close the machine.
"""