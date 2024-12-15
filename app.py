import streamlit as st  # type: ignore

#page setup ----------------------

st.set_page_config(
    layout="wide",
)



profile_page = st.Page(
    page = "views/profile.py",
    title = "Profile",
    icon = ":material/account_circle:",
    default = True,
)

projects_page = st.Page(
    page = "views/projects.py",
    title = "Projects",
    icon = ":material/category:",
)

blogs_page = st.Page(
    page = "views/blogs.py",
    title = "Articles",
    icon = ":material/library_books:",
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact Me",
    icon = ":material/email:",
)

##Projects-------------------------------------------------------------
chatbot_project_page = st.Page(
    page = "views/projects/chatbot.py",
    title = "Chatbot",
    icon = ":material/category:",
)
dashboard_project_page = st.Page(
    page = "views/projects/dashboard.py",
    title = "Dashboard",
    icon = ":material/category:",
)


#Navigation Menu --------------------
pg=st.navigation(pages=[profile_page, projects_page, blogs_page, contact_page])



# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Jubayer Hossain Arnob": [profile_page, projects_page, blogs_page, contact_page],
        "Projects": [chatbot_project_page, dashboard_project_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Made with streamlit")


#run_navigation ------------------
pg.run()