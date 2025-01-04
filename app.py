import streamlit as st
import base64
from datetime import datetime, timezone
import PyPDF2
import docx
import requests
from io import BytesIO
import time

# Page configuration
st.set_page_config(
    page_title="ResumeAI - Smart Resume Customization",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS (keeping your existing CSS)
st.markdown("""
    <style>
        /* Your existing CSS styles here */
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state['step'] = 1
if 'resume_text' not in st.session_state:
    st.session_state['resume_text'] = None
if 'job_details' not in st.session_state:
    st.session_state['job_details'] = None

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def extract_text_from_docx(docx_file):
    try:
        doc = docx.Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading DOCX: {str(e)}")
        return None

def extract_job_details(linkedin_url):
    # Mock implementation
    return {
        "title": "Sample Job Title",
        "description": "This is a sample job description with key requirements...",
        "requirements": ["Python", "Machine Learning", "Data Analysis"],
        "company": "Sample Company"
    }

def customize_resume(resume_text, job_details):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    steps = [
        "Analyzing resume...",
        "Extracting key skills...",
        "Matching with job requirements...",
        "Optimizing content...",
        "Generating final resume..."
    ]
    
    for i, step in enumerate(steps):
        status_text.text(step)
        progress_bar.progress((i + 1) * 20)
        time.sleep(1)
    
    return f"""
    CUSTOMIZED RESUME
    
    PROFESSIONAL SUMMARY
    Experienced professional with skills matching {job_details['title']} requirements.
    
    HIGHLIGHTED SKILLS
    {', '.join(job_details['requirements'])}
    
    [Rest of resume content would go here...]
    """

def show_landing_page():
    st.markdown('<h1 class="main-header">Transform Your Resume with AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Get a perfectly tailored resume for every job application in seconds</p>', unsafe_allow_html=True)

def show_resume_tool():
    tabs = st.tabs(["Upload Resume", "Add Job Link", "Get Custom Resume"])
    
    with tabs[0]:
        st.markdown("### 📄 Upload Your Resume")
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF or DOCX)",
            type=["pdf", "docx"],
            help="We accept PDF and DOCX formats"
        )
        
        if uploaded_file:
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024:.2f} KB",
                "File type": uploaded_file.type
            }
            st.write("File Details:", file_details)
            
            if uploaded_file.type == "application/pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)
            
            if resume_text:
                st.session_state['resume_text'] = resume_text
                st.success("Resume uploaded successfully!")
                st.session_state['step'] = 2
    
    with tabs[1]:
        st.markdown("### 🔗 Add Job Link")
        job_url = st.text_input(
            "Paste the LinkedIn job URL",
            placeholder="https://www.linkedin.com/jobs/view/...",
            help="Enter the full LinkedIn job posting URL"
        )
        
        if job_url:
            if "linkedin.com/jobs" in job_url.lower():
                job_details = extract_job_details(job_url)
                if job_details:
                    st.session_state['job_details'] = job_details
                    st.success("Job details extracted successfully!")
                    st.session_state['step'] = 3
            else:
                st.error("Please enter a valid LinkedIn job URL")
    
    with tabs[2]:
        st.markdown("### ✨ Get Your Customized Resume")
        
        if 'resume_text' not in st.session_state or 'job_details' not in st.session_state:
            st.warning("Please complete the previous steps first!")
            return
        
        if st.button("Generate Customized Resume"):
            with st.spinner("Customizing your resume..."):
                customized_resume = customize_resume(
                    st.session_state['resume_text'],
                    st.session_state['job_details']
                )
                
                if customized_resume:
                    st.success("Resume customized successfully!")
                    st.markdown("### Preview")
                    st.text_area("Customized Resume", customized_resume, height=300)
                    
                    st.download_button(
                        label="Download Customized Resume",
                        data=customized_resume,
                        file_name="customized_resume.txt",
                        mime="text/plain"
                    )

def main():
    show_landing_page()
    show_resume_tool()

if __name__ == "__main__":
    main()
