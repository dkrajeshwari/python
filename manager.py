from car import Car
car1=Car("KA0176",4)
car2=Car("KA0176",4)
car3=Car("KA0176",4)
car4=Car("KA0176",4)
car5=Car("KA0176",4)
car1.start()
car2.start()
car3.start()
car4.start()
car5.start()
car1.change_gear()
car2.change_gear()
car3.change_gear()
car4.change_gear()
car5.change_gear()
lst =[car1,car2,car3,car4,car5]
for i in lst:
    i.showInfo()
c=len(list(filter(lambda x:x.is_started and  x.c_gear==0,lst)))
print(c)    
