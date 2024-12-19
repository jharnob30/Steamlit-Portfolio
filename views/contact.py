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
        smtp_user = st.secrets["email"]["smtp_user"]  # Replace with your email
        smtp_password = st.secrets["email"]["smtp_password"]  # Replace with your password

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

# Display Enhanced Email Address
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; font-family: 'Arial', sans-serif;">
        <a href="mailto:jubayerarnob97@gmail.com" style="text-decoration: none; color: #ffffff;">
            <div style="display: inline-block; padding: 10px 20px; background-color: #000000; border-color:#ffffff;  border-radius: 30px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); font-size: 18px; font-weight: bold; transition: transform 0.3s, box-shadow 0.3s;">
                <span>jubayerarnob97@gmail.com</span>
            </div>
        </a>
    </div>
    <style>
        a:hover div {
            transform: scale(1.05);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size: 20px; font-weight: bold;">Connect with me on different platforms:</p>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <a href="https://github.com/jharnob30?tab=repositories" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub" style="transition: transform 0.3s;"/>
                    <span>GitHub</span>
                </div>
            </a>
            <a href="https://www.linkedin.com/feed/" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" alt="LinkedIn" style="transition: transform 0.3s;"/>
                    <span>LinkedIn</span>
                </div>
            </a>
            <a href="https://www.behance.net/jubayerarnob" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/behance.png" alt="Behance" style="transition: transform 0.3s;"/>
                    <span>Behance</span>
                </div>
            </a>
            <a href="https://www.flickr.com/people/189515657@N03/" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/flickr.png" alt="Flickr" style="transition: transform 0.3s;"/>
                    <span>Flickr</span>
                </div>
            </a>
            <a href="https://www.facebook.com/jubayerhossain.arnob.97/" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/facebook.png" alt="Facebook" style="transition: transform 0.3s;"/>
                    <span>Facebook</span>
                </div>
            </a>
            <a href="https://www.instagram.com/j_h_arnob/" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/instagram-new.png" alt="Instagram" style="transition: transform 0.3s;"/>
                    <span>Instagram</span>
                </div>
            </a>
            <a href="https://studio.youtube.com/channel/UCAiYu2MOPo-hYy89ShNWyWQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/youtube-play.png" alt="YouTube" style="transition: transform 0.3s;"/>
                    <span>YouTube</span>
                </div>
            </a>
            <a href="https://medium.com/@jubayerarnob97" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/medium-logo.png" alt="Medium" style="transition: transform 0.3s;"/>
                    <span>Medium</span>
                </div>
            </a>
        </div>
    </div>
    <style>
        a:hover img {
            transform: scale(1.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)
