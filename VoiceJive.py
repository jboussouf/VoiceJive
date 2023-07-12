from User import User
from auth import Auth
from flask import Flask, render_template, request, redirect, session, url_for
from post import Post

app = Flask(__name__)
app.secret_key = 'secured_session'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST' and request.form.get('email', None) != None:
        session['email'] = request.form.get('email', None)
        auth = Auth()
        session['UID'] = auth.sign_in(session['email'])
        print(session['UID'])
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    if session.get('UID', None) != None:
        return render_template('index.html')
    return render_template('login.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_file.save('./recording.wav')

        caption = request.form['caption']
        print(caption)
    user = User(session['UID'])
    user.create_post({'audio': './recording.wav', 'caption':caption})
    return redirect('/index')


@app.route('/newPost', methods=['POST'])
def newPost():
    return render_template('newPost.html')


if __name__ == '__main__':
    app.run(debug=True)
