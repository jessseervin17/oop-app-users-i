class Users():
    posts = {}
    
    def createpost(self, new_post):
        Users.posts[self.user_name]=new_post
    
    def deletepost(self):
        del Users.posts[self.user_name]
    
    
        
        
    def __init__(self, user_name, email, password, age, SSN, phone, first_name, last_name, DOB):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.age = age
        self.SSN = SSN
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
    def __str__(self):
        return f"{self.user_name} is there"

user_1 = Users("nobody", "nobody21@yahoo.com", "password", 21, 1234567890, 3605085006, "John", "Doe", "02/29/2006")

user_2 = Users("nobody2", "nobody22@yahoo.com", "password1234", 25, 1987654321, 3605085007, "Jane", "Doe", "02/29/2006")

user_3 = Users("nobody3", "nobody33@yahoo.com", "password1234567890", 30, 1122334455, 3605085008, "Bob", "Smith", "02/29/2006")



# your User class goes here