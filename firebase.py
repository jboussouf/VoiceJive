import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
#import firebase

#create connection with firebase
class Firebase:

    def __init__(self):
        cred = credentials.Certificate("path/to/service_Account_Key.json")
        storage_bucket = 'voicejive.appspot.com' #application name
        firebase_admin.initialize_app(cred, {'storageBucket': storage_bucket})

    