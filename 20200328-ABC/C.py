K, N = map(int, input().split())
Aj = list(map(int, input().split()))

ans = 0
max = 0 
for i in range(N-1):
	diff = Aj[i+1] - Aj[i]
	ans += diff
	if max < diff:
		max = diff
diff = K-Aj[N-1]+Aj[0] 
ans += diff
if max < diff:
	max = diff
ans -= max
print(ans)

