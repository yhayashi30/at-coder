A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())
N = int(input())
bj = [int(input()) for i in range(N)]

result = []
result.append([A11, A12, A13])
result.append([A13, A23, A33])
result.append([A33, A32, A31])
result.append([A31, A21, A11])
result.append([A12, A22, A32])
result.append([A21, A22, A23])
result.append([A11, A22, A33])
result.append([A31, A22, A13])

flg = 'No'
for cmb in result:
	count = 0
	for i in bj:
		if i in cmb:
			count += 1
	if count == 3:
		flg = 'Yes'
print(flg)
