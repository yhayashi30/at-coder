N = int(input())
Sj = sorted([input() for i in range(N)])

maxCnt = 0
cnt = 0
result = []
str = ''
for S in Sj:
	if S == str:
		cnt += 1
	else:
		str = S
		cnt = 1
	if cnt > maxCnt:
		maxCnt = cnt
		result = [S]
	elif cnt == maxCnt:
		result.append(S)
for rStr in result:
	print(rStr)	
