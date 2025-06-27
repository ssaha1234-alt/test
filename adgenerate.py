import streamlit as st
import requests
from bs4 import BeautifulSoup
from Routerapi import generate_ad

st.set_page_config(page_title="AI Marketing Ad Generator", layout="centered")

st.title("🚀 AI Marketing Ad Generator")
st.markdown("Enter a company website and let AI generate a marketing ad for it!")

# User input
url = st.text_input("🔗 Enter company website URL", placeholder="https://www.example.com")

if st.button("Generate Ad") and url:
    try:
        st.info("Scraping website...")
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title + paragraph text
        title = soup.title.string if soup.title else "No title found"
        paragraphs = ' '.join(p.get_text() for p in soup.find_all('p')[:5])
        website_content = f"{title}\n{paragraphs}"

        st.success("Website content scraped. Sending to AI...")
        ad_text = generate_ad(website_content)

        st.markdown("### ✨ AI-Generated Ad:")
        st.text_area("Generated Marketing Ad", ad_text, height=200)

    except Exception as e:
        st.error(f"Error: {e}")
