# Your code here
[A, B] = input().split()
[A, B] = [int(A), int(B)]
winner = ""
place = 1
count = 1
while True:
    if A == 0:
        winner = "Joey"
        break
    if B == 0:
        winner = "Chandler"
        break
    if place == 1:
        B -= count
        place = 0
    else:
        A -= count
        place = 1
    count += 1
print(winner)