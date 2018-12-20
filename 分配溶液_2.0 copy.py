inf = input().split()
m = int(inf[0])
n = int(inf[1])

def scatter(m, a):
	if a == 1:
		return 1
	if a == 2:
		return m // 2
	else:
		return scatter_1(m-a, a)

def scatter_1(m, a):
	if m == 0:
		return 1
	else:
		cnt = 0
		if a > m:
			a = m
		while a >= 1:
			cnt += scatter(m, a)
			a = a - 1
		return cnt

print(scatter_1(m, n))

