import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
#import firebase



class Firebase:

    def __init__(self):
        cred = credentials.Certificate("./serviceAccountKey.json")
        storage_bucket = 'socialsphere-6841e.appspot.com'
        firebase_admin.initialize_app(cred, {'storageBucket': storage_bucket})

    """
    def add_data(self, collection_name, document_data):
        db = firestore.client()
        collection_ref = db.collection(collection_name)
        collection_ref.add(document_data)
        print('Data added successfully!')"""
    

    
    def save_post(self, post):
        # Save the post to the Firebase database
        pass

    def get_feed(self, user):
        # Retrieve and return the user's feed from the Firebase database
        pass

    