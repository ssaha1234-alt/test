import streamlit as st
import pandas as pd
from googlesearch import search

# Set page config
st.set_page_config(page_title="Profile Search Bot", page_icon="🔍", layout="centered")

# Search sites
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# App UI
st.title("🤖 Profile Search Bot")
st.write("Enter your search keywords below and I'll find professional or academic profiles for you!")

# User input
query = st.text_input("🔍 Enter keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Results per site", 1, 20, 5)

# Button to search
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

    # Display results
    if results:
        df = pd.DataFrame(results)
        st.success(f"✅ Found {len(df)} results.")
        st.dataframe(df)

        # Download as CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
