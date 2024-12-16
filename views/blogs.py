import streamlit as st
from datetime import datetime

# Define the blogs with categories, titles, dates, and images
blogs = [
    {
        "category": "AI/Technology",
        "title": "AI-Generated Videos: Fun or Unsettling?",
        "date": "2024-12-17",
        "image": "assets/image2.jpg",  # Replace with your image path or URL
        "content": """
        Today, while scrolling through Facebook, I came across two AI-generated videos. In one, a bunch of pandas gathered around a dinner table enjoying ramen and beer. It looked fun, but it didn’t quite sit right with me—I’ll explain why. The other video showed a crew on a ship having fun with a baby polar bear, and it looked so real it genuinely freaked me out.
        
        Let’s get to the point why I didn’t like it much. I’m someone who values real, tangible experiences. When fantasy starts blending with reality in ways that make it hard to tell what’s real and what’s not, it’s unsettling. The idea that people could mistake something fake for something genuine is scary to me.
        
        These can be fun to watch, but on the other hand, AI-generated content mostly freaks me out. I don’t get much enjoyment or satisfaction from these things anymore.
        """
    },
    {
        "category": "Life",
        "title": "A Day Full of Surprises: Blood Donation, Weddings, and Family Gatherings",
        "date": "2024-12-16",
        "image": "assets/image2.jpg",  # Replace with your image path or URL
        "content": """
        Today, I went to Gonoshasthaya Kendra for a blood donation. About half a week ago, my co-worker Dukul Bhai asked if I could help someone in need by donating blood, and I agreed. After our conversation, I told my family that I’d be going to Dhanmondi for the donation, and that’s when I found out we’d be celebrating my niece’s birthday on Friday with a family gathering. Then, when I met my friend Shahriour, he informed me that our friend Faiaz’s wedding was also scheduled for Friday, and I was invited as well. It felt like everything was happening on the same day!
        
        When I asked Dukul Bhai if he could find someone else to donate, he tried but couldn’t, so he asked again if I could come. I agreed to come around noon. I didn’t know the timing of the wedding, but I knew the birthday celebration would be from evening until night, so I planned to be back by 6 pm to help with the decorations.
        
        While I was traveling to Dhanmondi, my friends Araf and Shahriour called to check if I was coming to the wedding. That’s when I found out the wedding ceremony was right after Jumma, at noon! I had missed it. I told them I’d come as soon as I was done with the blood donation to at least spend 5-10 minutes with Faiaz.
        
        Now, I had to rush back to Uttara even faster to make it to both the wedding and the family party. The real problem was that, initially, I didn’t know about either the wedding or the family party, so I had already made plans with my girlfriend to go on a date after my donation. When I found out about everything today, I asked her if we could reschedule our date to next Friday, explaining that I needed to attend these events and couldn’t spend much time with her today. Unfortunately, this led to a fight, and now she’s upset. I’m starting to question if she’s really the understanding partner I need, and it’s making me nervous about the idea of marriage.
        
        The whole day felt like one mishap after another. To top it off, the person I was donating blood for was delayed with her paperwork, so I couldn’t leave the clinic until after 4 pm, even though I could’ve been done by 3:10 pm. That was when it became clear I wouldn’t be able to meet my girlfriend today, realizing that the delay would affect everything else. Luckily, I still managed to catch Faiaz for a couple of minutes before he left in his car. Now, I’m at the family party after helping with the decorations. Today has been quite a whirlwind!
        """
    },
    {
        "category": "Movies",
        "title": "Perfect Days | My Favorite Movie of 2024",
        "date": "2024-12-14",
        "image": "assets/image2.jpg",  # Replace with your image path or URL
        "content": """
        A movie based on a simple life. It follows a solitary man, Hirayama, who finds comfort in a quiet, routine life. Though his days look the same, small changes remind us that no day is truly perfect. Hirayama silently carries his pain inside, but a visit from his niece stirs his emotions. In the end, as he drives to work, his expression reveals the emotions he's been keeping inside while maintaining his perfect days.
        
        **Hirayama’s admirable qualities:**
        
        1. Appreciation for Life
        2. Contentment in Simplicity
        3. Self-discipline
        4. Mindfulness
        5. Sense of responsibility.
        
        - Practicing these qualities can make anyone a better person.
        
        **Notable mindful activities:**
        
        1. Appreciating moments by capturing and organizing photos in a month-based library.
        2. Reading a physical book each night, only buying a new one when he’s finished the last.
        3. Keeping a collection of classical music cassettes, enjoying music on his way to work.
        4. Observing nature in solitude, creating a soulful connection to the world around him.
        
        - Adopting some of these can lead to a more meaningful and fulfilling life experience.
        
        **Notable Quotes/ Words**
        
        1. Hirayama - "Next time is next time. Now is now."
        2. KOMOREBI (Japanese Word) - means the shimmering of light and shadows that is created by leaves swaying in the wind. It only exists once, AT THAT MOMENT.
        3. Businessman - One stop living when one no longer knows anything.
        """
    },
]

# Sidebar for filtering by category
categories = sorted(set([blog["category"] for blog in blogs]))
selected_category = st.sidebar.selectbox("Filter by Category", ["All"] + categories)

# Filter blogs based on the selected category
filtered_blogs = blogs if selected_category == "All" else [blog for blog in blogs if blog["category"] == selected_category]

# Display Blogs in expandable sections
st.header(f"Blogs ({selected_category if selected_category != 'All' else 'All Categories'})")

# Loop through blogs and display them in collapsible sections
for blog in filtered_blogs:
    with st.expander(f"{blog['title']} ({blog['category']})"):
        # Display the image and content
        col1, col2 = st.columns([3, 1])  # Adjust the ratio as per your requirement
        with col2:
            st.image(blog["image"], width=300)  # Image with consistent sizing
        with col1:
            # Format date and show a small snippet first
            formatted_date = datetime.strptime(blog["date"], "%Y-%m-%d").strftime("%B %d, %Y")
            st.markdown(f"**Date:** {formatted_date}")
            st.markdown(f"**Category:** {blog['category']}")
            st.markdown(f"{blog['content'][:300]}...")  # Show first 300 characters as an excerpt
            
            # Button to open the full post
            if st.button(f"Read full article: {blog['title']}"):
                st.write(blog["content"])  # This will reveal the full content in the current view
