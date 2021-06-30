def gcd(a,b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

[X, L] = input().split()
[X, L] = [int(X), int(L)]

count = 0
for B in range(X):
    for A in range(B):
        # print(A, B, gcd(A, B), X)
        if gcd(A, B) == L:
            count += 1

print(count)