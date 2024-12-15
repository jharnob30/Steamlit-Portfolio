def custom_css():
    return """
    <style>
    /* General section box styling */
    .section-box {
        border: 1px solid #ddd; /* Subtle border */
        padding: 20px; /* Uniform padding */
        border-radius: 10px; /* Rounded corners */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Light shadow */
        margin-bottom: 20px; /* Spacing between boxes */
    }

    /* Headings inside boxes */
    h4 {
        margin: 0;
        font-size: 18px; /* Unified font size */
    }

    /* Paragraph styling */
    p {
        margin: 5px 0;
    }

    /* Circular image styling */
    .circular-image {
        border-radius: 50%;
        width: 230px;
        height: 230px;
        object-fit: cover;
    }
    </style>
    """
