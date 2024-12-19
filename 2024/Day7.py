# The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. 
# He has changed the order of some packages, so shipments cannot be made.

# Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

# You will receive a string containing letters and parentheses.
# Every time you find a pair of parentheses, you need to reverse the content within them.
# If there are nested parentheses, solve the innermost ones first.
# Return the resulting string with parentheses removed, but with the content correctly reversed.
# He left us some examples:

packages = 'abc(def(gh)i)jk'

def fix_packages(packages):
    stack = []
    
    for character in packages:
        if character == ')':
            temp = ''
            while stack and stack[-1] != '(':
                print(temp)
                temp += stack.pop()
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(character)
    return ''.join(stack)

print(fix_packages(packages))