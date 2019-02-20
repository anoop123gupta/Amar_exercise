user=int(raw_input("number "))
add=0
sum_of_digits=0
for i in range(user+1):
	add=add+i**2
	sum_of_digits=sum_of_digits+i
	sqr_of_sum_digits=sum_of_digits**2
print 'add of each digits sqr' , add
print 'sqr_of_sum_digits', sqr_of_sum_digits
print  'answer is ' ,sqr_of_sum_digits - add