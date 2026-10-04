# Hacktoberfest 2026 — Build for a Friend submission

## What I Built

I built **DostStudy**, a private AI study buddy designed around a common study problem: complicated textbook explanations can take too long to understand. DostStudy provides simple explanations, summaries, doubts, and quizzes with English, Hindi, and Hinglish support.

## Demo

https://youtube.com/shorts/WfbHxrnq8AE?si=ITySnc1B8-Ssphwq

## Source Code

https://github.com/godGamerz812/doststudy

## AI Stack

- **Gemma 3** — open-weight AI model
- **Ollama** — model serving
- **Python** — application logic
- **Streamlit** — user interface

Architecture:

Student
↓
Streamlit
↓
Python
↓
Ollama
↓
Gemma 3

## Why Open Innovation Matters

Open innovation matters because the AI model is not locked behind one closed provider. DostStudy uses an open-weight model through Ollama, giving the project more control over how the AI is used.

When Ollama runs locally, study questions and notes can be processed on the user's machine instead of requiring a closed cloud AI API. The model can also be swapped, prompts can be changed, and the application can be adapted without rebuilding the entire product around one provider.

For this project, open AI is valuable because it gives the developer and user more control over the AI stack.

## Built for a Real Person

**Design scenario:** DostStudy is designed for a college classmate who finds long and complicated textbook explanations difficult and prefers simple explanations in Hinglish.

This scenario guided the features: simpler explanations, summaries, and quick quizzes.

> I am not claiming a fabricated testimonial or quote. Any future friend feedback will be added only after the person has actually tested the project and given permission to share it.

## Feedback-Driven Improvements

The first version focuses on the core workflow: ask a question, choose an explanation style, and receive an AI-generated explanation or practice quiz.

Future improvements will be based on testing with the intended user and their genuine feedback.

## Prize Categories

- Best Use of Gemma

## My Agent Session

No separate DevRelay session is included in this submission.

## Required Challenge Tags

#devchallenge #weekendchallenge #hf26challenge

Thanks for participating!
