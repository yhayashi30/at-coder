import copy

def check(li):
	count = 0
	cli = copy.copy(li)
	for l in li:
		del cli[0]
		for i in cli:
			if l == i:
				count += 1
	return count		 

def main():
	N = int(input())
	Aj = list(map(int, input().split()))
	for i in range(len(Aj)):
		li = copy.copy(Aj)
		del li[i]
		print(check(li))

if __name__ == "__main__":
    main()
