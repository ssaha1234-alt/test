import streamlit as st
import pandas as pd
from googlesearch import search

# --- Page Configuration ---
st.set_page_config(page_title="Profile Search Bot", page_icon="🔍", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f2f2f7;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stSlider > div > div {
        padding: 10px 0;
    }
    .stButton>button {
        background-color: #0072E3;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #005bb5;
    }
    .stDownloadButton>button {
        background-color: #28a745;
        color: white;
        border-radius: 6px;
        font-weight: bold;
    }
    .header-text {
        font-size: 26px;
        font-weight: bold;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title and Instructions ---
st.markdown('<div class="header-text">🤖 Smart Profile Search Assistant</div>', unsafe_allow_html=True)
st.markdown("Search academic and professional profiles from trusted sources like LinkedIn, Google Scholar, and ResearchGate.")

# --- Search Sites ---
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# --- User Inputs ---
query = st.text_input("🔍 Enter keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Results per site", 1, 20, 5)

# --- Search Button ---
if st.button("Start Search") and query.strip():
    with st.spinner("🔎 Searching the web... Please wait..."):
        results = []
        for source, site_filter in SEARCH_SITES.items():
            full_query = f"{query} {site_filter}"
            st.write(f"🛰️ Searching: `{full_query}`")

            try:
                urls = list(search(full_query, num_results=num_results))
            except Exception as e:
                st.error(f"⚠️ Error searching {source}: {e}")
                continue

            for url in urls:
                results.append({
                    "Source": source,
                    "Query": full_query,
                    "URL": url
                })

    # --- Display Results ---
    if results:
        df = pd.DataFrame(results)
        df_display = df.copy()
        df_display["URL"] = df_display["URL"].apply(lambda x: f"[Link]({x})")

        st.success(f"✅ Found {len(df)} results.")
        st.markdown(df_display.to_markdown(index=False), unsafe_allow_html=True)

        # --- Download as CSV ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
