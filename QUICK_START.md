# Quick Start Guide - Audio Upload Feature

## 🚀 Get Started in 3 Minutes

### Step 1: Start the Backend (30 seconds)

```bash
cd e:\NIRMAN_INTERNSHIP_TASK-main.worktrees\agents-audio-upload-speech-to-text-feature
python app.py
```

**Expected output:**
```
Initializing rubric parser...
Initializing scoring engine...
API ready!
Initializing speech recognizer...
================================================================================
Starting Communication Skills Scoring API...
API will be available at: http://localhost:5000
================================================================================

 * Running on http://127.0.0.1:5000
```

### Step 2: Open the Frontend (10 seconds)

Open your browser and go to:
```
http://localhost:5000
```

### Step 3: Test Audio Upload (60 seconds)

#### Option A: Upload Your Own Audio
1. Click the **🎤 Upload Audio** tab
2. Prepare an audio file (MP3, WAV, M4A, etc.) of a self-introduction
3. Drag the file onto the upload area, or click to browse and select
4. Wait for the green ✓ message: "Audio transcribed successfully!"
5. Optionally enter the audio duration
6. Click **"Score and generate video"**
7. See the results and generated video!

#### Option B: Create a Sample Audio (Advanced)

If you want to test without a real audio file, you can create a simple WAV file:

```python
import wave
import struct

# Create a sample WAV file with silence (for testing file handling)
filename = "sample.wav"
with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)      # Mono
    wav_file.setsampwidth(2)       # 2 bytes per sample
    wav_file.setframerate(16000)   # 16kHz
    
    # Write 3 seconds of silence (as test)
    silence = struct.pack('h' * 16000 * 3, *[0] * (16000 * 3))
    wav_file.writeframes(silence)
```

---

## 📋 Feature Overview

### What's New

| Feature | Description |
|---------|-------------|
| **Upload Audio** | Drag-and-drop or click to upload audio files |
| **Auto Transcription** | Converts audio to text automatically |
| **Supported Formats** | MP3, WAV, M4A, WebM, OGG, FLAC, AAC |
| **Progress Tracking** | Real-time progress bar during upload/transcription |
| **Error Handling** | Clear error messages if something goes wrong |
| **Smart Integration** | Transcribed text integrates seamlessly with scoring |

### What Stays the Same

- ✅ All existing scoring functionality
- ✅ Rubric system
- ✅ Video generation
- ✅ Results display
- ✅ Text input mode (still available)

---

## 🔧 For Developers

### Run Tests

Verify everything is working:

```bash
python test_api.py
```

Expected output:
```
✓ Basic API tests passed!
```

### Test Transcribe Endpoint

```python
import requests

# Test 1: No file
response = requests.post('http://localhost:5000/api/transcribe')
print(response.json())  # Should show error

# Test 2: With file
with open('audio.mp3', 'rb') as f:
    files = {'audio': f}
    response = requests.post(
        'http://localhost:5000/api/transcribe',
        files=files
    )
    print(response.json())  # Should show transcript
```

### Debug Mode

The backend runs in debug mode with:
- Auto-reloading on code changes
- Detailed error messages
- Request logging

---

## 📝 Manual Testing Checklist

Test these scenarios:

### ✅ Valid Audio
- [ ] Upload MP3 file → Transcript appears
- [ ] Upload WAV file → Transcript appears
- [ ] Upload M4A file → Transcript appears
- [ ] Drag-and-drop → Works same as clicking

### ✅ Invalid Inputs
- [ ] No file selected → Error message
- [ ] Unsupported format (.mov, .flv) → Error message
- [ ] File > 50MB → Error message
- [ ] Corrupted audio → Error message
- [ ] Empty audio → Error message

### ✅ UI/UX
- [ ] Tab switching works smoothly
- [ ] Progress bar animates
- [ ] Status messages appear in real-time
- [ ] Score button enables/disables correctly
- [ ] Auto-scroll to results works
- [ ] Mobile responsive

### ✅ Integration
- [ ] Transcribed text can be scored
- [ ] Video still generates
- [ ] Results display correctly
- [ ] Can clear and upload again
- [ ] Can switch to text mode after upload

---

## 🐛 Troubleshooting

### Backend Won't Start
```
Error: Failed to import speech_recognition
```
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Audio Upload Fails
```
Error: "Could not extract text from audio"
```
**Solutions:**
- Try a different audio file (clearer quality)
- Ensure audio is in English
- Check internet connection
- Reduce background noise

### File Too Large
```
Error: "Audio file too large. Maximum size: 50MB"
```
**Solution:** Use a smaller audio file or modify MAX_AUDIO_SIZE in app.py

### Transcription Takes Too Long
**Solutions:**
- Check internet speed
- Try shorter audio file
- Wait longer (can take 10-20 seconds for long audio)

---

## 📚 Documentation

For more information, see:
- **`AUDIO_FEATURE.md`** - Comprehensive feature documentation
- **`IMPLEMENTATION_SUMMARY.md`** - Technical implementation details
- **`README.md`** - Original project documentation

---

## 💡 Tips

### Best Practices for Audio Files
1. **Clear audio** - Minimize background noise
2. **Normal volume** - Not too quiet, not too loud
3. **English language** - Currently English only
4. **MP3 format** - Most compatible format
5. **Under 5 minutes** - Faster processing
6. **Good microphone** - Better recognition

### Performance Tips
1. Use MP3 format (more efficient than WAV)
2. Keep audio under 5 minutes
3. Upload during off-peak hours
4. Check internet connection
5. Close other applications for resources

---

## 🎯 Next Steps

### After Testing
1. ✅ Verify feature works end-to-end
2. ✅ Test with different audio files
3. ✅ Try both upload and text modes
4. ✅ Generate videos successfully
5. ✅ Review transcription accuracy

### Deployment
For production deployment:
1. See `DEPLOYMENT.md` (original project)
2. Add rate limiting for API
3. Set up file cleanup schedule
4. Monitor Google API usage
5. Configure HTTPS for uploads

---

## 📞 Support

If you encounter issues:

1. **Check error message** - Usually explains the problem
2. **Verify file format** - Use MP3/WAV
3. **Test API** - Run `python test_api.py`
4. **Check backend** - Verify `http://localhost:5000/api/health` returns 200
5. **Review documentation** - See AUDIO_FEATURE.md

---

## 🎉 You're All Set!

The audio upload feature is fully integrated and ready to use. 

**To summarize:**
- ✅ Upload audio files (MP3, WAV, M4A, etc.)
- ✅ Automatic speech-to-text conversion
- ✅ Seamless scoring integration
- ✅ Beautiful UI with progress tracking
- ✅ Comprehensive error handling

**Questions?** See the documentation files or test the API directly!

---

**Happy coding! 🚀**
