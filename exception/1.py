try:
    num2=int(input("Enter the number"))
    num1=int(input("Enter the number"))
    print(num1**num2)
    print(num1/num2)
    print("sum is:"+num1+num2)
except ZeroDivisionError:
    print(f"num2 cant be zero")
except ValueError:
    print(f"Please enter numbers only")
except Exception as e:
    print(f"Something went wrong {e}")            