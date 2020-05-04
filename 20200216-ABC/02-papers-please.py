N = int(input())
Aj = list(map(int, input().split()))
flg = True
for A in Aj:
	if A%2==0 and (A%3!=0 and A%5!=0):
		print('DENIED')
		flg = False
		break
if flg:
	print('APPROVED')
		
