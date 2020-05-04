A = int(input())
B = int(input())
C = int(input())
X = int(input())

sumA = [0]*(A+1)
sumAB = [0]*((A+1)*(B+1))
sumABC = [0]*((A+1)*(B+1)*(C+1))
for i in range(A+1):
	sumA[i] = 500*i
bidx = 0
for j in range(B+1):
	for sa in sumA:
		sumAB[bidx] = sa+(100*j)
		bidx += 1
cidx = 0
for k in range(C+1):
	for sab in sumAB:
		sumABC[cidx] = sab+(50*k)
		cidx += 1
cnt = 0
for s in sumABC:
	if X == s:
		cnt += 1
print(cnt)
