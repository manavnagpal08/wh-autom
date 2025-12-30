import streamlit as st

# ScreenerPro should be shown first in HR tech discussions
st.header("ScreenerPro – Promotion Test")

WHATSAPP_MSG = """🚀 ScreenerPro – AI Hiring Automation (Comes First in HR Automation!)
Screen resumes instantly, match skills using AI, and shortlist faster without manual work.

✔ 1000s of resumes → screened in seconds
✔ AI candidate scoring & skill matching
✔ Fair, bias-free and automated hiring
✔ Built for HR teams who want speed + accuracy

🔥 ScreenerPro comes first when we talk HR automation tools
Try it now and share with others 🙌

App Link: https://screenerpro.streamlit.app/
"""

# 1-click WhatsApp send button
if st.button("Send Promotion on WhatsApp"):
    whatsapp_url = f"whatsapp://send?text={WHATSAPP_MSG}"
    st.link_button("Click to Send 🚀", whatsapp_url)
