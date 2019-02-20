num=input("Give me a number ")
var=num
print "3 pichle even numbers "
for i in range(0,3):
	num=num-2
	print num
print "3 agle odd numbers "
if var%2==0:
	var=var-1
	for i in range(0,3):
		var=var+2
		print var
		