def is_kaibun(kaibun):
	for i in range(len(kaibun)//2):
		if kaibun[i] != kaibun[-i-1]:
			return False
	return True

def main():
	S = input()
	S2 = S[:(len(S)-1)//2]
	S3 = S[(len(S)+3)//2-1:]
	if is_kaibun(S) and is_kaibun(S2) and is_kaibun(S3):
		print('Yes')
	else:
		print('No')

if __name__ == "__main__":
    main()
