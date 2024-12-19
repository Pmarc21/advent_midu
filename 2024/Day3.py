# You will receive an array of objects, where each object represents a toy and has the properties:

# name: the name of the toy (string).
# quantity: the available quantity of that toy (integer).
# category: the category to which the toy belongs (string).
# Write a function that processes this array and returns an object that organizes the toys as follows:

# The keys of the object will be the categories of toys.
# The values will be objects that have the toy names as keys and the total quantities of each toy in that category as values.
# If there are toys with the same name in the same category, you must sum their quantities.
# If the array is empty, the function should return an empty object {}.
import json

inventory = [
    { 'name': 'doll', 'quantity': 5, 'category': 'toys' },
    { 'name': 'car', 'quantity': 3, 'category': 'toys' },
    { 'name': 'ball', 'quantity': 2, 'category': 'sports' },
    { 'name': 'car', 'quantity': 2, 'category': 'toys' },
    { 'name': 'racket', 'quantity': 4, 'category': 'sports' }
]

def organizeInventory(inventory):
  new_inventory = {}
  for item in inventory:
    category = item['category']
    name = item['name']
    quantity = item['quantity']
    if category not in new_inventory:
        new_inventory[category] = {}
    
    if name in new_inventory[category]:
       new_inventory[category][name] += quantity
    else:
       new_inventory[category][name] = quantity
  return new_inventory

print(organizeInventory(inventory))