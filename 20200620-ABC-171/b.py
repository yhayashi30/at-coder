	N, K = map(int, input().split())
	pn = sorted(list(map(int, input().split())))
	ans = 0
	for i in range(K):
		ans += pn[i]
		
	print(ans)

