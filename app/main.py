import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Custom CSS for better styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply custom CSS styling directly
def set_custom_css():
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50; /* Green background */
            border: none; /* Remove borders */
            color: white; /* White text */
            padding: 10px 24px; /* Some padding */
            text-align: center; /* Centered text */
            text-decoration: none; /* Remove underline */
            display: inline-block; /* Get the element to line up with others */
            font-size: 16px; /* Increase font size */
            margin: 4px 2px; /* Some margin */
            cursor: pointer; /* Pointer/hand icon */
            border-radius: 8px; /* Rounded corners */
        }
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50; /* Green border */
            padding: 8px;
            border-radius: 5px;
        }
        .main {
            background-color: #f9f9f9; /* Light grey background */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1); /* Shadow */
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

def create_streamlit_app(chain, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="📧 Cold Email Generator", page_icon="📧")
    
    # Apply custom CSS
    set_custom_css()

    st.title("📧 Cold Mail Generator")
    st.markdown("### 💼 Generate effective cold emails for job postings and portfolio links 💼")
    st.markdown("---")  # Add a horizontal line for separation

    url_input = st.text_input("🔗 Enter a Job URL:")
    submit_button = st.button("🚀 Generate Email")

    if submit_button:
        try:
            with st.spinner("🕵️‍♂️ Scraping and analyzing the job posting..."):
                loader = WebBaseLoader(url_input)
                data = clean_text(loader.load().pop().page_content)
                # st.write(data)
            
            with st.spinner("📂 Loading portfolio data..."):
                portfolio.load_portfolio()
                st.write("✅ Portfolio data loaded successfully.")

            jobs = chain.extract_jobs(data)

            # st.write(jobs)

            # Ensure jobs is a list or single dictionary
            if isinstance(jobs, dict):
                jobs = [jobs]  # Wrap in a list if it's a single dictionary

            for job in jobs:
                st.markdown(f"### 📝 Job Role: {job.get('role', 'Unknown Role')}")
                skills = job.get('skills', [])
                st.markdown(f"**Required Skills:** {', '.join(skills)}")

                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links) 
                
                st.markdown("#### 📧 Generated Cold Email:")
                st.code(email, language='markdown')
                st.markdown("---")

        except Exception as e:
            st.error(f"🚨 An Error Occurred: {e}")

if __name__ == "__main__":

    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
