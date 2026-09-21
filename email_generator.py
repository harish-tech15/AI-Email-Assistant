
from utils.prompts import EMAIL_SYSTEM_PROMPT


def create_email_prompt(
    purpose,
    recipient,
    tone,
    length,
    details
):
    prompt = f"""
{EMAIL_SYSTEM_PROMPT}

Email purpose:
{purpose}

Recipient:
{recipient}

Tone:
{tone}

Length:
{length}

Additional details:
{details}

Generate the email now.
"""

    return prompt
