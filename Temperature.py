q = input('c -> f / f -> c : ')
if q == 'c -> f': 
	c = input('Today temperature(C) : ')
	c = float(c)
	f = c * 9 / 5 + 32
	print('F = ', f)
else: 
	f = input('Today temperature(F) : ')
	f = float(f)
	c = (f - 32) * 5 / 9
	print('C =', c)