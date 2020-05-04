N = int(input())
Aj = list(map(int, input().split()))

anss = [0] * N

for A in Aj:
	anss[A-1] += 1

for ans in anss:
	print(ans)
