import streamlit as st
import pandas as pd
from googlesearch import search

# Page config
st.set_page_config(page_title="RPSG SCOUT Bot", page_icon="🔭", layout="centered")

# --- Custom CSS for background and styling ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    .title-text {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }

    label, .stSlider label, .stTextInput label {
        font-weight: bold !important;
        color: white !important;
    }

    .stTextInput > div > input {
        background-color: rgba(255,255,255,0.2);
        color: white;
    }

    .stSlider > div {
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px;
    }

    .stButton > button {
        color: white;
        background-color: #1f77b4;
        font-weight: bold;
        border-radius: 8px;
    }

    .stDataFrame {
        background-color: white;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title with binoculars ---
st.markdown("<div class='title-text'>🔭 RPSG SCOUT Bot 🔭</div>", unsafe_allow_html=True)

# --- Search configuration ---
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# --- User Inputs ---
st.write("Enter your search keywords and I’ll find relevant professional or academic profiles for you.")

query = st.text_input("🔍 Enter keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Results per site", 1, 20, 5)

# --- Perform Search ---
if st.button("Start Search") and query.strip():
    st.info("Searching the web... Please wait ⏳")

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

        # --- Download Button ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
