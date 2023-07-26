from firebase import Firebase
from post import Post
from firebase_admin import firestore
from audio import FirebaseStorageManager
from firebase_admin import auth
from datetime import datetime

#return document of the user
def get_ref(user_id):
    db = firestore.client()
    doc_ref = db.collection('users').document(user_id)
    
    return doc_ref

#return list of posts of a user 
def get_posts(uid):
        doc_ref = get_ref(uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        return doc_data['posts']
#return the account user name
def get_UserName(uid):
        doc_ref = get_ref(uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        return doc_data['userName']

#return all posts in a database
def getAll_posts():
        posts = []
        list_users = auth.list_users().users
        for item in list_users:
            user_posts = get_posts(item.uid)
            userName = get_UserName(item.uid)
            if len(user_posts) == 0:
                 continue
            else:
                for subItem in user_posts:
                    posts.append((userName, subItem))
        return posts

#return list of friends of a user
def get_friend(uid):
    doc_ref = get_ref(uid)
    doc_snapshot = doc_ref.get()
    doc_data = doc_snapshot.to_dict()
    return doc_data['friends']

#get the last msg between user and all friends
def last_msg(uid, key):
    doc_ref = get_ref(uid)
    doc_snapshot = doc_ref.get()
    doc_data = doc_snapshot.to_dict()
    return doc_data['friends'][key]["messenger"][-1]

#return all messages
def all_msgs(uid, key):
    doc_ref = get_ref(uid)
    doc_snapshot = doc_ref.get()
    doc_data = doc_snapshot.to_dict()
    return doc_data['friends'][key]["messenger"]
#return all friends
def get_all_friends(uid):
    friend = get_friend(uid)
    friends_userNames = []
    for key in friend.keys():
        msg=last_msg(uid, key).split('/')
        friends_userNames.append([key, get_UserName(key), msg[0], msg[-1]])
    return friends_userNames
#get the users how are not friends of a user
def not_friends(uid):
    list_users = auth.list_users().users
    all_friends = get_all_friends(uid)
    friends_uid = [uid]
    for item in all_friends:
        friends_uid.append(item[0])
    all_users = []
    for item in list_users:
        all_users.append(item.uid)
    not_friend = [user for user in all_users if user not in friends_uid]
    return [(userID, get_UserName(userID)) for userID in not_friend]

#create post or add friend to the list of friends send messages to friends
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

        content['date'] = datetime.now().strftime("%B %d, %Y")
        
        manager = FirebaseStorageManager()
        destination_path = self.uid+'/audio'+str(len(self.posts))+'.mp3'
        audio_url = manager.upload_audio_file(content["audio"], destination_path)
        storgeUrl = "https://storage.googleapis.com/voicejive.appspot.com/"
        print(audio_url)
        
        if doc_snapshot.exists:
            content["audio"] = storgeUrl+self.uid+'/audio'+str(len(self.posts))+'.mp3'
            doc_data["posts"].append(content)
            db.collection('users').document(self.uid).set(doc_data)
        else:
            print("Document does not exist.")
        
        print("post added !")
  
    
    def add_friend(self, friendID):
        db = firestore.client()

        # add friend to the user list
        me_ref = db.collection('users').document(self.uid)
        doc_snapshot = me_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][friendID] = {"messenger": [" /Say hello"]}
        me_ref.set(doc_data)

        # add user to the frind list
        friend_ref = db.collection('users').document(friendID)
        doc_snapshot = friend_ref.get()
        doc_data = doc_snapshot.to_dict()
        doc_data["friends"][self.uid] = {"messenger": [" /Say hello"]}
        friend_ref.set(doc_data)

        print("the frind is added !")
    
    def send_msg(self, friendID, msg):
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
        #print(doc_data)
        return doc_data

