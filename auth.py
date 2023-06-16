from firebase import Firebase
from firebase_admin import auth


class Auth():

    def __init__(self):
            user = Firebase()

    def create_user(self, email):
        user = auth.create_user(
            email=email
        )
        print('User created successfully!')
        return user.uid
    
    def sign_in(self, email):
        signed_in_user = auth.get_user_by_email(email)
        print('User signed in successfully!')
        return signed_in_user.uid

    