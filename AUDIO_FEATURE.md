# Audio Upload & Speech-to-Text Feature

## Overview

The Communication Skills Scoring system now includes a complete audio upload and automatic speech-to-text transcription feature. Users can upload audio files of their self-introductions, which are automatically converted to text and scored using the existing rubric.

## Features

### 1. **Dual Input Modes**
- **📝 Paste Text Mode**: Traditional text input with optional duration
- **🎤 Upload Audio Mode**: Upload audio files for automatic transcription

### 2. **Audio Upload Capabilities**
- Supports multiple audio formats: MP3, WAV, M4A, WebM, OGG, FLAC, AAC
- Drag-and-drop support for easy file upload
- Click-to-browse file selection
- File size validation (up to 50MB)
- Visual upload progress indicator

### 3. **Automatic Transcription**
- Uses Google Speech Recognition API (free, cloud-based)
- Automatic format conversion support via pydub
- Intelligent error handling with user-friendly messages
- Real-time transcription status updates

### 4. **Seamless Integration**
- Transcribed text automatically appears in the text area
- Optional audio duration input (for WPM calculation)
- One-click scoring after transcription
- Auto-switch to results view after processing

## Technical Implementation

### Backend Changes

#### New Endpoint: `POST /api/transcribe`
```python
@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio_file():
    """
    Transcribe audio file to text using Google Speech Recognition.
    Expected: multipart form data with 'audio' file
    Returns: JSON with extracted transcript text
    """
```

**Request Format:**
```
POST /api/transcribe
Content-Type: multipart/form-data

audio: <audio file>
```

**Response Format:**
```json
{
    "status": "success",
    "transcript": "Hello everyone, my name is John. I am 15 years old...",
    "filename": "interview.mp3"
}
```

**Error Response:**
```json
{
    "error": "Audio could not be understood. Please ensure the audio is clear and in English."
}
```

#### New Import
```python
import speech_recognition as sr
```

#### New Configuration
```python
UPLOAD_FOLDER = "uploads/"
ALLOWED_AUDIO_EXTENSIONS = {'.wav', '.mp3', '.m4a', '.ogg', '.webm', '.flac', '.aac'}
MAX_AUDIO_SIZE = 50 * 1024 * 1024  # 50MB
recognizer = sr.Recognizer()
```

#### New Helper Function
```python
def transcribe_audio(file_path):
    """
    Transcribe audio file using Google Speech Recognition API.
    Returns the extracted text transcript.
    """
```

### Frontend Changes

#### New UI Components
1. **Input Tabs** - Switch between text and audio modes
2. **Audio Upload Area** - Drag-and-drop zone with file browser
3. **Progress Indicator** - Shows upload/transcription progress
4. **Status Message** - Real-time feedback on transcription status
5. **Duration Input** - Optional for audio mode

#### New JavaScript Functions
```javascript
function switchInputMode(mode)
// Switch between text input and audio upload modes

function handleAudioDragOver(e)
// Handle drag over event for audio files

function handleAudioDragLeave(e)
// Handle drag leave event

function handleAudioDrop(e)
// Handle file drop for drag-and-drop upload

async function handleAudioSelect(e)
// Process selected or dropped audio file

function clearAudioSection()
// Clear audio input and reset state
```

#### CSS Additions
- `.input-tabs` - Tab navigation styling
- `.audio-upload-area` - Drag-and-drop zone
- `.audio-progress` - Progress bar container
- `.transcription-status` - Status message display
- Responsive design for all screen sizes

## Usage Guide

### For Users

#### Upload Audio
1. Click the **"🎤 Upload Audio"** tab
2. Either:
   - Drag an audio file into the upload area, OR
   - Click the area and browse for a file
3. Wait for transcription (automatic)
4. Optionally enter the audio duration for WPM calculation
5. Click **"Score and generate video"**

#### Paste Text
1. Click the **"📝 Paste Text"** tab
2. Paste or type the transcript
3. Optionally enter duration
4. Click **"Score and generate video"**

### For Developers

#### Installation
```bash
pip install -r requirements.txt
```

#### Running the Application
```bash
python app.py
```

The API will be available at `http://localhost:5000`

#### Testing the API
```bash
python test_api.py
```

#### Transcribe Audio via API
```python
import requests

files = {'audio': open('sample.mp3', 'rb')}
response = requests.post('http://localhost:5000/api/transcribe', files=files)
print(response.json())
```

## Dependencies

### New Dependencies Added
- **SpeechRecognition** (3.10.0+) - Speech-to-text conversion
- **pydub** (0.25.1+) - Audio format handling

### Total Dependencies
See `requirements.txt` for complete list.

## File Structure

```
project/
├── app.py                      # Updated Flask app with transcribe endpoint
├── index.html                  # Updated frontend with audio UI
├── requirements.txt            # Updated with new dependencies
├── uploads/                    # Temporary audio uploads (auto-created)
├── generated_outputs/          # Generated videos (existing)
├── test_api.py                # API testing script (new)
├── AUDIO_FEATURE.md            # This documentation (new)
└── [other existing files]
```

## Technical Details

### Speech Recognition
- **API**: Google Cloud Speech-to-Text (free tier via SpeechRecognition library)
- **Language**: English (can be extended)
- **Supported Formats**: WAV, MP3, FLAC, OGG, WEBM, AAC
- **Error Handling**: Clear error messages for unsupported formats or unclear audio

### File Upload
- **Max Size**: 50MB (configurable)
- **Temp Storage**: Files are deleted after transcription
- **Format Validation**: Extension and MIME type checking
- **Progress Tracking**: Real-time upload progress indicator

### Performance
- **Transcription Time**: 2-10 seconds depending on audio length and quality
- **Upload Time**: 1-5 seconds for typical file sizes
- **Total Flow**: 5-20 seconds from upload to scoring
- **Caching**: No caching (fresh transcription each time)

## Error Handling

### User-Facing Errors
1. **No file selected** → "No file selected for uploading"
2. **Unsupported format** → "Unsupported audio format. Allowed formats: ..."
3. **File too large** → "Audio file too large. Maximum size: 50MB"
4. **Audio unclear** → "Audio could not be understood. Please ensure the audio is clear and in English."
5. **API unavailable** → "Speech recognition service error: ..."
6. **Empty transcript** → "Could not extract text from audio."

### Developer Notes
- All errors are caught and returned as JSON with descriptive messages
- Temporary files are cleaned up even on error
- Empty/None transcripts are validated before scoring

## Limitations & Future Improvements

### Current Limitations
1. English language only
2. Requires internet connection for Google API
3. Long audio files (>5 minutes) may timeout
4. Maximum 50MB file size
5. No audio quality preprocessing

### Future Enhancements
1. Support for multiple languages
2. Offline transcription option (using Whisper or similar)
3. Audio preprocessing (noise reduction, normalization)
4. Larger file support with chunking
5. Real-time transcription for live input
6. Audio visualization and trimming
7. Multiple speaker detection
8. Confidence scores for transcription

## Testing

### Unit Tests
Run `python test_api.py` to verify:
- API health check
- API info endpoint
- Transcribe endpoint availability

### Integration Testing
1. Upload a clear MP3 file with a self-introduction
2. Verify transcript appears in text area
3. Click "Score and generate video"
4. Verify results display and video generates

### Edge Cases to Test
- Unsupported audio formats (.flv, .mov, etc.)
- Files larger than 50MB
- Corrupted audio files
- Empty audio files
- Very quiet audio
- Background noise

## FAQ

**Q: What audio formats are supported?**
A: MP3, WAV, M4A, WebM, OGG, FLAC, AAC (any format supported by SpeechRecognition)

**Q: How accurate is the transcription?**
A: Google's speech recognition is quite accurate (~95%) for clear, English audio. Quality depends on audio clarity and background noise.

**Q: Can I transcribe non-English audio?**
A: Currently English only. Can be extended by modifying the `speech_recognition` parameters.

**Q: What if the API fails?**
A: A clear error message appears. Check internet connection and try again with a different audio file.

**Q: Are uploaded files stored?**
A: No, temporary files are deleted immediately after transcription.

**Q: How long does transcription take?**
A: Usually 2-10 seconds depending on audio length and network speed.

**Q: Can I transcribe videos?**
A: Not directly, but you can extract audio from video first using external tools.

## Support

For issues or questions:
1. Check the error message for specific guidance
2. Verify audio is clear and in English
3. Ensure file is one of the supported formats
4. Check that backend is running: `python app.py`
5. Verify API is responding: `python test_api.py`

## Changelog

### Version 1.0 (Current)
- ✅ Audio upload with drag-and-drop
- ✅ Automatic speech-to-text transcription
- ✅ Google Speech Recognition API integration
- ✅ File validation and size limits
- ✅ Progress tracking UI
- ✅ Error handling and user feedback
- ✅ Dual input modes (text/audio)
- ✅ Seamless integration with scoring system
