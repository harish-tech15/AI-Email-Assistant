import streamlit as st
from google import genai

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide"
)

# --------------------------------
# Gemini API Configuration
# --------------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Gemini API key is not configured.")
    st.stop()


# --------------------------------
# Available Gemini Models
# --------------------------------
MODELS = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3-flash-preview",
    "gemini-flash-latest"
]


# --------------------------------
# AI Email Function
# --------------------------------
def email_ai(task, text, tone, length):

    prompt = f"""
You are an AI Email Assistant.

Task:
{task}

Tone:
{tone}

Length:
{length}

User Content:
{text}

Instructions:
- Write natural and professional English.
- Do not invent important information.
- Keep the response clear and useful.
- If generating an email, include:
  SUBJECT:
  BODY:
"""

    last_error = None

    for model in MODELS:
        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as e:
            last_error = e
            continue

    return f"""
AI service is temporarily unavailable.

Please try again after some time.

Error:
{last_error}
"""


# --------------------------------
# Header
# --------------------------------
st.title("📧 AI Email Assistant")

st.write(
    "Generate, rewrite, summarize, and reply to emails using Generative AI."
)

st.divider()


# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("⚙️ Email Settings")

task = st.sidebar.selectbox(
    "Select Task",
    [
        "Generate Email",
        "Generate Reply",
        "Rewrite Email",
        "Summarize Email"
    ]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Casual",
        "Polite"
    ]
)

length = st.sidebar.selectbox(
    "Select Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)


# --------------------------------
# User Input
# --------------------------------
st.subheader("📝 Email Content")

email_text = st.text_area(
    "Enter your email request or email content:",
    height=220,
    placeholder=(
        "Example: I attended an interview yesterday "
        "and want to ask HR about the result and next steps."
    )
)


# --------------------------------
# Generate Button
# --------------------------------
if st.button("✨ Generate with AI", type="primary"):

    if not email_text.strip():

        st.warning(
            "Please enter some email content first."
        )

    else:

        with st.spinner(
            "AI is processing your request..."
        ):

            result = email_ai(
                task=task,
                text=email_text,
                tone=tone,
                length=length
            )

        st.success(
            "AI response generated successfully!"
        )

        st.subheader("🤖 AI Result")

        st.text_area(
            "Generated Content",
            value=result,
            height=350
        )

        st.download_button(
            label="📥 Download Email",
            data=result,
            file_name="ai_generated_email.txt",
            mime="text/plain"
        )


# --------------------------------
# Footer
# --------------------------------
st.divider()

st.caption(
    "AI Email Assistant | Python • Gemini • Streamlit • Generative AI"
)
