# 🎤 Viola - AI Voice Assistant

A powerful Python-based voice assistant that listens to your commands and performs various tasks using speech recognition and text-to-speech technology.

## ✨ Features

- **Voice Recognition**: Listens and understands natural language commands
- **Text-to-Speech**: Responds with natural-sounding voice feedback
- **Web Navigation**: Open popular websites like Google, YouTube, GitHub, and Stack Overflow
- **Music Playback**: Play songs from a customizable music library on YouTube
- **Time Announcement**: Ask for the current time
- **Smart Wake Word**: Responds only after hearing "Viola" wake word
- **Easy to Extend**: Simple command structure to add new functionalities

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+** (Tested with Python 3.12.5)
- **Microphone**: For voice input (required for speech recognition)
- **Internet Connection**: For speech-to-text (Google API) and web browsing
- **Windows OS**: (Primary support for Windows; cross-platform support may vary)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/lotus-outlook-6/Project-Viola.git
cd Project-Viola
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Required Packages
```bash
pip install -r requirements.txt
```

> **Note**: If you encounter issues with `pyaudio` installation on Windows, you may need to install it using pre-built wheels. Alternatively, you can skip it initially and the program will still work (though audio input might need system configuration).

## 💻 Usage

### Starting Viola

```bash
python main.py
```

### How to Use

1. The program will print "Listening..." in the console
2. Say "**Viola**" (the wake word) to activate the assistant
3. After hearing the wake word, Viola will respond with "Yes, how can I help you?"
4. Now say your command

### 📍 Supported Commands

#### Web Navigation
- `"open google"` - Opens Google
- `"open youtube"` - Opens YouTube channel
- `"open github"` - Opens GitHub profile
- `"open stack overflow"` - Opens Stack Overflow

#### Music Control
- `"play virtual"` - Plays the Virtual song
- `"play checkpoint"` - Plays the Checkpoint song
- `"play ping"` - Plays the Ping song
- `"play overthinker"` - Plays the Overthinker song
- `"play playlist"` or `"play the playlist"` - Opens YouTube playlist
- `"play"` - Lists all available songs

#### Information
- `"what is the time"` or `"tell me the time"` - Announces current time
- `"what is your name"` or `"who are you"` - Introduces itself

#### Control
- `"stop listening"` - Exits the program

## 🎵 Music Library

The assistant comes with a music library stored in `musicLibrary.py`. You can easily add more songs:

```python
music = {
    "song_name": "https://youtu.be/your-video-id",
    "another_song": "https://www.youtube.com/watch?v=another-id",
}
```

Just add your song name as the key and YouTube URL as the value, and Viola will play it!

## 📁 Project Structure

```
Project-Viola/
├── main.py              # Main application file
├── musicLibrary.py      # Music library with YouTube links
├── requirements.txt     # Python dependencies
├── test_speak.py        # Test script for speak functionality
├── test_music_library.py # Test script for music library
└── README.md           # This file
```

## 🛠️ Testing

### Test speak functionality:
```bash
python test_speak.py
```

### Test music library:
```bash
python test_music_library.py
```

## ⚙️ Configuration

You can customize the following in `main.py`:

- **Speech Rate**: Adjust `engine.setProperty('rate', 150)` (higher = faster)
- **Listen Timeout**: Change `timeout=2` values for listening duration
- **Ambient Noise**: Adjust `r.adjust_for_ambient_noise(source, duration=1)` duration

## 🐛 Troubleshooting

### Microphone Not Detected
- Ensure your microphone is properly connected and recognized by Windows
- Check Sound Settings in Windows
- Try running tests with `test_speak.py` first to verify audio output works

### Speech Recognition Not Working
- Check your internet connection (Google Speech API requires this)
- Speak clearly and within the listening duration
- Reduce background noise

### PyAudio Installation Issues
- On Windows, pre-built wheels for PyAudio can be found at [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Download the appropriate `.whl` file and install: `pip install pyaudio-0.2.14-cp312-cp312-win_amd64.whl`

## 📦 Dependencies

- **speech_recognition** - Speech-to-text recognition
- **pyttsx3** - Text-to-speech engine
- **pyaudio** - Audio recording (optional, for microphone)

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add more voice commands
- Expand music library
- Implement weather information
- Add note-taking functionality
- Create GUI interface
- Cross-platform optimization

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Lotus Outlook**
- GitHub: [@lotus-outlook-6](https://github.com/lotus-outlook-6)
- YouTube: [Lotus Outlook Channel](https://www.youtube.com/@LotusOutlook)

## 🙏 Acknowledgments

- CodeWithHarry for Python Course inspiration
- GitHub community for feedback and contributions
- All users and testers

## 📞 Support

If you encounter any issues, please:
1. Check the Troubleshooting section
2. Open an issue on GitHub
3. Include error messages and system information

---

Made with ❤️ by Lotus Outlook
