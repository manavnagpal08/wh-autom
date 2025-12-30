import streamlit as st
import urllib.parse

st.header("🚀 ScreenerPro Bulk Promotion")

PROMO_MSG = """🚀 *ScreenerPro – AI Talent Intelligence (Comes First in HR Automation!)*

Hiring just got smarter. ScreenerPro is an AI-powered talent intelligence platform built to help HR teams screen, score, rank, and shortlist candidates at scale — with high precision and zero manual keyword guessing.

💼 *Access HR Portal:* https://screenerpro.streamlit.app/

🧠 *Powerful HR Capabilities:*
✔ Screens thousands of resumes in minutes  
✔ AI-generated Resume Score + Candidate Ranking  
✔ Skill Gap Analysis for accurate shortlisting  
✔ Candidate Pipeline Tracking with timestamps  
✔ AI Role Matcher to suggest best-fit job roles  
✔ Bias-aware, DEI-aligned analytics  
✔ Fast, scalable and recruiter-friendly  

🔍 *3-Step Transparent Hiring Workflow:*
1️⃣ *Data Ingestion* – Resumes are normalized & structured  
2️⃣ *AI Analysis* – Multi-dimensional skill scoring + bias checks  
3️⃣ *Human Review* – HR makes the final hiring call  

🎯 *Accuracy You Can Trust:*
✅ *95%+ reduction in shortlisting time*  
🎯 *97% matching precision tested on structured resumes*  
📊 *Multi-layer AI scoring for better hiring confidence*  

💡 ScreenerPro turns hiring into a faster, fairer, and data-driven system.

🙌 *Support us by sharing this with your network!*  
Help others hire smarter with AI-first intelligence 🚀

#HRTech #AIHiring #ResumeScreening #Recruitment #Automation #ScreenerPro

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
