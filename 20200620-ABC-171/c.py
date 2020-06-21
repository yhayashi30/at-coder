N = int(input())

alList = list('abcdefghijklmnopqrstuvwxyz')

x = 1
y = 26
z = 0
# 何桁かを算出
while N > y:
	z += 26**x
	x += 1
	y += 26**x
if N > 26:
	tmp = N - (z+1)
else:
	tmp = N - 1
# 26進数に変換する
ans = []
while tmp > 0:
	ans.append(tmp%26)
	tmp = tmp//26
# 文字列に変換する
str = ''
for al in ans:
	str = alList[al] + str
# 桁数に足りない場合はaを付与する
while len(str) < x:
	str = 'a' + str
print(str)
