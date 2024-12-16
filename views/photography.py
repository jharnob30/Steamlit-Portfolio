import streamlit as st

# Page Title
st.title("Jubayer Hossain's Photography Portfolio")

# Improved Header for Art & Illustrations Section

st.markdown('''<h5>A collection of my Captures for soul entertainment</h5>''', unsafe_allow_html=True)

# Sample data for images (now supports both URL and local path)
images = [
    {
        "source": "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/470130049_2587580184785176_4922155773556246974_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeHz61oTvd3ukRgYQDs01sA8VR9632dT3IVVH3rfZ1PchYekpuZRdeJ2cTOi3spxKxu3FaSJTkFjJHiDP3nR1qy4&_nc_ohc=MB87bPW2jZUQ7kNvgEsBxMH&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=AIMkNU5fB7kfhD7Av44zCa3&oh=00_AYCUQMpoDkKnrIWQyQAMlctiVEvYbdb-oP53jNEMoGGnEg&oe=67666BBC",  # URL
        "title": "Sunset Bliss", 
        "date": "2023-06-12", 
        "category": "Nature", 
        "device": "Canon EOS 5D"
    },
    {
        "source": "assets/image1.jpg",  # Local path
        "title": "Urban Nightscape", 
        "date": "2023-09-15", 
        "category": "Cityscape", 
        "device": "Sony A7 III"
    },
    {
        "source": "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/470130049_2587580184785176_4922155773556246974_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeHz61oTvd3ukRgYQDs01sA8VR9632dT3IVVH3rfZ1PchYekpuZRdeJ2cTOi3spxKxu3FaSJTkFjJHiDP3nR1qy4&_nc_ohc=MB87bPW2jZUQ7kNvgEsBxMH&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=AIMkNU5fB7kfhD7Av44zCa3&oh=00_AYCUQMpoDkKnrIWQyQAMlctiVEvYbdb-oP53jNEMoGGnEg&oe=67666BBC",  # URL
        "title": "Mountain Adventure", 
        "date": "2023-07-08", 
        "category": "Nature", 
        "device": "Nikon D850"
    },
    {
        "source": "assets/image2.jpg",  # Local path
        "title": "Street Vibes", 
        "date": "2023-10-21", 
        "category": "Street", 
        "device": "Fujifilm X-T4"
    },
]

# Sidebar for filtering by category
categories = sorted(set([image["category"] for image in images]))
selected_category = st.sidebar.selectbox("Filter by Category", ["All"] + categories)

# Filter images based on the selected category
filtered_images = images if selected_category == "All" else [img for img in images if img["category"] == selected_category]

# Display Images
st.header(f"Photographs ({selected_category if selected_category != 'All' else 'All Categories'})")
cols = st.columns(4)

# Loop through images and display with details
for i, image in enumerate(filtered_images):
    with cols[i % 4]:
        # Check if the source is a URL or local path
        if image["source"].startswith("http"):  # Check if the source is a URL
            st.image(image["source"], caption=image["title"], use_container_width=True)
        else:  # Local path
            st.image(image["source"], caption=image["title"], use_container_width=True)
        
        st.caption(f"**Title:** {image['title']}  \n"
                   f"**Capture Date:** {image['date']}  \n"
                   f"**Category:** {image['category']}  \n"
                   f"**Device:** {image['device']}")

# Footer with Instagram link for full portfolio
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.instagram.com/j_h_arnob/" 
           style="text-decoration: none; background-color: #3b5998; color: white; padding: 12px 24px; border-radius: 5px; font-size: 18px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;">
           View Full Photo Portfolio on Instagram
        </a>
    </div>
""", unsafe_allow_html=True)
