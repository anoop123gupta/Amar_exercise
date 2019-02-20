user=input("Enter a year to check ")
# ------------check leap year--------------------
if user%4==0 and user%100==0 and user%400==0:
	print "leap year ",user
elif user%4==0 and user%100!=0:
	print '{0} {1}'.format(user, 'leap year  hai ')
else:
	print '{0} {1}'.format(user, 'leap year nahi hai')
