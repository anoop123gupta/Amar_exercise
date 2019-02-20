num=int(raw_input("Give  me a number "))
for i in range(1,num+1):
	add=0
	for j in range(1,i):
		if i%j==0:
			add=add+j
	if add==i:
			print i

