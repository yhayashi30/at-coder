N = int(input())
Ali = list(map(int, input().split()))
cnt = 0
flg = True
while flg:
	for i in range(N):
		if Ali[i]%2 == 0:
			Ali[i] = Ali[i]/2
		else:
			flg = False
			break
	if flg:
		cnt += 1
print(cnt)
