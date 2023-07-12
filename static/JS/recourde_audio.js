let mediaRecorder;
let recordedChunks = [];
let audio_file;
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
            document.getElementById('select_audio').disabled = true;
        });
}

function stopRecording() {
    mediaRecorder.stop();
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
    document.getElementById('sendBtn').disabled = false;
}

function select_audio() {
    let select_audio = document.createElement('input');
    select_audio.setAttribute('type', 'file');
    select_audio.setAttribute('name', 'audio');
    select_audio.setAttribute('accept', 'audio/*');
    select_audio.addEventListener('change', function(event) {
      var selectedFile = event.target.files[0];
      if (selectedFile) {
        document.getElementById('startBtn').disabled = true;
        document.getElementById('select_audio').disabled = true;
        document.getElementById('sendBtn').disabled = false;
        audio_file = select_audio.files[0];
      } else {
        console.log('Audio file not selected yet');
      }
    });
    select_audio.click();
  }

  function sendAudio() {
    const captionInput = document.getElementById('mycaption');
    const captionValue = captionInput.value;
    const formData = new FormData();
  
    if (recordedChunks.length !== 0) {
      const blob = new Blob(recordedChunks, { type: 'audio/*' });
      formData.append('audio', blob, 'recording.wav');
    } else if (audio_file) {
      formData.append('audio', audio_file);
    } else {
      console.error('No audio file available');
      return;
    }
  
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


