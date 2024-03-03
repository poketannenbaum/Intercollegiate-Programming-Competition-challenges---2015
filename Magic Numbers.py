import re
numbers = input ("Enter numbers ")
endnum = numbers
numbers = list(numbers)
counter = len(numbers)
count1 = 0
count2 = 1
revcount = 0
modcount = 0
prognum = ""
while(counter != 0):
	try:
		prognum += numbers[revcount]
		prognum = int(prognum)
		modcount = prognum % count2
		if modcount != 0:
			print(f"{endnum} is not a magic number!")
			break
	except:
		break
	revcount += 1
	counter -= 1
	count2 += 1
	prognum = str(prognum)
if modcount == 0:
	print(f"{endnum} is a magic number!")
	


