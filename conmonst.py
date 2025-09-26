import streamlit as st
import pandas as pd
import pickle
import requests
import re
from sklearn.linear_model import LinearRegression

# --- Load Linear Regression model ---
try:
    with open("linear_regression_model.pkl", "rb") as f:
        lr_model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ linear_regression_model.pkl not found. Please make sure the file exists.")
    st.stop()

# --- Streamlit UI ---
st.title("📊 YouTube Ad Revenue Prediction")
st.write("Enter a YouTube video URL and your API key to predict ad revenue.")

# Inputs
api_key = st.text_input("Enter your YouTube API Key:")
video_url = st.text_input("Enter YouTube Video URL:")

# Function to extract video ID from URL
def extract_video_id(url):
    """
    Extracts YouTube video ID from standard or shortened URLs.
    Returns None if invalid URL.
    """
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",  # standard URL
        r"youtu\.be\/([0-9A-Za-z_-]{11})"   # shortened URL
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

if st.button("Fetch Data & Predict"):
    if not api_key or not video_url:
        st.warning("⚠️ Please provide both API Key and YouTube Video URL.")
    else:
        # Extract video ID
        video_id = extract_video_id(video_url)
        if not video_id:
            st.error("❌ Invalid YouTube URL format. Please enter a correct URL.")
            st.stop()

        # Fetch video data from YouTube API
        api_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        try:
            response = requests.get(api_url)
            if response.status_code != 200:
                st.error(f"❌ Failed to fetch data. Status code: {response.status_code}")
                st.text(response.text)
            else:
                data = response.json()
                if "items" not in data or len(data["items"]) == 0:
                    st.error("❌ Video not found or data unavailable.")
                else:
                    stats = data["items"][0]["statistics"]

                    # Prepare input features for model (adjust to your trained features)
                    # Example: using numeric fields only
                    input_dict = {
                        'viewCount': int(stats.get("viewCount", 0)),
                        'likeCount': int(stats.get("likeCount", 0)),
                        'commentCount': int(stats.get("commentCount", 0))
                    }

                    input_df = pd.DataFrame([input_dict])

                    st.write("✅ Features fetched from YouTube API:")
                    st.dataframe(input_df)

                    # Predict ad revenue
                    prediction = lr_model.predict(input_df)
                    st.success(f"💰 Predicted Ad Revenue: ${prediction[0]:,.2f}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Request failed: {e}")

