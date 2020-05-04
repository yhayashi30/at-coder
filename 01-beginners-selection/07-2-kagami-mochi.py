N = int(input())
Dj = sorted([int(input()) for i in range(N)])

result = 1
if N == 0:
	result = 0
else:
	for i in range(N-1):
		if Dj[i] != Dj[i+1]:
			result += 1
print(result)
