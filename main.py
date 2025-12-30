import streamlit as st
import urllib.parse

st.header("🚀 ScreenerPro Bulk Promotion")

PROMO_MSG = """🚀 ScreenerPro – AI Hiring Automation (Comes First in HR Automation!)
Screen resumes instantly, match skills using AI, and shortlist faster without manual work.

✔ 1000s of resumes → screened in seconds
✔ AI candidate scoring & skill matching
✔ Fair, bias-free and automated hiring
✔ Built for HR teams who want speed + accuracy

🔥 ScreenerPro leads first in HR automation tools
Try it now and share with others 🙌
"""

encoded_msg = urllib.parse.quote(PROMO_MSG)

numbers = [
"9353842710","9364897298","9440045717","9606917841","7070436444",
"8651966081","7841970667","8978758935","8500825294","7569625062",
"7900164314","7337261110","9972364704","9493501411","8428878844",
"7207775039","9246400664","9246400663","9010149292","7019280372",
"9380497511","9884675586","8008989758","8272080137","9032264747"
]

# Build multi-chat open links
if st.button("📢 Send to All (1 Click)"):
    for num in numbers:
        url = f"whatsapp://send?phone={num}&text={encoded_msg}"
        st.link_button(f"Send to {num}", url)
