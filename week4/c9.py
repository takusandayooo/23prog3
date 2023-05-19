m = int(input())

line= "+"
for i in range (m):
	line += "-"
line += "+"

f = "|{:^"
g = "}"
h = "{}"
t = f+g+h


print(line)
for i in range (1, m+1, 2):
	print(t.format(" "*int((m-i)/2),"#"*i),end="")
	for x in range(int((m-i)/2)):
		print(" ",end="")
	print("|")
print(line)