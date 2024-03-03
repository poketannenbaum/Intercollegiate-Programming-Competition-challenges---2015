xnum = int(input("Enter x "))
xnumcount = xnum
ynum = int(input("Enter y "))
nnum = int(input("Enter n "))
crosscount = 1
tallycount = 0
ansnums = []
while (xnumcount <= ynum):
	divisor1 = xnumcount
	while crosscount <= divisor1:
		if divisor1 % crosscount == 0:
			tallycount += 1
		crosscount +=1
	if tallycount == nnum:
		ansnums.append(xnumcount)
	else:
		tallycount = 0
	xnumcount += 1
	crosscount = 1
print(ansnums)