def function(n, k):
    """
    The function return the numbers which respect the rules:
    numbers of 𝒏 digits equal to 𝒌 multiplied by their product.
    input: n ( n<=9 and 1<=n , n is a integer)
       k ( k<=100 and 1<=k, k is a integer)
    output: l (list )
    """
    i = 10 ** (n - 1)
    l = []
    while i < 10 ** n:
        copy = i
        product = 1
        while copy > 9:
            product = product * int(copy % 10)
            copy = copy / 10
        if k * product == i:
            l.append(i)
        i = i + 1
    return l


print("Please input the n (number of digits) and the number k ")
n = int(input('n='))
k = int(input('k='))
l1 = function(n, k)
if l1:
    print("The numbers of ", n, " digits which satisfy the rules are:", l1)
else:
    print("There are doesn't exist such numbers of ", n, 'digits')

print('')
input('Press any key to exit')
