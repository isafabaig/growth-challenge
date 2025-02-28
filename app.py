#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project 🌱🚀", page_icon= "★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header ("Welcome to your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI powered app helps you grow, innovate, and achieve more effortlessly.")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("❝Success is not final, failure is not fatal: it is the courage to continue that counts.❞ - Winston Churchill")

st.header("What's your Challege Today?")
user_input = st.text_input("Describe a challenge you are facing: ")

#condition
if user_input:
    st.success(f"💪you re facing: {user_input}- Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started")

#reflecting
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"🌟Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#achievements
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")


if achievement:
    st.success(f"🌟Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now😍")


    #footer
    st.write("- - -")
    st.write("🚀Keep believing in yourself. Growth is a journey, not a destination! ✨")
    st.write("Created by Safa Aamir 💻✨")  