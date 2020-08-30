S = input()
T = input()

ans = 10**9

for i in range(len(S)-len(T)+1):
	tmpS = S[i:i+len(T)]
	cnt = 0
	for j in range(len(T)):
		if tmpS[j] != T[j]:
			cnt += 1
	ans = min(ans, cnt)
print(ans)
