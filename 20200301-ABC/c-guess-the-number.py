N, M = map(int, input().split())
scj = [list(map(int, input().split())) for i in range(M)]

flg = False
result = ['none']*N
for sc in scj:
	if result[sc[0]-1] == 'none' or result[sc[0]-1] == str(sc[1]):
		result[sc[0]-1] = str(sc[1])
	else:
		flg = True
		break
if flg == True or result[0] == 'none' or (N != 1 and result[0] == '0'):
	print(-1)
else:
	ans = ''
	for re in result:
		if re != 'none':
			ans += re
		else:
			ans += '0'
	print(int(ans))
