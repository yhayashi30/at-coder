N, K = map(int, input().split())

def cmb(n, r, mod):
	if ( r<0 or r>n ):
		return 0
	r = min(r, n-r)
	return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
M = N+1
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, M + 1 ):
	g1.append( ( g1[-1] * i ) % mod )
	inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
	g2.append( (g2[-1] * inverse[-1]) % mod )
    
ans = 0
for j in range(K, N+1):
	ans += cmb(N+1, j, mod)
print(ans)