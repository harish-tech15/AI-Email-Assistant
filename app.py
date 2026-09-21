import streamlit as st
from google import genai


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide"
)


# =========================================================
# GEMINI API SETUP
# =========================================================

try:
    api_key = st.secrets["GEMINI_API_KEY"].strip()

    if not api_key:
        st.error("GEMINI_API_KEY is empty.")
        st.stop()

    client = genai.Client(
        api_key=api_key
    )

except KeyError:
    st.error(
        "GEMINI_API_KEY is not configured in Streamlit Secrets."
    )
    st.stop()

except Exception as e:
    st.error(
        f"Gemini configuration error: {e}"
    )
    st.stop()


# =========================================================
# GEMINI MODEL
# =========================================================

MODEL_NAME = "gemini-3.6-flash"


# =========================================================
# AI EMAIL FUNCTION
# =========================================================

def email_ai(task, email_text, tone, length):

    prompt = f"""
You are an AI Email Assistant.

Your job is to help users write clear, professional,
natural, and useful emails.

TASK:
{task}

TONE:
{tone}

LENGTH:
{length}

USER CONTENT:
{email_text}

RULES:

1. Understand the user's request carefully.
2. Do not invent important facts.
3. Keep the response natural and professional.
4. Use correct English.
5. If the task is generating or rewriting an email,
   provide a suitable SUBJECT and BODY.
6. If the task is summarizing an email,
   provide a short summary and important action items.
7. If the task is generating a reply,
   write only the appropriate reply.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    if not response.text:
        return "No response was generated."

    return response.text


# =========================================================
# APP HEADER
# =========================================================

st.title("📧 AI Email Assistant")

st.write(
    "Generate, rewrite, summarize, and reply to emails "
    "using Generative AI."
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

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


# =========================================================
# MAIN INPUT
# =========================================================

st.subheader("📝 Email Content")

email_text = st.text_area(
    "Enter your email request or email content:",
    height=220,
    placeholder=(
        "Example:\n"
        "I attended an interview yesterday for a Data Analyst "
        "position. I want to ask HR about the interview result "
        "and next steps."
    )
)


# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button(
    "✨ Generate with AI",
    type="primary",
    use_container_width=True
):

    if not email_text.strip():

        st.warning(
            "Please enter your email content first."
        )

    else:

        try:

            with st.spinner(
                "🤖 AI is generating your email..."
            ):

                result = email_ai(
                    task=task,
                    email_text=email_text,
                    tone=tone,
                    length=length
                )

            st.success(
                "✅ AI response generated successfully!"
            )

            st.subheader("🤖 AI Result")

            st.text_area(
                "Generated Content",
                value=result,
                height=400
            )

            st.download_button(
                label="📥 Download Email",
                data=result,
                file_name="ai_generated_email.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:

            error_message = str(e)

            st.error(
                "❌ Gemini API request failed."
            )

            st.code(
                error_message,
                language="text"
            )

            st.info(
                "Check your Streamlit Secrets and Gemini API key."
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Email Assistant | Python • Gemini • Streamlit • Generative AI"
)
