limit = 2000000

isPrime = [True] * limit

i = 2
while i * i <= limit:
    if isPrime[i]:
        for j in range(i * i, limit, i):
            isPrime[j] = False
    i += 1
isPrime[1] = False

s = 0
for i in range(1, len(isPrime)):
    if isPrime[i]:
        s += i

print(s)