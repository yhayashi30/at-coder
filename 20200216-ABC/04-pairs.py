N, K = map(int, input().split())
Aj = sorted(list(map(int, input().split())))
result = []
for i in range(N):
	for j in range(N-(i+1)):
		result.append(Aj[i]*Aj[j+(i+1)])
result = sorted(result)
print(result[K-1])
