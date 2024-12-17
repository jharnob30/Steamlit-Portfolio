import streamlit as st
import requests
from datetime import datetime
from functools import lru_cache

# Replace with your Flickr API Key
API_KEY = 'aa2df8738e2836736bb85876f495004b'

# Flickr API Endpoints
BASE_URL = "https://www.flickr.com/services/rest/"

@st.cache_data
def fetch_flickr_photos(user_id, page=1):
    """Fetches photos from Flickr for a specific user."""
    params = {
        "method": "flickr.photos.search",
        "api_key": API_KEY,
        "user_id": user_id,
        "page": page,
        "format": "json",
        "nojsoncallback": 1,
        "extras": "tags,date_taken",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("photos", {}).get("photo", [])
    else:
        st.error("Failed to fetch photos from Flickr.")
        return []

def get_photo_url(photo):
    """Constructs the photo URL."""
    farm_id = photo['farm']
    server_id = photo['server']
    photo_id = photo['id']
    secret = photo['secret']
    return f"https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg"

def get_flickr_url(photo):
    """Constructs the Flickr page URL."""
    return f"https://www.flickr.com/photos/{photo['owner']}/{photo['id']}"

# Replace with your Flickr user ID
user_id = "189515657@N03"

# Main Photography Gallery Page
st.title("Jubayer Hossain's Photography Portfolio")
st.markdown('''<h5>A collection of my photography captures for soul entertainment.<h5>''', unsafe_allow_html=True)

# Fetch photos from Flickr
photos = fetch_flickr_photos(user_id)

# Sidebar for filter options
st.sidebar.title("Filter Photos")
all_tags = set(tag for photo in photos for tag in photo.get("tags", "").split())
tags_list = ["All"] + sorted(all_tags)
selected_tag = st.sidebar.selectbox("Select Tag", tags_list)

if photos:
    # Filter photos based on selected tag
    filtered_photos = [
        photo for photo in photos
        if selected_tag == "All" or selected_tag in photo.get("tags", "").split()
    ]

    if filtered_photos:
        num_columns = 3
        cols = st.columns(num_columns)

        for idx, photo in enumerate(filtered_photos):
            photo_url = get_photo_url(photo)
            title = photo.get('title', 'Untitled')
            tags = photo.get('tags', 'No tags').replace(" ", ", ")
            date_taken = photo.get('datetaken', 'Unknown')
            flickr_url = get_flickr_url(photo)

            with cols[idx % num_columns]:
                st.markdown(
                    f'''
                    <a href="{flickr_url}" target="_blank">
                        <img src="{photo_url}" alt="{title}" style="width: 100%; border-radius: 5px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);"/>
                    </a>
                    <h4 style="margin-bottom: -10px; font-size: 16px;">{title}</h4>
                    <p style="font-size: 14px; margin: 0px; color: #555;">Date: {datetime.strptime(date_taken, '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y') if date_taken != 'Unknown' else 'Unknown'}</p>
                    <p style="font-size: 14px; color: #777;">Tags: {tags}</p>
                    ''',
                    unsafe_allow_html=True
                )
    else:
        st.warning("No photos match the selected tag.")
else:
    st.warning("No photos available to display.")
