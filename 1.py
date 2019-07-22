import random as rn
num=rn.randint(1,6)
count=0
while True:
   inp_num=int(input(Enter the number"))
   if inp_num==num:
      count+=1
      print(f"you guessed number in (count)attempts")
      break
    elif inp_num<num:
       printf("Guessed number is less than actual number")
       count+=1
    else:
       print("gussed number is more then actual number")
       count+=1
    if count==3:
       print(Better luck next time")
       break



