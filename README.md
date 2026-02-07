# Viola - AI Voice Assistant

A powerful Python-based voice assistant that listens to your commands and performs various tasks using speech recognition and text-to-speech technology.

## Features

- **Voice Recognition**: Listens and understands natural language commands
- **Text-to-Speech**: Responds with natural-sounding female voice feedback
- **Web Navigation**: Open popular websites like Google, YouTube, GitHub, and Stack Overflow
- **Music Playback**: Play songs from a customizable music library on YouTube
- **Time Announcement**: Ask for the current time
- **Smart Wake Word**: Responds only after hearing "Viola" wake word
- **Easy to Extend**: Simple command structure to add new functionalities

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/lotus-outlook-6/Project-Viola.git
cd Project-Viola
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Viola
```bash
python main.py
```

## Prerequisites

- **Python 3.8+** (Tested with Python 3.12.5)
- **Microphone**: For voice input
- **Internet Connection**: For Google Speech API and web browsing
- **Windows OS**: (Primary support; other OS may vary)

## How to Use

1. Start the program with `python main.py`
2. Listen for "Listening..." message in console
3. Say **"Viola"** (the wake word) to activate
4. Viola responds: "Yes, how can I help you?"
5. Say your command from the list below

---

## Available Commands

### Web Navigation
| Command | Action |
|---------|--------|
| `"open google"` | Opens Google search |
| `"open youtube"` | Opens YouTube channel |
| `"open github"` | Opens GitHub profile |
| `"open stack overflow"` | Opens Stack Overflow |

### Music Control
| Command | Action |
|---------|--------|
| `"play virtual"` | Plays Virtual song |
| `"play checkpoint"` | Plays Checkpoint song |
| `"play ping"` | Plays Ping song |
| `"play overthinker"` | Plays Overthinker song |
| `"play playlist"` | Opens YouTube playlist |
| `"play"` | Lists all available songs |

**Note:** You can also use "play the [song name]" (e.g., "play the virtual")

### Information
| Command | Action |
|---------|--------|
| `"what is the time"` | Announces current time |
| `"tell me the time"` | Announces current time |
| `"what is your name"` | Introduces itself |
| `"who are you"` | Introduces itself |

### Control
| Command | Action |
|---------|--------|
| `"stop listening"` | Exit the program |

---

## Music Library

Customize your music in `musicLibrary.py`:

```python
music = {
    "song_name": "https://youtu.be/your-video-id",
    "another_song": "https://www.youtube.com/watch?v=another-id",
}
```

Add your favorite songs and Viola will play them instantly!

## Project Structure

```
Project-Viola/
├── main.py                  # Main application
├── musicLibrary.py          # Music library with YouTube links
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
├── README.md               # This file
└── tests/                  # Test suite
    ├── test_speak.py            # Test speak functionality
    ├── test_music_library.py    # Test music library
    └── test_commands.py         # Test command parsing
```

## Testing

Run tests from the tests folder:

```bash
# Test speech synthesis
python tests/test_speak.py

# Test music library
python tests/test_music_library.py

# Test command parsing
python tests/test_commands.py
```

## Configuration

Customize settings in `main.py`:

- **Speech Rate**: `engine.setProperty('rate', 150)` (higher = faster)
- **Listen Timeout**: `timeout=2` (seconds to listen)
- **Ambient Noise**: `r.adjust_for_ambient_noise(source, duration=1)` (calibration time)
- **Voice Gender**: Female voice is set by default in the `speak()` function

## Troubleshooting

### Microphone Not Detected
- Ensure microphone is connected and recognized by Windows
- Check Windows Sound Settings
- Run `tests/test_speak.py` to verify audio output

### Speech Recognition Not Working
- Verify internet connection (Google Speech API required)
- Speak clearly within the listening window
- Reduce background noise

### PyAudio Installation Issues
- For Windows, download pre-built wheels: [PyAudio Wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install: `pip install pyaudio-0.2.14-cp312-cp312-win_amd64.whl`

## Dependencies

```
SpeechRecognition==3.14.5  # Speech-to-text
pyttsx3==2.99              # Text-to-speech
pyaudio==0.2.14           # Microphone input
pywin32==311              # Windows support
```

## Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

**Ideas for Contributions:**
- Add more voice commands
- Expand music library
- Implement weather information
- Add note-taking functionality
- Create GUI interface
- Cross-platform optimization

---

Made with love by Lotus Outlook
