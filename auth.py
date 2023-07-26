from firebase import Firebase
from firebase_admin import auth
from firebase_admin import firestore


# create and sign in to an account on firebese with fire base auth and firebase firestor
class Auth():

    def __init__(self):
        user = Firebase()

    def create_user(self, email, userName):
        # Create the user
        user = auth.create_user(
            email=email
        )

        # Store additional user information in the database
        user_data_0 = {
            'email': user.email,
            'userName': userName,
            'uid': user.uid,
            'friends' : {},
            'posts' : []
        }

        # Save the user data to the database
        db = firestore.client()
        db.collection('users').document(user.uid).set(user_data_0)

        return user.uid
    
    def sign_in(self, email):
        signed_in_user = auth.get_user_by_email(email)
        print('User signed in successfully!')
        return signed_in_user.uid


    