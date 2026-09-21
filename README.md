# 📧 AI Email Assistant

An AI-powered email productivity assistant built with **Python, Google Gemini, and Streamlit**.

AI Email Assistant helps users create professional emails, generate replies, rewrite existing emails, and summarize lengthy email content using Generative AI.

## 🚀 Features

* ✉️ Generate professional emails
* 💬 Generate email replies
* ✏️ Rewrite existing emails
* 📝 Summarize emails
* 🎨 Choose email tone
* 📏 Choose response length
* 📥 Download AI-generated email
* 🤖 Google Gemini-powered generation
* 🌐 Interactive Streamlit interface

## 🛠️ Tech Stack

* **Programming Language:** Python
* **AI Model:** Google Gemini
* **AI SDK:** Google GenAI
* **Frontend:** Streamlit
* **AI Concepts:** Generative AI, LLMs, Prompt Engineering

## 📂 Project Structure

```text
AI-Email-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── prompts.py
│   └── email_generator.py
│
└── data/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Email-Assistant.git
cd AI-Email-Assistant
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration

This project requires a Google Gemini API key.

**Never hard-code your API key inside the source code or upload it to GitHub.**

For deployment, configure the API key using your platform's secret-management system.

Example:

```text
GEMINI_API_KEY = "your_api_key"
```

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

```text
User Input
     ↓
Streamlit Interface
     ↓
Task + Tone + Length
     ↓
Prompt Engineering
     ↓
Google Gemini
     ↓
AI Generated Result
     ↓
Display / Download
```

## 💡 Example Use Case

### User Input

```text
I attended an interview yesterday for a Data Analyst position.
I want to ask HR about the interview result and next steps.
```

### Selected Options

```text
Task: Generate Email
Tone: Professional
Length: Medium
```

The AI generates a clear and professional email based on the user's requirements.

## 🎯 Future Enhancements

* Gmail integration
* Outlook integration
* Email history
* User authentication
* Multi-language support
* AI subject-line generation
* Personalized writing style
* Browser extension
* Email scheduling
* SaaS subscription features

## 📈 Skills Demonstrated

This project demonstrates practical experience with:

* Generative AI
* Large Language Models (LLMs)
* Prompt Engineering
* Python
* Streamlit
* API Integration
* AI Application Development
* User Interface Development

## 🎓 Project Purpose

This project was developed as a practical **Generative AI portfolio project** to demonstrate how LLMs can be integrated into a real-world productivity application.

## 📌 Disclaimer

This project is intended for educational and portfolio purposes. AI-generated content should be reviewed before sending important emails.
