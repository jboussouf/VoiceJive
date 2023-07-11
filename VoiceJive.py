from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = request.form.get('email', None)
        if email != None:
            return render_template('index.html')
    return render_template('login.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_file.save('./recording.wav')

        caption = request.form['caption']
        print(caption)
    return redirect('/index')


@app.route('/newPost', methods=['POST'])
def newPost():
    return render_template('newPost.html')


if __name__ == '__main__':
    app.run(debug=True)
