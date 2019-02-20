user=input("year ")
# ------------check leap year--------------------
if user%4==0 and user%100==0 and user%400==0:
	print "leap year ",user
elif user%4==0 and user%100!=0:
	print '{0} {1}'.format(user, 'leap year  hai ')
else:
	print '{0} {1}'.format(user, 'leap year nahi hai')
# -------------------3 previous leap year-----------------
year=user-1
add=0
print "3 pechee k leap year "
while year>0:
	if add==3:
		break
	if year%4 ==0 and year %100==0 and year%400==0:
		print year
		add+=1
	elif year%4==0 and year%100!=0:
		print year
		add+=1
	year-=1
# --------------------3 next leap year---------------------
print "3 aage k leap year "
add1=0
var=0
year2=user+1
while var<year2:
	if add1==3:
		break
	if year2%4 ==0 and year2 %100==0 and year2%400==0:
		print year2
		add1+=1
	elif year2%4==0 and year2%100!=0:
		print year2
		add1+=1
	year2+=1
