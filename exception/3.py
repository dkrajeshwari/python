def cast_vote(age):
    assert age>=18,f"Age should not be less then 18,it was {age}"
    print("thank u for voting")

try:
    age =int(input("Enter the age"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print(f"you entered the valid age:{age}")
finally:
    print("end..")            
    

