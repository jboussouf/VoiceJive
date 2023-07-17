import firebase_admin
from firebase_admin import credentials, storage


class FirebaseStorageManager:
    def __init__(self):
        self.bucket = storage.bucket()

    def upload_audio_file(self, file_path, destination_path):
        blob = self.bucket.blob(destination_path)
        blob.upload_from_filename(file_path)
        blob.make_public()
        url = blob.public_url
        print(url)
        return url

    def get_audio_url(self, file_path):
        blob = self.bucket.blob(file_path)
        url = blob.public_url
        return url
