from auth import Auth
from user import User 
from audio import FirebaseStorageManager

# Create an instance of the FirebaseStorageManager class
manager = FirebaseStorageManager('./serviceAccountKey.json', 'socialsphere-6841e.appspot.com')

# Upload an MP3 file and get the URL
file_path = 'audio.wav'
destination_path = 'audio_files/audio1.mp3'
audio_url = manager.upload_audio_file(file_path, destination_path)
print("Audio URL:", audio_url)

# Get the URL of an existing MP3 file
file_path = 'audio_files/audio1.mp3'
audio_url = manager.get_audio_url(file_path)
print("Audio URL:", audio_url)




