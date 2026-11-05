class Users():
    posts = {}
    
    def createpost(self, post_title, post_content):
        Users.posts[post_title]=post_content
    
    def deletepost(self, post_title):
        del Users.posts[post_title]
    
    
        
        
    def __init__(self, user_name, email, password):
        self.user_name=user_name
        self.email = email
        self.password = password
    def __str__(self):
        return f"{self.user_name} is there"

class FreeUser(Users):
    def __init__(self, user_name, email, password, privileges="read-only", post=0):
        super().__init__(user_name, email, password)
        self.privileges=privileges
        self.post=post
    
    def createpost(self, post_title, post_content):
            if self.post==2:
                print("You have reached your max post limit on the free plan. Delete a post to add another, or get the premium user plan to make as many posts as you want!")
                return "You have reached your max post limit on the free plan. Delete a post to add another, or get the premium user plan to make as many posts as you want!"
            else:
                Users.posts[post_title]=post_content
                self.post+=1
                print("You've added a post! Print User.posts to see your post!")
                return "You've added a post! Print User.posts to see your post!"
    
    def deletepost(self, post_title):
            del Users.posts[post_title]
            self.post-=1
    
        
    
class PremiumUser(Users):
    def __init__(self, user_name, email, password, privileges="CRUD"):
        super().__init__(user_name, email, password)
        self.privileges=privileges


free_user1=FreeUser("James", "imjames@gmail.com", "password")

print(free_user1.post)
free_user1.createpost("New account", "I made an account!")
print(Users.posts)
free_user1.createpost("My second post", "I posted a 2nd post!")
print(Users.posts)
free_user1.createpost("My third post", "Can I add this?")
print(Users.posts)

# your User class goes here