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
        padding: 8px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown("<div class='title-text'>🔭 RPSG SCOUT Bot 🔭</div>", unsafe_allow_html=True)

# --- Search Configuration ---
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# --- User Inputs ---
st.markdown("### 👤 Enter your search criteria below:")
query = st.text_input("🔍 Keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Number of results per site", 1, 20, 5)

# --- Perform Search ---
if st.button("Start Search") and query.strip():
    st.info("Searching... ⏳")

    results = []
    for source, site_filter in SEARCH_SITES.items():
        full_query = f"{query} {site_filter}"
        st.write(f"🔎 Searching: `{full_query}`")
        try:
            urls = list(search(full_query, num_results=num_results))
        except Exception as e:
            st.error(f"⚠️ Error searching {source}: {e}")
            continue
        for url in urls:
            results.append({"Source": source, "Query": full_query, "URL": url})

    # --- Display Results ---
    if results:
        df = pd.DataFrame(results)
        st.success(f"✅ Found {len(df)} results.")
        st.dataframe(df)

        # --- Download CSV ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
