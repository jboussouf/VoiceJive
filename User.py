from firebase import Firebase
from post import Post

class User():

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.store = Firebase()
        self.posts = []

    def create_post(self, content):
        post = Post(content)
        self.posts.append(post)
        self.store.save_post(post)

    def get_posts(self):
        return self.posts

    def like_post(self, post):
        post.add_like(self)

    def comment_on_post(self, post, comment):
        post.add_comment(self, comment)

    def get_feed(self):
        # Retrieve and return the user's feed from the Firebase store
        return self.store.get_feed(self)
