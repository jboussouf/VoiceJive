import firebase_admin
from firebase_admin import credentials, firestore

class Firebase:
    def __init__(self):
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    def add_data(self, collection_name, document_data):
        db = firestore.client()
        collection_ref = db.collection(collection_name)
        collection_ref.add(document_data)
        print('Data added successfully!')