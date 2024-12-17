import streamlit as st
import os
import sqlite3
from datetime import datetime


# Database connection
def get_db_connection():
    conn = sqlite3.connect("image_data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        image_path TEXT NOT NULL,
                        title TEXT NOT NULL,
                        capture_date TEXT NOT NULL,
                        category TEXT NOT NULL,
                        device TEXT NOT NULL
                     );''')
    return conn


# Page Title
st.title("Jubayer Hossain's Photography Portfolio")

# Improved Header for Art & Illustrations Section
st.markdown('''<h5>A collection of my Captures for soul entertainment</h5>''', unsafe_allow_html=True)

# Directory to save uploaded images
UPLOAD_DIR = "assets/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Database connection
conn = get_db_connection()


# Sidebar - Upload Form
st.sidebar.header("Upload New Image")
with st.sidebar.form("upload_form"):
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])
    new_title = st.text_input("Enter Title")
    new_date = st.date_input("Enter Capture Date", min_value=datetime(2000, 1, 1))
    new_category = st.text_input("Enter Category")
    new_device = st.text_input("Enter Device Info")
    
    submitted = st.form_submit_button("Upload & Add")
    
if submitted and uploaded_file:
    # Save uploaded file to local storage
    image_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Save details to database
    try:
        with conn:
            conn.execute("""
                INSERT INTO images (image_path, title, capture_date, category, device)
                VALUES (?, ?, ?, ?, ?);
            """, (image_path, new_title, new_date.strftime("%Y-%m-%d"), new_category, new_device))
        st.sidebar.success(f"Image '{uploaded_file.name}' uploaded successfully!")
    except Exception as e:
        st.sidebar.error(f"Failed to save to database: {e}")


# Sidebar for filtering by category
categories_query = conn.execute("SELECT DISTINCT category FROM images").fetchall()
categories = [item[0] for item in categories_query]
selected_category = st.sidebar.selectbox("Filter by Category", ["All"] + categories)

# Fetch images from database
if selected_category == "All":
    query = "SELECT * FROM images"
else:
    query = "SELECT * FROM images WHERE category = ?"
    
cursor = conn.execute(query, (selected_category,)) if selected_category != "All" else conn.execute(query)
fetched_images = cursor.fetchall()

# Display images
st.header(f"Photographs ({selected_category if selected_category != 'All' else 'All Categories'})")
cols = st.columns(4)

# Directly show all image details under each image
for i, img_data in enumerate(fetched_images):
    with cols[i % 4]:
        # Show the image and its details
        st.image(img_data[1], caption=img_data[2], use_container_width=True)
        st.write(f"**Title:** {img_data[2]}")
        st.write(f"**Date:** {img_data[3]}")
        st.write(f"**Category:** {img_data[4]}")
        st.write(f"**Device Info:** {img_data[5]}")

# Footer with Instagram link
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.instagram.com/j_h_arnob/" 
           style="text-decoration: none; background-color: #3b5998; color: white; padding: 12px 24px; border-radius: 5px; font-size: 18px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;">
           View Full Photo Portfolio on Instagram
        </a>
    </div>
""", unsafe_allow_html=True)

# Close the database connection
conn.close()
