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
        "link": "views/projects/dashboard.py",
    },
    {
        "name": "Chatbot Project",
        "details": "NLP-based chatbot AI for user engagement.",
        "tech_stack": "Python, TensorFlow, NLP",
        "link": "views/projects/chatbot.py",
    },
]

# Create a dropdown filter UI
st.header("Projects")
category_filter = st.selectbox("Filter by Project Type", options=["All", "Dashboard", "Chatbot"])

# Render clickable links dynamically
for project in projects:
    if category_filter == "All" or \
       (category_filter == "Dashboard" and project["name"] == "Dashboard Project") or \
       (category_filter == "Chatbot" and project["name"] == "Chatbot Project"):
        st.markdown(
            f"""
            <a href="{project['link']}" target="_self" style="text-decoration: none;">
                <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h4>{project['name']}</h4>
                    <p><strong>Details:</strong> {project['details']}</p>
                    <p><strong>Tech Stack:</strong> {project['tech_stack']}</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
