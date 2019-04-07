# Solution for problem 3

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

cases = int(input())

for case in range(cases):
    text = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    ch = input().split()
    no_of_chars = int(ch[1])
    max_prime = int(ch[0])
    
    products = [int(i) for i in input().split()]

    factors = []
    pairs = []
    for i in range(len(products)):
        l = prime_factors(products[i])
        a, b = l[0], l[1]
        if i > 0:
            if pairs[i-1][1] == a:
                flag = True
            else:
                a, b = b, a
        pairs.append([a, b])

        if a in factors:
            flag = True
        else:
            factors.append(a) 

        if b in factors:
            flag = False
        else:
            factors.append(b)

    factors.sort()
    for i in pairs:
        text += alphabets[factors.index(i[0])]
    text += alphabets[factors.index(pairs[-1][1])]


    print('Case #{}: {}'.format(case + 1, text.upper()))
