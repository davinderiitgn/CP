N,D = map(int, raw_input().split())
L = []
for _ in range(N):
	L.append(input())
L = sorted(L)
count = 0
while(len(L)!=0):
	if len(L) == 1:
		L = []
	else:
		a = L.pop(0)
		b = L[0]
		if b-a<=D:
			count+=1
			L.pop(0)
print count
