import streamlit as st
import pandas as pd
from googlesearch import search
from PIL import Image

# Set page config
st.set_page_config(page_title="RPSG SCOUT Bot", page_icon="🔭", layout="centered")

# --- Custom CSS styling ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }

    h1, h2, h3, h4, h5, h6, .stTextInput label, .stSlider label, .stButton button, .stMarkdown {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
    }

    /* Hide Streamlit footer & menu */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Title with binoculars
st.markdown("<h1 style='text-align: center;'>🔭 RPSG SCOUT Bot 🔭</h1>", unsafe_allow_html=True)
st.write("Enter your search keywords and I’ll find relevant professional or academic profiles for you.")

# Search sites
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# Inputs
query = st.text_input("🔍 **Enter keywords (e.g., 'AI energy India')**", "")
num_results = st.slider("📊 **Results per site**", 1, 20, 5)

# Optional Image (if uploaded to root dir)
try:
    image = Image.open("PHOTO-2025-05-19-09-57-19.jpg").resize((250, 250))
    st.image(image, caption="Your uploaded image", use_column_width=False)
except:
    pass

# Search logic
if st.button("Start Search") and query.strip():
    st.info("Searching the web... Please wait ⏳")
    results = []

    for source, site_filter in SEARCH_SITES.items():
        full_query = f"{query} {site_filter}"
        st.markdown(f"🔎 **Searching:** `{full_query}`")

        try:
            urls = list(search(full_query, num_results=num_results))
        except Exception as e:
            st.error(f"⚠️ Error searching {source}: {e}")
            continue

        for url in urls:
            results.append({"Source": source, "Query": full_query, "URL": url})

    # Display clickable results
    if results:
        df = pd.DataFrame(results)
        st.success(f"✅ Found {len(df)} results.")
        for _, row in df.iterrows():
            st.markdown(f"""
            🔗 **Source**: {row['Source']}  
            📝 **Query**: {row['Query']}  
            🌐 **URL**: [Click here]({row['URL']})  
            ---
            """)
        # Download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
