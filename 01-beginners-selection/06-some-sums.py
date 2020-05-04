N, A, B = map(int, input().split())

sum = 0
for i in range(N):
	num = 0
	for s in list(str(i+1)):
		num += int(s)
	if num>=A and num<=B:
		sum += i+1
print(sum)
