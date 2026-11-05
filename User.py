class Users():
    posts = {}
    
    def createpost(self, new_post):
        Users.posts[self.user_name]=new_post
    
    def deletepost(self):
        del Users.posts[self.user_name]
    
    
        
        
    def __init__(self, user_name, email, password):
        self.user_name=user_name
        self.email = email
        self.password = password
    def __str__(self):
        return f"{self.user_name} is there"

class FreeUser(Users):
    def __init__(self, user_name, email, password, privileges="read-only"):
        super().__init__(user_name, email, password)
        self.privileges=privileges
    
class PremiumUser(Users):
    def __init__(self, user_name, email, password, privileges="CRUD"):
        super().__init__(user_name, email, password)
        self.privileges=privileges


free_user1=FreeUser("James", "imjames@gmail.com", "password")

print(free_user1.email)

# your User class goes here