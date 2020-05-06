N, K = map(int, input().split())

def sumLR(l, r):
	return (l+r)*(r-l+1)//2

mod = 10**9 + 7
count = 0

for n in range(K, N+2):
	max = sumLR(N-n+1, N)
	min = sumLR(0, n-1)
	count += max - min + 1
	count %= mod
print(count)
