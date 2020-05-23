import copy
N, M, Q = map(int, input().split())
Qj = [list(map(int, input().split())) for i in range(Q)]

ans = 0

def dfs(Aj):
	global ans
	if len(Aj) == N:
		now = 0
		for Q in Qj:
			if Aj[Q[1]-1] - Aj[Q[0]-1] == Q[2]:
				now += Q[3]
		ans = max(ans, now)
		return;
	if len(Aj) == 0:
		Aj.append(1)
	else:
		Aj.append(Aj[-1])
	while Aj[-1] <= M:
		dfs(copy.deepcopy(Aj))
		Aj[-1] += 1
Aj = []
dfs(Aj)
print(ans)
