from User import Users
"""Requirements:
method allowing users to create posts
any neccessary instance properties/data structures
class variable storing posts from all users, data structure?
Info stays in sync
Bonus: Method for deleting a post, info stays in sync"""

def test_post_method():
    user1=Users("Jesse")
    user1.createpost("My post")
    assert print(Users.posts)=={"Jesse":"my post"}
    
def test_overwrite_post():
    user1=Users("Jesse")
    user1.createpost("My post")
    user1.createpost("My second post")
    assert print(Users.posts)=={"Jesse":"My second post"}

def test_delete_post_method():
    user1=Users("Jesse")
    user1.createpost("My post")
    user1.deletepost("Jesse")
    assert print(Users.posts)=={}
    