from User import Users
"""Requirements:
method allowing users to create posts
any neccessary instance properties/data structures
class variable storing posts from all users, data structure?
Info stays in sync
Bonus: Method for deleting a post, info stays in sync"""

def test_post_method():
    user1=Users("Jesse", "nobody21@yahoo.com", "password", 21, 1234567890, 3605085006, "John", "Doe", "02/29/2006")
    user1.createpost("My post")
    assert print(Users.posts)=={"Jesse":"my post"}
    
def test_overwrite_post():
    user1=Users("Jesse", "nobody21@yahoo.com", "password", 21, 1234567890, 3605085006, "John", "Doe", "02/29/2006")
    user1.createpost("My post")
    user1.createpost("My second post")
    assert print(Users.posts)=={"Jesse":"My second post"}

def test_delete_post_method():
    user1=Users("Jesse", "nobody21@yahoo.com", "password", 21, 1234567890, 3605085006, "John", "Doe", "02/29/2006")
    user1.createpost("My post")
    user1.deletepost("Jesse")
    assert print(Users.posts)=={}
    