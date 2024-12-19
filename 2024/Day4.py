# It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. 
# We're going to create a function that receives the height of the tree (a positive integer between 1 and 100) and a special character to decorate it.

# The function should return a string that represents the Christmas tree, constructed as follows:

# The tree is made up of triangles of special characters.
# The spaces on the sides of the tree are represented with underscores _.
# All trees have a trunk of two lines, represented by the # character.
# The tree should always have the same length on each side.
# You must ensure the tree has the correct shape using line breaks \n for each line.

# const tree = createXmasTree(5, '*')
# /*
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____
# */

def create_xmas_tree(height, ornament):
    outside_tree_character = '_'
    tree = []
    i = 0
    k = 0
    max_len_ornament = (2*height -1) # en realidad es (2*height -1) + 2
    max_len_tree = max_len_ornament
    middle_number = (max_len_tree - 1) // 2
    for i in range(height):
        row = ''
        for j in range(0,max_len_tree):
            if j > middle_number + i or j < middle_number - i:
                row += outside_tree_character
            else:
                row += ornament
        tree.append(row)
        i += 1
    for k in range(2):
        row = ''
        l = 0
        while l < max_len_tree:
            if l < middle_number:
                row += outside_tree_character
            elif l == middle_number:
                row += '#'
            else:
                row += outside_tree_character
            l += 1
        tree.append(row)
        k += 1
    return '\n'.join(tree)

print(create_xmas_tree(3,'+'))
print(create_xmas_tree(7,'.'))