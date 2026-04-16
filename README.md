# Notes2Quiz

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?logo=google&logoColor=white) ![gTTS](https://img.shields.io/badge/gTTS-34A853?logo=googletranslate&logoColor=white) ![dotenv](https://img.shields.io/badge/dotenv-ECD53F?logo=dotenv&logoColor=black)

Turn note images into summarized notes, audio narration, and quiz-ready output.

## Live Website

[Open the notes2quiz live app](https://notes-to-quiz.streamlit.app/)

## Features

- Upload note images and generate a concise AI summary.
- Choose quiz difficulty: Easy, Medium, or Hard.
- Convert the generated note summary into audio.
- Clean, simple Streamlit interface for quick use.

## Run Locally

1. Clone the repository.
2. Move into the project folder.
3. Create and activate a virtual environment.
4. Install dependencies.
5. Add your Gemini API key to a .env file.
6. Start the app.

```bash
git clone https://github.com/fatin-israq/notes-to-quiz.git
cd notes-to-quiz
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_api_key_here" > .env
streamlit run app.py
```
