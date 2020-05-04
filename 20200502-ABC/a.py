K = int(input())
A, B = map(int, input().split())

flg = False
for i in range(A, B):
	if i % K == 0:
		flg = True
		break

if flg or A % K == 0 or B % K == 0:
	print('OK')
else:
	print('NG')
