
# VoiceJive

Share Your Voice: appliction for sharing your ideas as an audio

This work introduces a Flask-based social media application using Firebase for idea sharing and user interaction. Users can share thoughts through voice recordings with captions, fostering meaningful online interactions. The application includes user management, post creation, friend connections, and a user-friendly interface. Flask and Firebase enable seamless integration, real-time data synchronization, secure authentication, and efficient storage. This work contributes to enhancing social media platforms by providing an interactive medium for idea sharing and improving user experiences.




![Logo](https://github.com/jboussouf/VoiceJive/blob/main/media/voicejive.png?raw=true)

In this project, we leveraged Flask, a powerful web framework, to develop an innovative social media application centered around audio posts. Our primary focus was on enabling seamless communication between friends through the exchange of messages.

To store user information efficiently, we opted to work with NoSQL databases, and specifically integrated Firebase Firestore into our system.

Moreover, to handle the storage of audio files, we seamlessly integrated Firebase Storage into our application. This cloud-based storage solution allowed us to securely save and manage audio posts uploaded by users, ensuring their accessibility and reliability.


## Installation

To use the application, you must first go to firebase and generate the json key file, then add it to the application.

./firebase.py:
```py 
  ../
  credentials.Certificate("path/to/service_Account_Key.json")
  ../
```


Run on the teminal:
```bash
    source ./flaskiii/bin/activate
    python VoiceJive.py

```

## Authors

- [@jboussouf](https://github.com/jboussouf)

- [@iseddik](https://github.com/iseddik)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jboussouf/)
