import streamlit as st
import pandas as pd
from googlesearch import search

# Page config
st.set_page_config(page_title="RPSG SCOUT Bot", page_icon="🔭", layout="centered")

# --- Custom CSS for background, font, and UI styling ---
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }

    html, body, [class*="css"] {
        color: white !important;
        font-weight: 600;
        font-size: 18px;
    }

    .title-text {
        text-align: center;
        font-size: 40px;
        font-weight: 800;
        color: white;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .stTextInput > div > div > input,
    .stSlider > div,
    .stButton > button,
    .stDownloadButton > button {
        background-color: rgba(0,0,0,0.6) !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
    }

    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.1);
    }

    /* Hide Streamlit default UI */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown("<div class='title-text'>🔭 RPSG SCOUT Bot 🔭</div>", unsafe_allow_html=True)

# --- Search sites ---
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# --- User Input ---
st.write("🔎 Enter your search keywords and I’ll find relevant professional or academic profiles.")
query = st.text_input("Enter keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Results per site", 1, 20, 5)

# --- Search Logic ---
if st.button("Start Search") and query.strip():
    st.info("Searching the web... Please wait ⏳")

    results = []
    for source, site_filter in SEARCH_SITES.items():
        full_query = f"{query} {site_filter}"
        st.write(f"🔍 Searching: `{full_query}`")

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

        # --- Download Button ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
