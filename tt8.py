import streamlit as st
import pandas as pd
from googlesearch import search

# Page config
st.set_page_config(page_title="RPSG SCOUT Bot", page_icon="🔭", layout="centered")

# --- Custom CSS ---
st.markdown(
    """
    <style>
    body, .stApp {
        background-image: url("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    .title-text {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 12px;
        margin-top: 30px;
    }

    label, .stSlider label, .stMarkdown p, .stTextInput label {
        color: white !important;
        font-weight: bold;
    }

    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }

    .stButton > button {
        background-color: #0059b3;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
        transition: 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #0073e6;
        transform: scale(1.05);
    }

    .stSlider > div {
        background-color: rgba(255,255,255,0.8);
        border-radius: 10px;
        padding: 15px;
        color: black;
    }

    .stDataFrameContainer {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 10px;
        color: black;
    }

    .stDownloadButton > button {
        background-color: #004080;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding
