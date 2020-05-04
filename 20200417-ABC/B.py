N, M = map(int, input().split())
Aj = list(map(int, input().split()))

ans = N

for A in Aj:
	ans -= A 
	if ans < 0:
		ans = -1
		break
print(ans)
