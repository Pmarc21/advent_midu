# You are in a very special market where Christmas trees 🎄 are sold. 
# Each one comes decorated with a series of very peculiar ornaments, 
# and the price of the tree is determined by the ornaments it has.

# *: Snowflake - Value: 1
# o: Christmas Ball - Value: 5
# ^: Decorative Tree - Value: 10
# #: Shiny Garland - Value: 50
# @: Polar Star - Value: 100
# Normally, you would sum up all the values of the ornaments and that's it…

# But, watch out! If an ornament is immediately to the left of another of greater value, 
# instead of adding, its value is subtracted.

def calculate_price(ornaments: str) -> int:
    price = 0
    ornaments_values = {'*': 1, 'o': 5, '^':10, '#':50, '@':100}
    
    for i in range(len(ornaments) - 1):
        current_value = ornaments_values.get(ornaments[i], 0)
        next_value = ornaments_values.get(ornaments[i+1], 0)

        if current_value < next_value:
            price -= current_value
        else:
            price += current_value
    
    price += next_value

    return price

ornaments = '***'
print(calculate_price(ornaments))