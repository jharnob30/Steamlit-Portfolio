import streamlit as st
import re
import smtplib
from email.mime.text import MIMEText


# Function to validate email format
def is_valid_email(email):
    """
    Simple regex to validate email.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email)


# Function to send email
def send_email(name, email_address, message):
    """
    Send email using SMTP server.
    Replace placeholders with your SMTP server credentials.
    """
    # Set up the SMTP server connection (example with Gmail SMTP)
    try:
        # Email credentials
        smtp_user = "jubayer.arnob97@gmail.com"  # Replace with your email
        smtp_password = "rxfq efmy fxda lmsd"  # Replace with your password

        # Set up SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(smtp_user, smtp_password)

        # Create email content
        subject = "Streamlit Portfolio - Contact Me"
        body = f"Name: {name}\nEmail: {email_address}\nMessage: {message}"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = smtp_user
        msg["To"] = smtp_user

        # Send email
        server.sendmail(smtp_user, smtp_user, msg.as_string())
        server.quit()

        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")


# Streamlit UI for the contact form
def contact_form():
    """
    Displays a contact form and handles submission.
    """
    st.title("Contact Me")

    with st.form(key="contact_form"):
        st.subheader("Please share your details below")

        # Input fields
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")

        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Validate fields
            if not name or not email or not message:
                st.error("All fields are required. Please fill them in.")
            elif not is_valid_email(email):
                st.error("Invalid email address. Please enter a valid one.")
            else:
                st.info("Sending email...")
                send_email(name, email, message)


# Render contact form
contact_form()
        
st.markdown(
    """
    <div style="display: flex; gap: 0px; align-items: center;">
        <a href="https://github.com/yourgithub" target="_blank" style="filter: grayscale(100%);">
            <img src="https://img.icons8.com/ios-filled/30/000000/github.png" alt="GitHub">
        </a>
        <a href="https://linkedin.com/in/yourlinkedin" target="_blank" style="filter: grayscale(100%); margin-left: 5px;">
            <img src="https://img.icons8.com/ios-filled/30/0077B5/linkedin.png" alt="LinkedIn">
        </a>
        <a href="https://behance.net/yourbehance" target="_blank" style="filter: grayscale(100%); margin-left: 5px;">
            <img src="https://img.icons8.com/ios-filled/30/1769FF/behance.png" alt="Behance">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)