def sankakukei(a,b,c):
	lis=[a,b,c]
	lis.sort()
	if(lis[2]<lis[0]+lis[1]):
		return True
	else:
		return False
print("3pen 1 2 3 ha", end=" ")
if sankakukei(1, 2, 3):
	print("Sankakukei")
else:
	print("Sankakukei denai")

print("3pen 6 6 6 ha", end=" ")
if sankakukei(6, 6, 6):
	print("Sankakukei")
else:
	print("Sankakukei denai")
print("3pen 4 5 6 ha", end=" ")
if sankakukei(4, 5, 6):
	print("Sankakukei")
else:
	print("Sankakukei denai")
