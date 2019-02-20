# user=int(raw_input("Give me a number "))
# a=0
# b=1
# c=0
# for i in range(user):
# 	if a%2==0:
# 		print a,
# 	c=a+b
# 	a=b
# 	b=c
# __________________________second method------------------
def fib(user):
	first_num=0
	second_num=1
	third_num=0
	var=0
	while var<user:
		if third_num%2==0:
			print third_num
		third_num=first_num+second_num
		first_num=second_num
		second_num=third_num
		var+=1
user=int(raw_input("Give me a number "))
fib(user)