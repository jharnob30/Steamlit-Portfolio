import streamlit as st
from style import custom_css
from views.contact import contact_form
#from assets.profile.modal_resume import show_pdf


@st.dialog(" ")
def show_contact_form():
    contact_form()


# Inject custom CSS
st.markdown(custom_css(), unsafe_allow_html=True)


st.title("Jubayer Hossain Arnob")
#Hero Section --------
col1, col2 = st.columns([3,1], gap="medium", vertical_alignment="center")

# About Me Section
with col1:
    # Page Title
    st.write(
        "**Senior Data Analyst | Aspiring Data Scientist**\n\n"
        "I'm Jubayer Hossain Arnob, currently employed as a Data Analyst at an Agri-Tech firm. "
        "I have experience in machine learning and computer vision tasks, and I hold a Bachelor's degree in "
        "Computer Science and Engineering. My career aspiration is to excel as a data scientist, "
        "focusing on advanced statistical analysis, machine learning, deep learning, and data visualization techniques."
    )

    st.markdown(
        """
        <div style="margin-top: 10px;">
            <a href="https://github.com/jharnob30?tab=repositories" target="_blank">
                <img src="https://img.icons8.com/ios-filled/30/000000/github.png" alt="GitHub">
            </a>
            <a href="https://www.linkedin.com/feed/" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/linkedin.png" alt="LinkedIn">
            </a>
            <a href="https://www.behance.net/jubayerarnob" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/behance.png" alt="Behance">
            </a>
            <a href="https://www.flickr.com/people/189515657@N03/" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/flickr.png" alt="Flickr">
            </a>
            <a href="https://www.facebook.com/jubayerhossain.arnob.97/" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/facebook.png" alt="Facebook">
            </a>
            <a href="https://www.instagram.com/j_h_arnob/" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/instagram-new.png" alt="Instagram">
            </a>
            <a href="https://studio.youtube.com/channel/UCAiYu2MOPo-hYy89ShNWyWQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D" target="_blank" style="margin-left: 10px;">
                <img src="https://img.icons8.com/ios-filled/30/000000/youtube-play.png" alt="YouTube">
            </a>
        </div>
        """,
        unsafe_allow_html=True
)



with col2:
    st.image("./assets/image2.jpg", width=200)

if st.button("Contact"):
    show_contact_form()


pdf_file = "assets/resume.pdf"

# Trigger file download with proper MIME type
st.download_button(
    label="Download Resume",
    data=open(pdf_file, "rb").read(),  # Read the file
    file_name="Jubayer_Hossain_Resume.pdf",  # Name for the downloaded file
    mime="application/pdf"  # MIME type for PDF
)




# Work Experience Section
st.header("Work Experience")
jobs = [
    {
        "role": "Senior Data Analyist",
        "organization": "Agrigate Network Limited",
        "duration": "Nov 2024 - Present",
        "location": "Dhaka, Bangladesh",

    },
    {
        "role": "Data Analyist",
        "organization": "Agrigate Network Limited",
        "duration": "Jan 2023 - Present",
        "location": "Dhaka, Bangladesh",
        "responsibilities": [
            "Develop survey design & strategy",
            "Design database schema and organize data effectively",
            "Analyze complex data sets using Excel, Google Sheets, and SQL",
            "Build and maintain dashboards using BI tools",
            "Provide training to field teams related to survey and digital applications",
        ],
    },
    {
        "role": "Research Associate - Deep Learning and Computer Vision (Part-time)",
        "organization": "Bangladesh Machine Learning Institute",
        "duration": "Mar 2024 - May 2024",
        "location": "Dhaka, Bangladesh",
        "responsibilities": [
            "Research generative models for computer vision",
            "Train and fine-tune pre-trained models",
            "Improve model performance using advanced techniques",
            "Design and implement computer vision tasks",
        ],
    },
        {
        "role": "Data Analyst (Part-time)",
        "organization": "Samak Technologies",
        "duration": "Jan 2024 - Mar 2024",
        "location": "New Delhi, India (Remote)",
        "responsibilities": [
            "Develop machine learning model for cattle weight prediction",
            "Fine-tune nutrition datasets and models",
            "Create datasets for cow/bull weight prediction",
        ],
    },
    {
        "role": "Data Analyst and Visualizer Intern",
        "organization": "Agrigate Network Limited",
        "duration": "Oct 2022 - Dec 2022",
        "location": "Dhaka, Bangladesh",
    }
    
]

for job in jobs:
    responsibilities = (
        f"<ul>{''.join(f'<li>{task}</li>' for task in job.get('responsibilities', []))}</ul>"
        if "responsibilities" in job
        else ""
    )
    st.markdown(
        f"""
        <div class="section-box">
            <h4>{job['role']}</h4>
            <p><strong>Organization:</strong> {job['organization']}</p>
            <p><strong>Duration:</strong> {job['duration']}</p>
            <p><strong>Location:</strong> {job['location']}</p>
            {responsibilities}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Digital Skills Section
skills = {
    "Python": ["Pandas", "NumPy", "Scikit-learn", "PyTorch", "OpenCV"],
    "Data Visualization": ["BI Tools (Power BI, Tableau, Looker)", "Python (Matplotlib, Seaborn, Plotly)"],
    "Databases & Spreadsheets": ["MySQL", "Postgres", "Excel", "Google Sheets"],
    "ML Algorithms": ["Regression", "Classification", "Clustering", "Random Forests"],
    "DL Architectures": ["CNNs", "NLP"],
    "Web Design": ["HTML", "CSS", "Basic JS", "Figma"],
    "Graphics Design": ["Adobe Illustrator", "Adobe Photoshop", "Canva"],
    "General": ["Google Suite", "Microsoft Office", "LARK"]
}



st.header("Digital Skills")

# Display all skills by category
for category, skill_list in skills.items():
    st.markdown(
        f"<div class='section-box'><strong>{category}</strong>: {', '.join(skill_list)}</div>",
        unsafe_allow_html=True,
    )


# Education Section
# Education Section
st.header("Education")
education_data = [
    {
        "degree": "Bachelor of Science in Computer Science and Engineering",
        "institution": "North South University",
        "location": "Dhaka, Bangladesh",
        "duration": "2018 - 2022",
        "grade": "CGPA 3.50/4.00 (Distinction: Cum Laude)",
        "thesis": "Out of Context Object Detection",
    },
    {
        "degree": "Higher Secondary School Certificate (Science)",
        "institution": "Uttara High School and College",
        "location": "Dhaka, Bangladesh",
        "duration": "2015 - 2017",
        "grade": "GPA 5.00",
    },
    {
        "degree": "Secondary School Certificate (Science)",
        "institution": "Uttara High School and College",
        "location": "Dhaka, Bangladesh",
        "duration": "2013 - 2015",
        "grade": "GPA 5.00",
    },
]

# Render education details
for edu in education_data:
    st.markdown(
        f"""
        <div class="section-box" style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
            <h4>{edu['degree']}</h4>
            <p><strong>Institution:</strong> {edu['institution']}</p>
            <p><strong>Location:</strong> {edu['location']}</p>
            <p><strong>Duration:</strong> {edu['duration']}</p>
            {"<p><strong>Grade:</strong> " + edu['grade'] + "</p>" if 'grade' in edu else ''}
            {"<p><strong>Thesis:</strong> " + edu['thesis'] + "</p>" if 'thesis' in edu else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


# Recommendations Section
st.header("Recommendations")
recommendations = [
    {
        "name": "Khan Muhammad Nafiul Akbar, Supervisor",
        "content": "Jubayer has a vast knowledge of various data analysis tools such as Tableau, Sheets, Python, and R. He is also proficient in utilizing no-code platforms such as AppSheet to input data, which has allowed our organization to streamline our data collection process."
    },
]

for rec in recommendations:
    st.markdown(
        f"""
        <div class="section-box">
            <p style="margin: 0; font-weight: bold;">{rec['name']}</p>
            <p>{rec['content']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
