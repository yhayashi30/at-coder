N = int(input())
aj = sorted(list(map(int, input().split())), reverse=True)

sum = 0

for i in range(len(aj)):
	if i%2 == 0:
		sum += aj[i]
	else:
		sum -= aj[i]
print(sum)
