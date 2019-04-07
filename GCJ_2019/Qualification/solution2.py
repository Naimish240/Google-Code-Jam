# Solution for question 2

def replace(moves):
    l = []
    for i in moves:
        if i == 'S':
            l.append('E')
        else:
            l.append('S')
    
    return ''.join(i for i in l)


cases = int(input())

for i in range(cases):
    grid_size = int(input())
    moves = input()

    print('Case #{}: {}'.format(i+1, replace(moves)))

# Score : 5 + 9
