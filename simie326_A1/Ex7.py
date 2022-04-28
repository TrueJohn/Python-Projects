def generate(n):
    """
    input: n (an integer) 
    The function generates a list of the first n numbers with
    the property that :
    a. Number 1 belongs to M
    b. If 𝒙 belongs to M then 2𝒙+1 and 3𝒙+1 also belong to M
    c. M does not contain any other element
    
    returns l ( a list)
    
    """
    ai = 0
    bi = 0
    eq = 0
    l = [1]
    while ai + bi < n + eq:
        y = 2 * l[ai] + 1;
        z = 3 * l[bi] + 1;
        if y < z:
            l.append(y)
            ai = ai + 1
        elif y > z:
            l.append(z)
            bi = bi + 1

        else:
            l.append(y)
            ai = ai + 1
            bi = bi + 1
            eq = eq + 1

    return l.pop()


print('Please input an integer which represents the amount of number to be generated:')
n = int(input('n= '))
if n <= 0:
    print('Error')
else:
    for i in range(n):
        print(generate(i), end=' ')
print('')
input('Press any key to exit')
