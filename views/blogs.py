import streamlit as st
import feedparser
from bs4 import BeautifulSoup

# Medium RSS feed URL (replace with your own Medium username)
MEDIUM_RSS_URL = "https://medium.com/feed/@jubayerarnob97"

# Function to fetch blog posts from Medium using the RSS feed
def fetch_medium_blogs():
    # Parse the RSS feed
    feed = feedparser.parse(MEDIUM_RSS_URL)
    
    # Extract relevant blog information
    blogs = []
    for entry in feed.entries:
        blog = {
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "published": entry.published,
            "content": entry.content[0].value,  # Full content with HTML
            "topics": [tag['term'] for tag in entry.tags] if 'tags' in entry else []
        }
        blogs.append(blog)
    
    return blogs

# Function to clean HTML content, keeping structure but removing unwanted elements
def clean_html(content):
    soup = BeautifulSoup(content, "html.parser")
    
    # Remove image, script, and style tags
    for img_tag in soup.find_all("img"):
        img_tag.decompose()  # Remove images entirely
    
    for script in soup.find_all(["script", "style"]):
        script.decompose()  # Remove script and style tags
    
    # Ensure the content retains paragraph, heading, and other text-based tags
    for tag in soup.find_all(["figure", "style", "script"]):
        tag.decompose()  # Remove unwanted tags but keep others
    
    # Remove <p> tags but keep the text inside
    for p_tag in soup.find_all("p"):
        p_tag.unwrap()  # Remove <p> tag but keep its contents
    
    # Return the cleaned HTML as string (preserving other important HTML structure)
    return str(soup)

# Function to display blogs with a "Read Full Post" button
def display_blogs(blogs, selected_topic=None):
    st.title("Jubayer Hossain's Medium Blogs")
    
    # If the user selected a topic filter, show only matching blogs
    if selected_topic:
        blogs = [blog for blog in blogs if selected_topic.lower() in [topic.lower() for topic in blog['topics']]]
    
    # Show the filtered or all blogs
    for blog in blogs:
        # Clean the summary HTML and display the title, summary, and topics
        clean_summary = clean_html(blog['summary'])
        
        st.subheader(blog['title'])
        st.write(f"**Published on:** {blog['published']}")
        st.write(f"**Summary:** {clean_summary[:150]}...")  # Show only a truncated summary of cleaned text
        st.write(f"**Topics:** {', '.join(blog['topics']) if blog['topics'] else 'No topics'}")
        
        # Use an expander for the full content and add a link to the full blog post
        with st.expander(f"Read Full Post: {blog['title']}"):
            # Clean the content and render it as HTML
            clean_content = clean_html(blog['content'])
            st.markdown(f"<div>{clean_content}</div>", unsafe_allow_html=True)
            
            # Create a styled "Read on Medium" button
            st.markdown(f"<a href='{blog['link']}' target='_blank'><button style='background-color: #00ab6c; color: white; padding: 10px 20px; border-radius: 5px; border: none; font-size: 16px; cursor: pointer;'>Read on Medium</button></a>", unsafe_allow_html=True)
        
        st.write("---")

# Function to filter blog posts by topics (in the sidebar)
def filter_blogs_by_topic(blogs):
    # Get all unique topics/tags
    all_topics = set(topic for blog in blogs for topic in blog['topics'])
    
    # Display topic filter options in the sidebar
    selected_topic = st.sidebar.selectbox(
        "Filter by Topic",
        ["All Topics"] + list(all_topics)  # Add "All Topics" as the default option
    )
    
    if selected_topic != "All Topics":
        return selected_topic
    return None

# Fetch blogs
blogs = fetch_medium_blogs()

# Show topic filter in the sidebar
selected_topic = filter_blogs_by_topic(blogs)

# Display blogs based on the selected filter
display_blogs(blogs, selected_topic)


import streamlit as st
import requests
from datetime import datetime
from functools import lru_cache

# Replace with your Flickr API Key
API_KEY = st.secrets["photography"]["API_KEY"]

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


st.markdown(
    '''
    <div style="text-align: center; margin-top: 30px;">
        <a href="https://medium.com/feed/@jubayerarnob97" 
           style="text-decoration: none; background-color: #3b5998; color: white; padding: 12px 24px; border-radius: 5px; font-size: 18px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;">
           Read Articles on Medium
        </a>
    </div>
    <style>
        a:hover {{
            background-color: #2d4373;
            transform: scale(1.05);
        }}
    </style>
    ''',
    unsafe_allow_html=True
)
