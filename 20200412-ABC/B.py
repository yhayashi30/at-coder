N = int(input())

sum = 0
for i in range(N):
	if (i+1)%3 != 0 and (i+1)%5 != 0:
		sum += i+1
print(sum)
