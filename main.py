import streamlit as st
import pyperclip  # optional, for auto-copy to clipboard on desktop
import urllib.parse

st.header("🚀 ScreenerPro Promotion")

PROMO_MSG = """🚀 ScreenerPro – AI Hiring Automation (Comes First in HR Automation!)
Screen resumes instantly, match skills using AI, and shortlist faster without manual work.

✔ 1000s of resumes → screened in seconds
✔ AI candidate scoring & skill matching
✔ Fair, bias-free and automated hiring
✔ Built for HR teams who want speed + accuracy

🔥 ScreenerPro leads first in HR automation tools
Try it now and share with others 🙌

App Link: https://candidate-screeneerpro.streamlit.app/
"""

# 1-click button
if st.button("📢 Copy Message & Open WhatsApp"):
    pyperclip.copy(PROMO_MSG)  # copies text
    encoded = urllib.parse.quote("Open WhatsApp and paste the message")
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url=whatsapp://send?text={encoded}">',
        unsafe_allow_html=True
    )
    st.success("Message copied! Paste it in WhatsApp and send to your contacts or numbers.")
