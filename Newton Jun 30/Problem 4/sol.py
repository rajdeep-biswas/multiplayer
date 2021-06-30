# Your code here
[A, B] = input().split()
[A, B] = [int(A), int(B)]

likeA = A / (A + B)
likeB = B / (A + B)

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

if A == 0 or B == 0:
    print(0)
    exit()

if likeA > likeB:
    print(modInverse(A, 1000000007))

else:
    print(modInverse(B, 1000000007))