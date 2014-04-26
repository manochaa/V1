def rec(n,x,y):
	if n >= y:
		return 0
	return 1 + rec(n/(x+1.0),x,y-n)

print rec(50,2,150)