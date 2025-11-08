# 🤖 AI Desktop Assistant (Tom)

An **AI-powered voice-based desktop assistant** built using Python that listens, speaks, and performs everyday tasks like web browsing, chatting, and automation using the OpenAI API.

---

## 🧠 Features
- 🎙️ **Voice Commands:** Listens to your voice using `SpeechRecognition`
- 🗣️ **Text-to-Speech:** Speaks responses using Windows SAPI (`win32com`)
- 🌐 **Web Automation:** Opens websites like Google, YouTube, and Wikipedia
- 🕒 **Time Functionality:** Tells the current time
- 💬 **AI Conversations:** Interacts intelligently using OpenAI (`text-davinci-003`)
- 💾 **File Creation:** Saves AI responses into text files
- 👋 **Exit Command:** Gracefully ends on “see you later”

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** 
  - `speech_recognition`
  - `pywin32`
  - `openai`
  - `datetime`
  - `webbrowser`
  - `os`
- **Model Used:** `text-davinci-003` (OpenAI GPT-3)

---

## ⚙️ Installation & Setup
2. Install dependencies
pip install -r requirements.txt

3. Add your OpenAI API Key

Create a new file named config.py in the project folder and add:

apikey = "your_api_key_here"

4. Run the Assistant
python main.py

🗣️ Example Commands

Try saying:

“Open Google”

“Open YouTube”

“What’s the time?”

“Write an essay using artificial intelligence”

“Reset chat”

“See you later”
