print("+-------------------+")
m =19
for i in range (1, m+1, 2): 
	print("|{}{}".format(" "*int((m-i)/2),"#"*i),end="")
	for x in range(int((m-i)/2)):
		print(" ",end="")
	print("|")
print("+-------------------+")
