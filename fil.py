def is_prime(num):
    if num<2:
        return false
    else:
        for i in range (2,num//2+1):
            if num%i==0:
                return False
        return True        

nums=[i for i in range(1,200)]
lst=list(filter(lambda i : i% 5==0,nums))
print(lst)
