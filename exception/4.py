class MaxLimitError(Exception):

    def __init__(self,message):
        self.message=message

    def __str__(self):
         return f"{self.__class__.__name__}:{self.message}"

c=0
def login(username,password):
    global c
    if username=="abc" and password=="cba":
        print("login is successfull")
    else:
        print(f"Bad credencials")
    c+=1
    if c>5:
        raise MaxLimitError("you have reached maximum attempts")

login("abc","CBA")
login("a","CA")
login("ABC","C")
login("abc","cba")


