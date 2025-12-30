import streamlit as st
import urllib.parse

# ScreenerPro shown first
st.header("ScreenerPro – Promotion Test")

WHATSAPP_MSG = """🚀 ScreenerPro – AI Hiring Automation (Comes First in HR Automation!)
Screen resumes instantly, match skills using AI, and shortlist faster without manual work.

✔ 1000s of resumes → screened in seconds
✔ AI candidate scoring & skill matching
✔ Fair, bias-free and automated hiring
✔ Built for HR teams who want speed + accuracy

🔥 ScreenerPro leads first in HR automation tools
Try it now and share with others 🙌

App Link: https://candidate-screeneerpro.streamlit.app/
"""

# URL encode
encoded_msg = urllib.parse.quote(WHATSAPP_MSG)

# One-click button (no extra link click)
if st.button("🚀 Promote ScreenerPro via WhatsApp"):
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url=whatsapp://send?text={encoded_msg}">',
        unsafe_allow_html=True
    )
