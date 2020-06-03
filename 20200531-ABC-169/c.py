from decimal import Decimal

A, B = map(float, input().split())
ans = int(int(A)*Decimal(str(B)))
print(ans)
