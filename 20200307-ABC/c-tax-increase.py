import math
A, B = map(int, input().split())

X = math.floor(A/0.08)
Y = math.floor(B/0.1)

flg = True
if X == Y:
	print(X)
else:
	if X > Y:
		xySa = X - Y
		for i in range(xySa+1):
			if math.floor((Y+i) * 0.08) == math.floor((Y+i) * 0.1):
				flg = False
				print(Y+i)
				break
		if flg:
			print(-1)
	else:
		yxSa = Y - X
		for i in range(yxSa+1):
			if math.floor((X+i) * 0.1) == math.floor((X+i) * 0.08):
				flg = False
				print(X+i)
				break
		if flg:
			print(-1)
