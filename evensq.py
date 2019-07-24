from functools import reduce

lst=[1,2,3,4,5,6,7,8,9,10]
x=list(map(lambda x:x**2,lst))
print(x)
y=list(filter(lambda x:x%2==0,x))
print(y)
z=reduce(lambda a,b:a+b,y)
print(z)