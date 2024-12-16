import streamlit as st
from style import custom_css

# Inject custom CSS
st.markdown(custom_css(), unsafe_allow_html=True)

# Page Title
st.title("Jubayer Hossain's Portfolio")

# Define the projects data with query parameters
projects = [
    {
        "name": "Dashboard Project",
        "details": "Real-time dashboard to monitor system health KPIs.",
        "tech_stack": "React, HTML, CSS, JS",
        "category": "Dashboard",  # Added category
        "link": "/views/projects/dashboard.py",  # Use the relative link for the Dashboard page
    },
    {
        "name": "Chatbot Project",
        "details": "NLP-based chatbot AI for user engagement.",
        "tech_stack": "Python, TensorFlow, NLP",
        "category": "Chatbot",  # Added category
        "link": "/views/projects/chatbot.py",  # Use the relative link for the Chatbot page
    },
]

# Sidebar for filtering by project type
categories = sorted(set([project["category"] for project in projects]))  # Get unique categories from projects
selected_category = st.sidebar.selectbox("Filter by Project Type", ["All"] + categories)

# Filter projects based on the selected category
filtered_projects = projects if selected_category == "All" else [project for project in projects if project["category"] == selected_category]

# Display Projects
st.header(f"Projects ({selected_category if selected_category != 'All' else 'All Categories'})")

# Loop through filtered projects and display
for project in filtered_projects:
    st.markdown(
        f"""
        <a href="{project['link']}" target="_blank" style="text-decoration: none;">
            <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <h4>{project['name']}</h4>
                <p><strong>Details:</strong> {project['details']}</p>
                <p><strong>Tech Stack:</strong> {project['tech_stack']}</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
