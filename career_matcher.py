# -*- coding: utf-8 -*-
import streamlit as st
from collections import Counter

st.set_page_config(page_title="Career Matcher", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
        .title {
            font-size: 42px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #7f8c8d;
            text-align: center;
        }
        .box {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Career Matcher 🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">בחר את מה שמתאים לך ונגיד לך איזו עבודה בול בשבילך!</div>', unsafe_allow_html=True)

with st.form("career_form"):
    q1 = st.multiselect("מה מלהיב אותך?", ["טכנולוגיה", "אמנות", "עבודה עם אנשים", "טבע ובעלי חיים", "אוכל ובישול", "עסקים", "משהו שקט ונעים"])
    q2 = st.multiselect("איפה אתה מדמיין את עצמך עובד?", ["משרד הייטק", "אולפן", "בית ספר", "מסעדת שף", "חווה או שטח פתוח", "מהבית", "מעבדה"])
    q3 = st.multiselect("מה הכי מאפיין אותך?", ["יצירתיות", "אכפתיות", "דיוק", "חברותיות", "סקרנות", "משמעת עצמית", "אהבת טכנולוגיה"])
    q4 = st.multiselect("איך אתה אוהב לעבוד?", ["בצוות", "לבד", "עם ילדים", "עם מחשבים", "עם אוכל", "עם בעלי חיים", "עם קהל"])
    q5 = st.radio("כמה אתה אוהב ללמוד דברים חדשים?", ["מאוד", "בינוני", "פחות"])
    submitted = st.form_submit_button("מצא לי מקצוע!")

if submitted:
    interests = q1 + q2 + q3 + q4

    job_scores = {
        "מתכנת / סייבר / מפתח תוכנה": ["טכנולוגיה", "אהבת טכנולוגיה", "דיוק", "עם מחשבים", "משרד הייטק", "סקרנות"],
        "שחקן / מוזיקאי / במאי": ["אמנות", "אולפן", "יצירתיות", "עם קהל"],
        "מורה / מדריך / מרצה": ["עבודה עם אנשים", "בית ספר", "אכפתיות", "עם ילדים", "חברותיות"],
        "וטרינר / מאלף / מטפל בבעלי חיים": ["טבע ובעלי חיים", "חווה או שטח פתוח", "עם בעלי חיים", "דיוק"],
        "שף / קונדיטור / בלוגר אוכל": ["אוכל ובישול", "מסעדת שף", "עם אוכל", "יצירתיות"],
        "יזם / מנהל שיווק / כלכלן": ["עסקים", "מהבית", "דיוק", "סקרנות", "עם קהל"],
        "ספרן / כותב / מתרגם": ["משהו שקט ונעים", "לבד", "דיוק", "מהבית"]
    }

    score_counter = {}

    for job, keywords in job_scores.items():
        matches = len(set(keywords) & set(interests))
        score_counter[job] = matches

    # ניקח את המקצועים עם הכי הרבה התאמות
    best_match = max(score_counter, key=score_counter.get)

    st.markdown(f'<div class="box"><h3>המקצוע שהכי מתאים לך הוא:</h3><p><strong>{best_match}</strong></p></div>', unsafe_allow_html=True)
