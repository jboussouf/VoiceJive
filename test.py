from auth import Auth
from user import User 
from firebase_admin import firestore, credentials
import firebase_admin


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

auth = Auth()
"""
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com',
    'informations':{
        'job':['AI', 'ML', 'LLM'],
        'socity':'IBM',
        'experience':15
    }
}
user.add_data("users.name",data)"""

uid = auth.sign_in("sedissam@gmail.com")

# Create a Firestore client
db = firestore.Client()

# Access the Firestore document for the user
user_doc_ref = db.collection('users').document(uid)

# Retrieve the user document
user_doc = user_doc_ref.get()

# Check if the document exists
if user_doc.exists:
    # Get the user data as a dictionary
    user_data = user_doc.to_dict()
    
    # Print or use the user data
    print(user_data)
else:
    print("User document does not exist.")


