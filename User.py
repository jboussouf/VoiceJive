from firebase import Firebase
from post import Post
from firebase_admin import firestore

class User():

    def __init__(self, uid):
        self.uid = uid
        self.posts = []
        self.friend = []
        

    def create_post(self):
        
        content = None
        post = Post(content)
        self.posts.append(post)
        db = firestore.client()
        doc_ref = db.collection('users').document(self.uid)
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            doc_data = doc_snapshot.to_dict()
            doc_data["posts"].append(content)
            db.collection('users').document(self.uid).set(doc_data)
            print(doc_data)
        else:
            print("Document does not exist.")
        
        print("post added !")

    def get_posts(self):
        return self.posts

    def like_post(self, post):
        post.add_like(self)

    def comment_on_post(self, post, comment):
        post.add_comment(self, comment)

