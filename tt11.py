import streamlit as st
import pandas as pd
from googlesearch import search
from PIL import Image
import base64
from io import BytesIO

# --- Page Config ---
st.set_page_config(page_title="RPSG SCOUT Bot", page_icon="🔭", layout="centered")

# --- Helper: Convert image to base64 ---
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- Load and convert user-uploaded image ---
img = Image.open("image/PHOTO-2025-05-19-09-57-19.jpg").resize((300, 300))
img_base64 = image_to_base64(img)

# --- Custom CSS Styling ---
st.markdown(f"""
    <style>
    /* Background */
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }}

    /* Text colors */
    .stTextInput > div > div > input,
    .stSlider > div,
    .stDownloadButton,
    .stButton > button {{
        color: white !important;
        background-color: rgba(0,0,0,0.4);
        border-radius: 10px;
    }}

    .stTextInput label,
    .stSlider label,
    .stMarkdown,
    .stDataFrame,
    .stSlider {{
        color: white !important;
        font-weight: bold;
    }}

    /* Hide Streamlit UI options */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Floating scout image */
    .scout-img {{
        position: fixed;
        top: 50%;
        right: 20px;
        transform: translateY(-50%);
        width: 220px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 99;
    }}
    </style>
    <img src="data:image/jpeg;base64,{img_base64}" class="scout-img" />
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: white;'>🔭 RPSG SCOUT Bot 🔭</h1>", unsafe_allow_html=True)
st.write("Enter your search keywords and I’ll find relevant professional or academic profiles for you.")

# --- Search config ---
SEARCH_SITES = {
    "Google Scholar": "site:scholar.google.com",
    "ResearchGate": "site:researchgate.net",
    "LinkedIn": "site:linkedin.com/in"
}

# --- Inputs ---
query = st.text_input("🔍 Enter keywords (e.g., 'AI energy India')", "")
num_results = st.slider("📊 Results per site", 1, 20, 5)

# --- Search Logic ---
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

    if results:
        df = pd.DataFrame(results)
        st.success(f"✅ Found {len(df)} results.")
        st.dataframe(df)

        # --- Download ---
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="profile_links.csv", mime="text/csv")
    else:
        st.warning("❌ No results found.")
