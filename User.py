from firebase import Firebase
from post import Post
from firebase_admin import firestore
from audio import FirebaseStorageManager

class User():

    def __init__(self, uid):
        self.uid = uid
        self.posts = []
        self.friend = []
        

    def create_post(self, content):
        db = firestore.client()
        doc_ref = db.collection('users').document(self.uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        self.posts = doc_data["posts"]

        manager = FirebaseStorageManager()
        destination_path = self.uid+'/audio'+str(len(self.posts))+'.mp3'
        audio_url = manager.upload_audio_file(content["audio"], destination_path)

        
        if doc_snapshot.exists:
            content["audio"] = 'audio'+str(len(self.posts))+'.mp3'
            doc_data["posts"].append(content)
            db.collection('users').document(self.uid).set(doc_data)
        else:
            print("Document does not exist.")
        
        print("post added !")

    def get_posts(self):
        db = firestore.client()
        doc_ref = db.collection('users').document(self.uid)
        doc_snapshot = doc_ref.get()
        doc_data = doc_snapshot.to_dict()
        #print(doc_data)
        return self.posts
    
    def getOnePost(self, idPost):
        db = firestore.client()
        # Specify the collection and query
        collection_ref = db.collection('users')
        query_ref = collection_ref.where('posts', '==', 'value')

        # Retrieve the documents that match the query
        docs = query_ref.get()

        # Iterate over the documents
        for doc in docs:
            # Access document fields
            print(f'Document ID: {doc.id}')
            print(f'Document Data: {doc.to_dict()}')

        return post



        return post

    def like_post(self, post):
        # we need add here the post ID in order to recognize which post the user wants to like
        post.add_like(self)

    def comment_on_post(self, post, comment):
        # we need add here the post ID in order to recognize which post the user wants to comment
        post.add_comment(self, comment)

