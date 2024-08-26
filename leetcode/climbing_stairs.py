def climbStairs(n):
	a, b = 1, 2

	if n == 0:
		return 0
	if n == 1:
		return 1

	for i in range(n - 2):
		new = a + b
		a = b
		b = new
	return b
