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
