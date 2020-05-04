N, A, B = map(int, input().split())

cnt = N//(A+B)
amari = N%(A+B)

if amari >= A:
	print(A*cnt + A)
else:
	print(A*cnt + amari)
