from User import Users, FreeUser, PremiumUser
"""Requirements:
method allowing users to create posts
any neccessary instance properties/data structures
class variable storing posts from all users, data structure?
Info stays in sync
Bonus: Method for deleting a post, info stays in sync"""

def test_post_method():
    user1=Users("Jesse", "nobody21@yahoo.com", "password")
    user1.createpost("My post")
    assert Users.posts=={"Jesse":"My post"}
    
def test_overwrite_post():
    user1=Users("Jesse", "nobody21@yahoo.com", "password")
    user1.createpost("My post")
    user1.createpost("My second post")
    assert Users.posts=={"Jesse":"My second post"}

def test_delete_post_method():
    user1=Users("Jesse", "nobody21@yahoo.com", "password")
    user1.createpost("My post")
    user1.deletepost()
    assert Users.posts=={}

def test_multiple_posts():
    user1=Users("Jesse", "nobody21@yahoo.com", "password")
    user2 = Users("Josiah", "nobody22@yahoo.com", "password1234")
    user1.createpost("My post")
    user2.createpost("Now my post")
    assert Users.posts=={"Jesse":"My post", "Josiah": "Now my post"}

def test_multiple_posts_with_delete():
    user1=Users("Jesse", "nobody21@yahoo.com", "password")
    user2 = Users("Josiah", "nobody22@yahoo.com", "password1234")
    user1.createpost("My post")
    user2.createpost("Now my post")
    user1.deletepost()
    assert Users.posts=={"Josiah":"Now my post"}

def test_free_user():
    free_user1=FreeUser("James", "gmail.com", "password")
    assert free_user1.privileges == "read-only"
    assert free_user1.email=="gmail.com"

def test_premium_user():
    premium_user1=PremiumUser("James", "atmail.com", "12345")
    assert premium_user1.privileges=="CRUD"
    assert premium_user1.password=="12345"


    