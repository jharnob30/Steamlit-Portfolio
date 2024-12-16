import streamlit as st

# Page Title
st.title("Jubayer Hossain's Art & Photography Portfolio")

# Improved Header for Art & Illustrations Section
st.markdown('''<h5>A collection of my art, designs, and illustrations<h5>''', unsafe_allow_html=True)


# Categories for filtering
categories = ["All", "Music", "Comic", "Illustrations"]
selected_category = st.sidebar.selectbox("Filter by Category", categories)

# List of Behance project URLs with categories (replace with your actual project URLs and categories)
projects = [
    {"category": "Music", "url": "https://www.behance.net/gallery/103078787/Mr-Tambourine-Man"},
    {"category": "Music", "url": "https://www.behance.net/gallery/101030999/PINK-FLOYD-TOP-11"},
    {"category": "Comic", "url": "https://www.behance.net/gallery/150433345/Project-Name-1"},
    {"category": "Music", "url": "https://www.behance.net/gallery/103078787/Mr-Tambourine-Man"},
    {"category": "Music", "url": "https://www.behance.net/gallery/101030999/PINK-FLOYD-TOP-11"},
    {"category": "Comic", "url": "https://www.behance.net/gallery/150433345/Project-Name-1"},
    # Add more projects here with their respective categories
]

# Function to convert Behance gallery URL to embed URL
def get_embed_url(gallery_url):
    project_id = gallery_url.split("/")[4]  # Extract the project ID from the gallery URL
    return f"https://www.behance.net/embed/project/{project_id}?ilo0=1"

# Filter projects by category
filtered_projects = [project for project in projects if selected_category == "All" or project["category"] == selected_category]

# Create columns for gallery view with 4 columns layout
num_columns = 4  # Set to 4 columns for a 4x4 grid layout
cols = st.columns(num_columns)

# Loop through the filtered gallery URLs, convert to embed URL, and display them
for i, project in enumerate(filtered_projects):
    embed_url = get_embed_url(project["url"])
    with cols[i % num_columns]:  # Distribute the projects evenly across columns
        st.markdown(
            f'''
            <div style="border-radius: 15px; overflow: hidden; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <iframe src="{embed_url}" 
                        height="350" 
                        width="100%"  <!-- Make the iframe width responsive -->
                        allowfullscreen 
                        lazyload 
                        frameborder="0" 
                        allow="clipboard-write" 
                        refererPolicy="strict-origin-when-cross-origin">
                </iframe>
            </div>
            ''',
            unsafe_allow_html=True
        )

# Add a "View More" link styled as a button at the bottom with hover effect
st.markdown(
    '''
    <div style="text-align: center; margin-top: 30px;">
        <a href="https://www.behance.net/jubayerarnob/projects" 
           style="text-decoration: none; background-color: #3b5998; color: white; padding: 12px 24px; border-radius: 5px; font-size: 18px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;">
           View More Art & Illustrations on Behance
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
