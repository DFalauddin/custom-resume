import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from datetime import datetime, timezone

# Page configuration
st.set_page_config(
    page_title="ResumeAI - Smart Resume Customization",
    page_icon="📄",
    layout="wide"
)

# Version info and last updated
VERSION = "1.0.0"
LAST_UPDATED = "2025-01-04"

# Custom CSS
def local_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8f9fa;
        }
        
        .custom-container {
            background-color: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
        }
        
        .main-header {
            font-size: 3.5rem;
            font-weight: 700;
            color: #1a73e8;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .sub-header {
            font-size: 1.5rem;
            color: #5f6368;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .feature-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            height: 100%;
        }
        
        .pricing-card {
            background-color: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            height: 100%;
        }
        
        .cta-button {
            background-color: #1a73e8;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 2rem;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            margin: 1rem 0;
            text-align: center;
        }
        
        .cta-button:hover {
            background-color: #1557b0;
            color: white;
        }
        </style>
    """)

def footer():
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"Version: {VERSION}")
    with col2:
        st.markdown(f"Last Updated: {LAST_UPDATED}")
    with col3:
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        st.markdown(f"Current Time: {current_time}")

def main():
    local_css()
    
    # Hero Section
    st.markdown('<h1 class="main-header">Transform Your Resume with AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Get a perfectly tailored resume for every job application in seconds</p>', unsafe_allow_html=True)
    
    # Main CTA
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <a href="#" class="cta-button">Try It Free</a>
            </div>
        """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("---")
    st.markdown('<h2 style="text-align: center;">How It Works</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>1. Upload Resume</h3>
                <p>Simply upload your existing resume in any common format (PDF, DOCX, etc.)</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3>2. Add Job Link</h3>
                <p>Paste the LinkedIn job posting URL you're interested in</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <h3>3. Get Your Custom Resume</h3>
                <p>Receive your tailored resume optimized for the specific job in seconds</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("---")
    st.markdown('<h2 style="text-align: center;">Key Features</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="custom-container">
                <h3>AI-Powered Customization</h3>
                <ul>
                    <li>Smart keyword optimization</li>
                    <li>Skills matching</li>
                    <li>Experience highlighting</li>
                    <li>ATS-friendly formatting</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="custom-container">
                <h3>Professional Features</h3>
                <ul>
                    <li>Multiple format export options</li>
                    <li>Version history</li>
                    <li>Real-time preview</li>
                    <li>One-click application ready</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Pricing Section
    st.markdown("---")
    st.markdown('<h2 style="text-align: center;">Pricing Plans</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="pricing-card">
                <h3>Basic</h3>
                <h2>Free</h2>
                <ul style="list-style-type: none; padding: 0;">
                    <li>3 resume customizations/month</li>
                    <li>Basic formatting</li>
                    <li>PDF export</li>
                </ul>
                <a href="#" class="cta-button">Start Free</a>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="pricing-card" style="border: 2px solid #1a73e8;">
                <h3>Pro</h3>
                <h2>$19/month</h2>
                <ul style="list-style-type: none; padding: 0;">
                    <li>Unlimited customizations</li>
                    <li>Advanced AI optimization</li>
                    <li>All export formats</li>
                    <li>Priority support</li>
                </ul>
                <a href="#" class="cta-button">Go Pro</a>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="pricing-card">
                <h3>Enterprise</h3>
                <h2>Custom</h2>
                <ul style="list-style-type: none; padding: 0;">
                    <li>Team management</li>
                    <li>API access</li>
                    <li>Custom integration</li>
                    <li>Dedicated support</li>
                </ul>
                <a href="#" class="cta-button">Contact Us</a>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    footer()
