import streamlit as st
from preprocessing import function_out

# Set page config
st.set_page_config(
    page_title="Rate My Review",
    page_icon="⭐",
    layout="centered"
)

# Title and description
st.title("Rate My Review 📝")
st.markdown("""
This application analyzes reviews and rates them on a scale of 1-5, with corresponding experience labels:
- 1: Worst Experience
- 2: Bad Experience
- 3: Average Experience
- 4: Good Experience
- 5: Excellent Experience
""")

# Input text area
review_text = st.text_area("Enter your review here:", height=150)

# Process button
if st.button("Analyze Review"):
    if review_text:
        with st.spinner("Analyzing review..."):
            result = function_out(review_text)
            if result:
                rating, experience = result
                
                # Display rating with stars
                st.subheader("Rating:")
                st.write("⭐" * rating)
                
                # Display experience label
                st.subheader("Experience Category:")
                st.write(experience.title())
                
                # Add a progress bar for visualization
                st.progress(rating/5)
    else:
        st.warning("Please enter a review first!")