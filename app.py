import streamlit as st  # type: ignore

# Page setup ----------------------
st.set_page_config(
    layout="wide",
)

# Initialize session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Login Section - Optional
def login():
    """Handles user login if the user isn't already logged in."""
    if not st.session_state.logged_in:
        st.sidebar.title("Login Section")
        with st.sidebar.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if username == "ocean97" and password == "1997":
                    st.session_state.logged_in = True
                    st.sidebar.success("You are logged in.")
                else:
                    st.sidebar.error("Invalid credentials.")
    else:
        # Only show a logout button if logged in
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.sidebar.info("Logged out. You can log in again to access management features.")


# Pages
profile_page = st.Page(
    page="views/profile.py",
    title="Profile",
    icon=":material/account_circle:",
)

projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon=":material/category:",
)

blogs_page = st.Page(
    page="views/blogs.py",
    title="Articles",
    icon=":material/library_books:",
)

contact_page = st.Page(
    page="views/contact.py",
    title="Contact Me",
    icon=":material/email:",
)

photography_page = st.Page(
    page="views/photography.py",
    title="My Captures",
    icon=":material/camera_alt:",
)

art_page = st.Page(
    page="views/art.py",
    title="Art and Illustrations",
    icon=":material/brush:",
)

chatbot_project_page = st.Page(
    page="views/projects/chatbot.py",
    title="Chatbot",
    icon=":material/robot:",
)

dashboard_project_page = st.Page(
    page="views/projects/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
)

# Navigation Menu ----------------
pg = st.navigation(
    {
        "Jubayer Hossain Arnob": [profile_page, blogs_page, art_page, photography_page, contact_page],
       # "Projects": [chatbot_project_page, dashboard_project_page],
    }
)

# Run navigation menu regardless of login
pg.run()


# Show Login logic - only trigger login features
login()
# Actions allowed for logged-in users
if st.session_state.logged_in:
    st.sidebar.success("You are logged in. You can manage projects, edit content, etc.")
else:
    st.sidebar.info("Login to manage contents")
