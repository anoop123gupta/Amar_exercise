user=raw_input(" Enter String ")
a=user[-3:]
if a!='ing':
	print user+'ing'
elif a=='ing':
	rep = user.replace('ing', 'ly')
	print rep