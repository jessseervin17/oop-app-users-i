from User import Users, FreeUser, PremiumUser
"""Requirements:
method allowing users to create posts
any neccessary instance properties/data structures
class variable storing posts from all users, data structure?
Info stays in sync
Bonus: Method for deleting a post, info stays in sync"""

def test_post_method():
    user1=FreeUser("Jesse", "nobody21@yahoo.com", "password")
    user1.createpost("My post", "Content")
    assert Users.posts=={"My post":"Content"}
    
def test_no_overwrite_post():
    user1=FreeUser("Jesse", "nobody21@yahoo.com", "password")
    user1.createpost("My post", "Content")
    user1.createpost("My second post", "More Content")
    assert Users.posts=={"My post":"Content", "My second post":"More Content"}

def test_delete_post_method():
    user1=FreeUser("Jesse", "nobody21@yahoo.com", "password")
    user1.deletepost("My post")
    user1.deletepost("My second post")
    assert Users.posts=={}

def test_multiple_posts():
    user1=FreeUser("Jesse", "nobody21@yahoo.com", "password")
    user2 = FreeUser("Josiah", "nobody22@yahoo.com", "password1234")
    user1.createpost("My post", "Content")
    user2.createpost("Now my post", "My Content")
    assert Users.posts=={"My post":"Content", "Now my post": "My Content"}

def test_multiple_posts_with_delete():
    user1=FreeUser("Jesse", "nobody21@yahoo.com", "password")
    user2 = PremiumUser("Josiah", "nobody22@yahoo.com", "password1234")
    user1.createpost("My post", "Content")
    user2.createpost("Now my post", "More Content")
    user1.deletepost("My post")
    assert Users.posts=={"Now my post":"More Content"}

def test_free_user():
    free_user1=FreeUser("James", "gmail.com", "password")
    assert free_user1.privileges == "read-only"
    assert free_user1.email=="gmail.com"

def test_premium_user():
    premium_user1=PremiumUser("James", "atmail.com", "12345")
    assert premium_user1.privileges=="CRUD"
    assert premium_user1.password=="12345"


def test_free_post_limit():
    free_user2=FreeUser("Jonah", "jonah@thewhale.com", "fishstink123")
    free_user2.createpost("Post1", "Content")
    free_user2.createpost("Post2", "More Content")
    post = free_user2.createpost("Post3", "Can I post this?")
    assert post == "You have reached your max post limit on the free plan. Delete a post to add another, or get the premium user plan to make as many posts as you want!"

def test_free_post():
    free_user2=FreeUser("Jonah", "jonah@thewhale.com", "fishstink123")
    post=free_user2.createpost("Post1", "More Content")
    assert post == "You've added a post! Print User.posts to see your post!"



    