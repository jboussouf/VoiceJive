from firebase import Firebase
from post import Post
from firebase_admin import firestore
from audio import FirebaseStorageManager
from firebase_admin import auth

def get_ref(user_id):
    db = firestore.client()
    doc_ref = db.collection('users').document(user_id)
    
    return doc_ref

def get_posts(uid):
        doc_ref = get_ref(uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        return doc_data['posts']

def getAll_posts():
        posts = []
        list_users = auth.list_users().users
        for item in list_users:
            user_posts = get_posts(item.uid)
            if len(user_posts) == 0:
                 continue
            else:
                for subItem in user_posts:
                    posts.append(subItem)
        print(len(posts))
        return posts

class User():

    def __init__(self, uid):
        self.uid = uid
        self.posts = []
        self.friend = []
        self.messenger = {}

    def create_post(self, content):
        db = firestore.client()
        doc_ref = db.collection('users').document(self.uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        self.posts = doc_data["posts"]

        manager = FirebaseStorageManager()
        destination_path = self.uid+'/audio'+str(len(self.posts))+'.mp3'
        audio_url = manager.upload_audio_file(content["audio"], destination_path)
        storgeUrl = "https://storage.googleapis.com/socialsphere-6841e.appspot.com/"
        print(audio_url)
        
        if doc_snapshot.exists:
            content["audio"] = storgeUrl+self.uid+'/audio'+str(len(self.posts))+'.mp3'
            doc_data["posts"].append(content)
            db.collection('users').document(self.uid).set(doc_data)
        else:
            print("Document does not exist.")
        
        print("post added !")
  
    
    def add_friend(self, friend):
        friendID = friend.uid
        db = firestore.client()

        # add friend to the user list
        me_ref = db.collection('users').document(self.uid)
        doc_snapshot = me_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][friendID] = {"messenger": []}
        me_ref.set(doc_data)

        # add user to the frind list
        friend_ref = db.collection('users').document(friendID)
        doc_snapshot = friend_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][self.uid] = {"messenger": []}
        friend_ref.set(doc_data)

        print("the frind is added !")
    
    def send_msg(self, friend, msg):
        friendID = friend.uid
        db = firestore.client()

        # add msg to user messanger list
        me_ref = db.collection('users').document(self.uid)
        doc_snapshot = me_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][friendID]["messenger"].append("me/" + msg)
        me_ref.set(doc_data)

        # add msg to friend messanger list
        friend_ref = db.collection('users').document(friendID)
        doc_snapshot = friend_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][self.uid]["messenger"].append("friend/" + msg)
        friend_ref.set(doc_data)

        print("The friend's messenger list is updated!")

    def like_post(self, post):
        # we need add here the post ID in order to recognize which post the user wants to like
        post.add_like(self)

    def comment_on_post(self, post, comment):
        # we need add here the post ID in order to recognize which post the user wants to comment
        post.add_comment(self, comment)

    def user_to_dict(self, user_id):
        db = firestore.client()
        doc_ref = db.collection('users').document(user_id)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        print(doc_data)
        return doc_data

