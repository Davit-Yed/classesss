import random
x = random.randint(1,9)
y = random.randint(1,9)
z = random.randint(1,9)
q = random.randint(1,9)
v = True
n = 0
m = 0
while v:
	r = input("gushaki 4 tvic kazmvvac tiv")
	print(x,y,z,q)
	a = int(r[0])
	b = int(r[1])
	c = int(r[2])
	d = int(r[3])
	x = int(x)
	y = int(y)
	z = int(z)
	q = int(q)
	if x == a and y == b and z == c and q == d:
		v = False	
	if x == a:
		n = n + 1
	if b == y:
		n = n + 1
	if z == c:
		n = n + 1
	if q == d:
		n = n + 1
	x = str(x)
	y = str(y)
	z = str(z)
	q = str(q)
	if x in r and int(x) != a:
		m = m + 1
	if y in r and int(y) != b:
		m = m + 1
	if z in r and int(z) != c:
		m = m + 1
	if q in r and int(q) != d:
		m = m + 1
	print("cows",n,"buls",m)





