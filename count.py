#This program counts the numer of characters in text
from operator import itemgetter

message = '''Practice Projects
For practice, write programs to do the following tasks.

Fantasy Game Inventory (what a name)
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:


Bag:
13 arrow
42 gold coin
1 rope
6 torch
5 dagger

Total number of items: 66
Hint: You can use a for loop to loop through all the keys in a dictionary.


# bag.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 5, 'arrow': 13}

def displayBag(bag):
    print("Bag:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
    print("Total number of items: " + str(item_total))

displayBag(stuff)
List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished monster’s loot is represented as a list of strings like this:


monsterLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like monsterLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:


def addToBag(bag, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
monsterLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, monsterLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:


Bag:
45 gold coin
1 rope
5 ruby
5 dagger

Total number of items: 53


'''
count = {}

for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] + 1
    
for key, value in sorted(count.items(), key = itemgetter(1), reverse = True):
    print(key,value)
