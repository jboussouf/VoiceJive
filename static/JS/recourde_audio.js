let mediaRecorder;
let recordedChunks = [];

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function(stream) {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.addEventListener('dataavailable', function(e) {
                recordedChunks.push(e.data);
            });
            mediaRecorder.start();
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;
            document.getElementById('sendBtn').disabled = true;
        });
}

function stopRecording() {
    mediaRecorder.stop();
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
    document.getElementById('sendBtn').disabled = false;
}

function sendAudio() {
    const captionInput = document.getElementById('mycaption');
    const captionValue = captionInput.value;

    const blob = new Blob(recordedChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('audio', blob, 'recording.wav');
    formData.append('caption', captionValue);

    fetch('/save-audio', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        console.log('Audio sent successfully!');
        window.location.href = '/index';
    })
    .catch(function(error) {
        console.error('Error sending audio:', error);
    });
}

// great!


