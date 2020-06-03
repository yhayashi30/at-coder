N = int(input())
Aj = list(map(int, input().split()))

ans = 1
ng = False
max = 10**18
for A in Aj:
	if A == 0:
		ans = 0
		break
	if ng or ans*A > max:
		ans = -1
		ng = True
	else:
		ans *= A
print(ans)

