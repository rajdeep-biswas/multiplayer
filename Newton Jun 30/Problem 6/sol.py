import itertools

N = int(input())
F = [int(item) for item in input().split()]
G = [int(item) for item in input().split()]

Fi = {}
Arr = []

for i in range(N):
	if G[i] == 0:
		Fi[i] = list(range(0, F[i] + 1))
	else:
		Fi[i] = list(range(F[i], (10 ** 18) % 1000000007))

products = Fi[0]

for i in range(1, N):
	products = itertools.product(products, Fi[i])

print(sum([list(product) for product in products][0]))

"""
print(Fi)
count = 0
for i in range(N - 1):
	print(list(itertools.product(Fi[i], Fi[i + 1])))
	count += ['47' in str(sum(tup)) for tup in list(itertools.product(Fi[i], Fi[i + 1]))].count(True)
"""