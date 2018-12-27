import math
T = input()

def foo(p):
	if p == 0:
		return 0
	ptwo = int(math.log(p,2))
	count = 0
	if ptwo <= 11:
		count += 1
		remaining = p - pow(2,ptwo)
	else:
		count += p/2048
		remaining = p%2048	
	if remaining == 1:
		count += 1
		return count
	else:
		count += foo(remaining)
		return count

for _ in range(T):
	p = input()
	print foo(p)
