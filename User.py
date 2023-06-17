from firebase import Firebase
from post import Post
from firebase_admin import firestore

class User():

    def __init__(self, uid):
        self.uid = uid
        self.posts = []
        self.friend = []

    def create_post(self, content):
        post = Post(content)
        self.posts.append(post)
        db = firestore.Client()
        
        print("post added !")

    def get_posts(self):
        return self.posts

    def like_post(self, post):
        post.add_like(self)

    def comment_on_post(self, post, comment):
        post.add_comment(self, comment)

    def get_feed(self):
        # Retrieve and return the user's feed from the Firebase store
        return self.store.get_feed(self)
