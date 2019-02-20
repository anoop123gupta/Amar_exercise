user=raw_input("String ")
if len(user)>2:
	print user[0]+user[1]+user[-2]+user[-1]
elif len(user)==2:
	print user+user
else:
	print " "
	