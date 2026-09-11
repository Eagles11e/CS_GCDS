import random

main_courses =[
    "Cauliflower",
    "Tilapia Fillet",
    "Pork loin",
    "Salmon",
    "Potatoes",
    "Three Color Squash",
    "Eggplant",
    "Steak",
    "Baguette",
    ]
mains_prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]
flairs_prices = [3, 3, 4, 4, 8, 3, 6, 4, 7]

flairs = [
    "with Balsamico",
    "with Garlic and Olive Oil",
    "with Minted Yogurt",
    "with Chutney",
    "with Salad",
    "with Salsa",
    "over Sticky Rice",
    "au Jus",
    "with Basmati Rice",
    ]

def get_menu_items():
    while True:
        try:
            return int(input("How many menu items do you need? ").strip())
            
            
        except ValueError:
            print("imput is not a valid number of items (0-9)")
            continue
        
def main(): 
    items = get_menu_items()
    menu_names = []
    menu_prices = []
    menu_flairs = []
    flair_prices = []
    
    if items > 9:
        print("You can only order up to 9 menu items, as that is our current capacity")
        get_menu_items()
    if items == 0:
        print("why are you ordering nothing, try again ")
        get_menu_items
    for _ in range(items):
        index = random.randrange(0, len(flairs))
        menu_flairs.append(flairs[index])
        item = random.choice(list(filter(lambda x: x not in menu_names, main_courses)))
        item_flair = random.choice(list(filter(lambda x: x not in menu_flairs, flairs)))
        menu_names.append(item)
        menu_prices.append(mains_prices[main_courses.index(item)])
        flairs.append(item_flair)
        flair_prices.append(flairs_prices[flairs.index(item_flair)])

    for i in range (items):
        print (f"{menu_names[i]} {menu_flairs[i]}: ${menu_prices[i] + flairs_prices[i]} ")
    print (f"The total cost is: ${sum(menu_prices) + sum(flair_prices)}")

main()