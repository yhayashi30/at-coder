import math
    
K = int(input())

sum = 0
dict = {}
for a in range(K):
	for b in range(K):
		ab = math.gcd(a+1, b+1)
		if ab in dict:
			dict[ab] = dict[ab]+1 
		else:
			dict[ab] = 1
for c in range(K):
	for ab in dict:
		sum += math.gcd(ab, c+1)*dict[ab]
print(sum)
	
