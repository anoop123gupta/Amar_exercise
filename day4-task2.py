dic={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
user=raw_input("Enter words- number in a sequence ")
b = user.split()
add=0
for i in b:
	add = add + dic[i]
print add