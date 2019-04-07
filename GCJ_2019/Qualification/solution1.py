# Code for first problem

# Function to find a possible combiantion
# Takes 'val' as input, and returns a list
# The list is of the format [A, B]

from random import randint

# Checks if the solution has 4 in it or not
def check_validity(a, b):
    if '4' in str(a) or '4' in str(b):
        return 0
    else:
        return 1

def bruteForce(val):
    for a in range(1, val):
        b = val - a

        if check_validity(a, b):
            return [a, b]

def replace_four(val):
    l = [i for i in str(val)]
    a = []
    b = []

    if l.count('4') == 0:
        if l[-1] == '5':
            return [2, val-2]
        return [1, val-1]

    for i in l:
        if i == '4':
            a.append('3')
            b.append('1')
        else:
            a.append(i)
            b.append('0')
    
    a = int(''.join(i for i in a))
    b = int(''.join(i for i in b))

    if a + b == val and check_validity(a, b):
        return [a, b]
    
    return bruteForce(val)

# Gets test cases
test_cases = int(input())
#test_cases = 100

amt = []

for case in range(test_cases):
    # Gets amount for the case from input
    amount = int(input())
    #amount = randint(1, 100000000)
    # Calculates possible combination
    combination = replace_four(amount)
    print('Case #{}: {} {}'.format(case + 1, combination[0], combination[1]))
    #print('Case #{}: {} : {} {}'.format(case + 1, amount ,combination[0], combination[1]))

# Score for this round: 6 + 10