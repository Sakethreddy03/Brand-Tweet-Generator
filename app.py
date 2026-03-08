import streamlit as st
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT, BRAND_ANALYSIS_PROMPT, TWEET_GENERATION_PROMPT

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page Config
st.set_page_config(page_title="Brand Tweet Generator", layout="wide")

# Custom CSS for Dark Theme & UI matching
st.markdown("""
<style>
    /* Main Background */
    .stApp { background-color: #0E1117; color: white; }
    
    /* Title Styling */
    .main-title {
        font-size: 50px; font-weight: 800; text-align: center;
        background: linear-gradient(to right, #A855F7, #EC4899);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title { font-size: 60px; font-weight: 800; text-align: center; color: white; margin-top: -20px;}
    .description { text-align: center; color: #94A3B8; margin-bottom: 40px; }
    
    /* Card Styling */
    .tweet-card {
        background-color: #1E293B; border-radius: 15px; padding: 20px;
        border: 1px solid #334155; margin-bottom: 20px;
    }
    .badge {
        padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;
    }
    .badge-promo { background-color: #F59E0B; color: black; }
    .badge-engaging { background-color: #EC4899; color: white; }
    .badge-info { background-color: #06B6D4; color: white; }
    .badge-witty { background-color: #10B981; color: white; }
    
    /* Brand Header */
    .brand-header {
        background: linear-gradient(45deg, #1e1e2f, #3a1c71);
        border-radius: 15px; padding: 30px; margin-bottom: 30px;
        border: 1px solid #4B5563;
    }
</style>
""", unsafe_allow_html=True)

# UI Header
st.markdown('<div class="main-title">Brand Tweet</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Generator</div>', unsafe_allow_html=True)
st.markdown('<p class="description">Analyze any brand\'s voice and generate 10 perfectly crafted tweets with AI-powered tone matching</p>', unsafe_allow_html=True)

# Input Form
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        brand_name = st.text_input("Brand Name", placeholder="e.g. NIKE")
    with col2:
        industry = st.text_input("Industry / Category", placeholder="e.g. Sportswear")
    
    objective = st.selectbox("Campaign Objective", [
        "🔥 Engagement — Boost likes, replies & shares",
        "📢 Promotion — Drive sales & conversions",
        "🌐 Brand Awareness — Expand reach"
    ])
    
    product_desc = st.text_area("Product Description", placeholder="Briefly describe the product or service...")

    if st.button("Generate Tweets", use_container_width=True):
        if not brand_name or not product_desc:
            st.error("Please fill in the Brand Name and Product Description.")
        else:
            with st.status("Analyzing Brand Voice...", expanded=True) as status:
                # 1. Analyze Brand
                analysis_res = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": SYSTEM_PROMPT},
                              {"role": "user", "content": BRAND_ANALYSIS_PROMPT.format(brand_name=brand_name, industry=industry)}]
                )
                analysis = json.loads(analysis_res.choices[0].message.content)
                
                # 2. Generate Tweets
                tweet_res = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": SYSTEM_PROMPT},
                              {"role": "user", "content": TWEET_GENERATION_PROMPT.format(analysis=analysis, objective=objective, product_description=product_desc)}]
                )
                tweets = json.loads(tweet_res.choices[0].message.content)
                status.update(label="Tweets Generated!", state="complete")

            # Display Results
            st.markdown(f"""
            <div class="brand-header">
                <h1>{brand_name.upper()}</h1>
                <span class="badge" style="background:#7C3AED">{analysis['tone']}</span>
                <span class="badge" style="background:#059669">{analysis['audience']}</span>
                <h3 style="margin-top:20px;">✨ Brand Voice Analysis</h3>
                <ul>{"".join([f"<li>{c}</li>" for c in analysis['characteristics']])}</ul>
            </div>
            """, unsafe_allow_html=True)

            st.subheader("Generated Tweets (10)")
            
            # Display Tweets in Grid
            t_col1, t_col2 = st.columns(2)
            for i, tweet in enumerate(tweets):
                target_col = t_col1 if i % 2 == 0 else t_col2
                badge_class = f"badge-{tweet['Category'].lower()}"
                
                with target_col:
                    st.markdown(f"""
                    <div class="tweet-card">
                        <div style="display:flex; justify-content:space-between;">
                            <span style="color:#94A3B8">#{i+1}</span>
                            <span class="badge {badge_class}">{tweet['Category']}</span>
                        </div>
                        <p style="font-size:18px; margin:15px 0;">{tweet['text']}</p>
                        <div style="display:flex; justify-content:space-between; color:#94A3B8; font-size:12px;">
                            <span>💬 🔁 ❤️</span>
                            <span>{len(tweet['text'])}/280 • <span style="color:#10B981">● {tweet['Engagement Score']}</span></span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)