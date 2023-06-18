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
    const blob = new Blob(recordedChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('audio', blob, 'recording.wav');

    fetch('/save-audio', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        console.log('Audio sent successfully!');
    })
    .catch(function(error) {
        console.error('Error sending audio:', error);
    });
}
