import math

X = int(input())

ans = 0
mount = 100
while X > mount:
	ans += 1
	mount = math.floor(mount * 1.01)
print(ans)
