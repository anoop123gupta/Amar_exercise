user=raw_input(" Enter String ")
a=user[-3:]
if user[-2:] =='ly':
    print user
elif a!='ing':
    print user+'ing'
elif a=='ing':
    print user+'ly'