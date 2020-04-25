def odd_numbers(n):
	return [x for x in range(0,n+1) if x%2!=0]
print(odd_numbers(9))

def odd_numbers(n):
	return [x*x for x in range(0,n+1)]
print(odd_numbers(9))

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newlist= []
for name in filenames:
    exte = name.split('.')[1] 
    if(exte == 'hpp'):
        exte = 'h'
    n1 = '{}.{}'.format(name.split('.')[0], exte)
    newlist.append(n1)
   
print(newlist)


