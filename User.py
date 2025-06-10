class User:
    
    def __init__(self, name: str, email: str, license: int):
        self.name = name
        self.email = email
        self.license = license
    def emailer(self):
        print( f"Loading.........{self.name} just sent an email using his email {self.email}!")
    
    def send_message(self,message):
        print( f"{self.name} typed {message} in the chat.")
    
    def logging_off(self):
        print( f"User is logging off....See you soon!")
    
    def __str__(self):
        return f"User: {self.name}  Email: {self.email[0:2]}...{self.email[-3::]}"
    def __repr__(self):
        return f"Usr: {self.name}"
    

usr1 = User("Charlie", "cw@gmail.com", 1247392)

usr2 = User("Eric", "eric_is_funny@hotmail.com", 993453)

print(usr1)

arr = [usr1, usr2]
print(arr)
