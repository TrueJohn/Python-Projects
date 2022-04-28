def prime(nr):
    '''
      in this function we find if nr is a prime number
      input:n (integer)
      output: True or False
    '''
    if (nr < 2):
        return False
    for i in range(2, nr, 1):
        if nr % i == 0:
            return False
    return True


'''
n is a natural number
we take all numbers with n digits and print only the numbers with the property
that that all its prefixes are also prime
'''
print("Please input the amount of digits")
n = int(input('n='))
rez = 10 ** (n - 1)
# rez is an natural number
while rez < 10 ** n:
    copy = rez
    ok = 1
    while copy > 0 and ok == 1:
        if prime(copy) == False:
            ok = 0
        else:
            copy = copy // 10
    if ok == 1:
        print(rez, end=' ')
        break
    rez = rez + 1
print('')
input('Press any key to exit')