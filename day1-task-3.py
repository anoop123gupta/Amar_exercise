num_loop=input("Give me a number for loop ")
for num in range(1,num_loop+1):
	user=list(str(num))
	# print user
	add=0
	for i in user:
		b=int(i)
		add=add+b**3
	# print add
	if add==num:
		print (num, 'Armstrong number  hai')

# ----------------------check a number------------

# user=input("Give me a number ")
# num=list(str(user))
# # print num 
# add=0
# for i in num:
# 	b=int(i)
# 	add=add+b**3
# print 'add of each digit is ', add
# if add==user:
# 	print '{0} {1}'.format(user,'Armstrong number  hai ')
# else:
# 	print '{0} {1}'.format(user,'Armstrong number nahi hai ')
