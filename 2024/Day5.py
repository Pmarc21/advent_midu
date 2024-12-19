# Santa Claus's elves 🧝🧝‍♂️ have found a bunch of mismatched magic boots in the workshop. Each boot is described by two values:

# type indicates if it's a left boot (I) or a right boot (R).
# size indicates the size of the boot.
# Your task is to help the elves pair all the boots of the same size having a left and a right one. To do this, you should return a list of the available boots after pairing them.

# Note: You can have more than one pair of boots of the same size!

# const shoes = [
#   { type: 'I', size: 38 },
#   { type: 'R', size: 38 },
#   { type: 'R', size: 42 },
#   { type: 'I', size: 41 },
#   { type: 'I', size: 42 }
# ]

# organizeShoes(shoes)
# // [38, 42]

shoes = [
  {'type': 'I', 'size': 38 },
  {'type': 'R', 'size': 38 },
  {'type': 'R', 'size': 38 },
  {'type': 'I', 'size': 38 },
  {'type': 'I', 'size': 38 } 
]
def organizeShoes(shoes):
    new_shoes = {}
    for shoe in shoes:
        size = shoe['size']
        type_shoe = shoe['type']
        if size not in new_shoes:
            new_shoes[size] = {'I':0, 'R':0}
        
        new_shoes[size][type_shoe] += 1
    paired_boots = []
    for size, counts in new_shoes.items():
        left_boots = counts['I']
        right_boots = counts['R']
        
        pairs = min(left_boots, right_boots)
        for i in range(pairs):
            paired_boots.append(size)
    return paired_boots

organizeShoes(shoes)