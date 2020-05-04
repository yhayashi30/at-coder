N, M = map(int, input().split())

nsum = 0
for i in range(N-1):
	nsum += i+1
msum = 0
for i in range(M-1):
	msum += i+1
print(nsum + msum)

