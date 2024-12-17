import streamlit as st
import sqlite3


# Database connection and initialization
def get_db_connection():
    try:
        conn = sqlite3.connect("assets/art/art_projects.db")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS project_categories (
                project_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY (project_id) REFERENCES projects(id),
                FOREIGN KEY (category_id) REFERENCES categories(id),
                PRIMARY KEY (project_id, category_id)
            );
        ''')

        # List of predefined categories
        predefined_categories = [
            "Music", 
            "TV/Movies & Shows", 
            "Branding", 
            "Conceptual", 
            "Comic", 
            "Typography",
            "Poster Design",
            "Animation",
            "Illustrations"
        ]

        # Clear any existing categories in the table (if any)
        conn.execute("DELETE FROM categories")

        # Insert predefined categories if not already in the database
        for category in predefined_categories:
            conn.execute(
                "INSERT OR IGNORE INTO categories (name) VALUES (?)", 
                (category,)
            )

        return conn
    except Exception as e:
        st.error(f"Database connection error: {e}")
        return None



def insert_project_to_db(category, url):
    if not category.strip() or not url.strip():
        st.sidebar.error("Category or URL cannot be empty.")
        return False

    if "behance.net/gallery/" not in url:
        st.sidebar.error("URL must be a valid Behance gallery link.")
        return False

    conn = get_db_connection()
    if conn:
        try:
            with conn:
                conn.execute(
                    "INSERT INTO projects (category, url) VALUES (?, ?)",
                    (category.strip(), url.strip())
                )
            return True
        except Exception as e:
            st.sidebar.error(f"Failed to save to database: {e}")
            return False
        finally:
            conn.close()
    return False


def fetch_categories():
    conn = get_db_connection()
    if conn:
        try:
            categories = conn.execute("SELECT name FROM categories").fetchall()
            conn.close()
            return [category[0] for category in categories]
        except Exception as e:
            st.error(f"Failed to fetch categories: {e}")
            conn.close()
            return []
    return []


def fetch_projects():
    conn = get_db_connection()
    if conn:
        try:
            projects = conn.execute("SELECT * FROM projects").fetchall()
            conn.close()
            return projects
        except Exception as e:
            st.error(f"Failed to fetch projects from database: {e}")
            conn.close()
            return []
    return []


def delete_project_from_db(project_id):
    conn = get_db_connection()
    if conn:
        try:
            with conn:
                conn.execute("DELETE FROM projects WHERE id = ?", (project_id,))
            return True
        except Exception as e:
            st.sidebar.error(f"Failed to delete project: {e}")
            return False
        finally:
            conn.close()
    return False


def get_embed_url(gallery_url):
    try:
        if "behance.net/gallery/" in gallery_url:
            project_id = gallery_url.split("/")[4]
            return f"https://www.behance.net/embed/project/{project_id}?ilo0=1"
        else:
            st.error("Invalid Behance URL format.")
            return gallery_url
    except IndexError:
        st.error(f"Invalid URL: {gallery_url}")
        return gallery_url


# Main Art Gallery Page
st.title("Jubayer Hossain's Art Gallery")
st.markdown('''<h5>A collection of my art, designs, and illustrations<h5>''', unsafe_allow_html=True)

st.sidebar.header("Filter Projects by Category")
categories = fetch_categories()
categories.insert(0, "All")
selected_category_filter = st.sidebar.selectbox("Filter by Category", categories)

filtered_projects = [
    project for project in fetch_projects() if selected_category_filter == "All" or project[1] == selected_category_filter
]

# Display Projects
num_columns = 3
cols = st.columns(num_columns)

for i, project in enumerate(filtered_projects):
    embed_url = get_embed_url(project[2])
    with cols[i % num_columns]:
        st.markdown(
            f'''
            <div style="border-radius: 15px; overflow: hidden; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <iframe src="{embed_url}" 
                        height="350" 
                        width="100%" 
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

# Sidebar for Logged-in Users
if st.session_state.get("logged_in", False):
    st.sidebar.header("Manage Projects")
    with st.sidebar.form("add_project_form"):
        dynamic_categories = fetch_categories()
        selected_category = st.selectbox("Select Category", options=dynamic_categories)
        new_url = st.text_input("Behance Project URL")
        submitted = st.form_submit_button("Add Project")

    if submitted:
        if insert_project_to_db(selected_category, new_url):
            st.sidebar.success("Successfully added project.")

    st.sidebar.header("Delete a Project")
    all_projects = fetch_projects()
    project_options = {f"{project[1]} - {project[2]}": project[0] for project in all_projects}

    selected_project_to_delete = st.sidebar.selectbox(
        "Select a Project to Delete", 
        options=[""] + list(project_options.keys())
    )

    if st.sidebar.button("Delete Project") and selected_project_to_delete:
        project_id = project_options[selected_project_to_delete]
        if delete_project_from_db(project_id):
            st.sidebar.success("Project deleted successfully.")
    

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
