# DostStudy 📚

A private, local-first AI study buddy built for a real friend.

## What it does
- Ask study doubts
- Explain difficult topics
- Summarize notes
- Generate quizzes
- English, Hindi, and Hinglish modes
- Beginner, School, and Exam difficulty levels
- Local AI via Ollama + Gemma 3

## Architecture
Student → Streamlit → Python → Ollama → Gemma 3

## Run locally

1. Install Ollama.
2. Download the model:

```bash
ollama pull gemma3:4b
```

3. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

4. Start the app:

```bash
streamlit run app.py
```

Open http://localhost:8501.

## Why open/local AI?
When Ollama is running locally, study material can be processed on the user's own machine instead of requiring a closed cloud AI API. The model can also be swapped by setting `OLLAMA_MODEL`.

## Docker
A Docker setup can be added for a self-hosted server. The Ollama model weights are not included in this repository.

## Friend feedback
Replace this section with the real friend's problem, feedback, and quote (with permission) before publishing the DEV submission.

## Model terms
Gemma is distributed under Google's applicable Gemma terms. Review current terms before redistribution or commercial use.

## License
MIT for this application code.
