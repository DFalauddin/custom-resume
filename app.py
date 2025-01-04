import streamlit as st
import pandas as pd
import PyPDF2
import docx
import requests
from io import BytesIO
import re
import json
import time

# Add these to your requirements.txt:
# python-docx==0.8.11
# PyPDF2==3.0.1
# requests==2.31.0
# beautifulsoup4==4.12.2

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
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
    """Extract text from DOCX file"""
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
    """Extract job details from LinkedIn URL"""
    try:
        # This is a placeholder. In a real implementation, you would need to:
        # 1. Use LinkedIn API or web scraping (following LinkedIn's terms of service)
        # 2. Handle authentication and rate limiting
        # 3. Parse the job description properly
        
        # For demo purposes, we'll return a mock response
        job_details = {
            "title": "Sample Job Title",
            "description": "This is a sample job description with key requirements...",
            "requirements": ["Python", "Machine Learning", "Data Analysis"],
            "company": "Sample Company"
        }
        return job_details
    except Exception as e:
        st.error(f"Error extracting job details: {str(e)}")
        return None

def customize_resume(resume_text, job_details):
    """Customize resume based on job details"""
    try:
        # This is where you would implement your AI logic
        # For demo purposes, we'll simulate processing time
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
        
        # Return a mock customized resume
        return f"""
        CUSTOMIZED RESUME
        
        PROFESSIONAL SUMMARY
        Experienced professional with skills matching {job_details['title']} requirements.
        
        HIGHLIGHTED SKILLS
        {', '.join(job_details['requirements'])}
        
        [Rest of resume content would go here...]
        """
    except Exception as e:
        st.error(f"Error customizing resume: {str(e)}")
        return None

def create_upload_section():
    st.markdown("### 📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or DOCX)",
        type=["pdf", "docx"],
        help="We accept PDF and DOCX formats"
    )
    
    if uploaded_file:
        # Show file details
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.2f} KB",
            "File type": uploaded_file.type
        }
        st.write("File Details:", file_details)
        
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)
        
        if resume_text:
            st.session_state['resume_text'] = resume_text
            st.success("Resume uploaded successfully!")
            return True
    return False

def create_job_link_section():
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
                return True
        else:
            st.error("Please enter a valid LinkedIn job URL")
    return False

def create_customize_section():
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
                
                # Display preview
                st.markdown("### Preview")
                st.text_area("Customized Resume", customized_resume, height=300)
                
                # Download button
                st.download_button(
                    label="Download Customized Resume",
                    data=customized_resume,
                    file_name="customized_resume.txt",
                    mime="text/plain"
                )

def main():
    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state['step'] = 1

    # Create tabs for each step
    tab1, tab2, tab3 = st.tabs(["Upload Resume", "Add Job Link", "Get Custom Resume"])
    
    with tab1:
        if create_upload_section():
            st.session_state['step'] = 2
    
    with tab2:
        if create_job_link_section():
            st.session_state['step'] = 3
    
    with tab3:
        create_customize_section()

if __name__ == "__main__":
    main()
