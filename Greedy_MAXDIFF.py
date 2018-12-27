# sort and pick the first k smallest or last k largest elements
T = input()
for _ in range(T):
	N,K = map(int, raw_input().split())
	W = map(int, raw_input().split())
	W = sorted(W)
	w11 = 0
	w21 = 0
	SUM = sum(W)
	for i in range(K):
		w11 += W[i]
	w21 = SUM - w11
	diff1 = abs(w11-w21)
	W = list(reversed(sorted(W)))
	w21 = 0
	w22 = 0
	for i in range(K):
		w21 += W[i]
	w22 = SUM - w21
	diff2 = abs(w21 - w22)
	print max(diff1, diff2)


