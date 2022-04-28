def function(n, k):
    """

    :param n (integer) , k (integer)
    :return l (list) all powers less than 𝒌 of a given integer number 𝒏.
    """
    if n == 1:
        return [1]
    else:
        l = []
        i = 1
        while i < k:
            l.append(i)
            i = i * n

    return l

print("Please input n and k")
n = int(input("n="))
k = int(input("k="))
l1 = function(n, k)
if l1:
    print(l1)
else:
    print("There are no powers of", n, "smaller then", k)
print('')
input("Press any key to exit")
