n=int(input('enter the number : '))
temp=n
count=0
while (temp>0):
	count=count+1
	temp=temp//10
print('\ngiven number     = ',n)
print('\nnumber of digits = ',count)