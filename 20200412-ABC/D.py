N = int(input())
S = list(input())

R = 0
G = 0
B = 0

for i in range(N):
	if S[i] == 'R':
		R += 1
	elif S[i] == 'G':
		G += 1
	else:
		B += 1
ans = R*G*B
for i in range(N-2):
	for j in range(i+1, N-1):
		k = j+(j-i)
		if k >= N:
			break
		if S[i]!=S[j] and S[i]!=S[k] and S[j]!=S[k]:
			ans -= 1
print(ans)
