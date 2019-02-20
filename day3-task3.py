user=input("Enter a  number ")
num=list(str(user))
print num
add=0
for i in num:
	fact=1
	a=int(i)
	for j in range(1,a+1):
		fact=fact*j
	# print fact
	add=add+fact
print add
