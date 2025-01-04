import streamlit as st
import base64
from datetime import datetime, timezone

# Page configuration
st.set_page_config(
    page_title="ResumeAI - Smart Resume Customization",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with !important tags and direct element styling
st.markdown("""
    <style>
        /* Main Page Styling */
        .main {
            padding: 2em;
        }
        
        /* Header Styling */
        .main-header {
            color: #1a73e8 !important;
            font-family: 'Helvetica Neue', sans-serif !important;
            font-size: 3.5em !important;
            font-weight: 700 !important;
            text-align: center !important;
            padding: 1em 0 0.5em 0 !important;
            margin-bottom: 0.5em !important;
        }
        
        .sub-header {
            color: #5f6368 !important;
            font-family: 'Helvetica Neue', sans-serif !important;
            font-size: 1.5em !important;
            text-align: center !important;
            margin-bottom: 2em !important;
        }
        
        /* Section Headers */
        h2 {
            color: #1a73e8 !important;
            font-family: 'Helvetica Neue', sans-serif !important;
            font-size: 2em !important;
            text-align: center !important;
            margin: 1.5em 0 !important;
            padding-top: 1em !important;
        }
        
        /* Feature Cards */
        .feature-card {
            background-color: white !important;
            padding: 2em !important;
            border-radius: 10px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            height: 100% !important;
            margin: 1em !important;
            transition: transform 0.3s ease !important;
        }
        
        .feature-card:hover {
            transform: translateY(-5px) !important;
        }
        
        /* Pricing Cards */
        .pricing-card {
            background-color: white !important;
            padding: 2em !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            text-align: center !important;
            height: 100% !important;
            margin: 1em !important;
            transition: transform 0.3s ease !important;
        }
        
        .pricing-card:hover {
            transform: translateY(-5px) !important;
        }
        
        /* Buttons */
        .cta-button {
            background-color: #1a73e8 !important;
            color: white !important;
            padding: 0.8em 2em !important;
            border-radius: 30px !important;
            text-decoration: none !important;
            font-weight: 600 !important;
            display: inline-block !important;
            margin: 1em 0 !important;
            transition: background-color 0.3s ease !important;
        }
        
        .cta-button:hover {
            background-color: #1557b0 !important;
            text-decoration: none !important;
            color: white !important;
        }
        
        /* Lists */
        ul {
            list-style-type: none !important;
            padding: 0 !important;
        }
        
        li {
            margin: 0.5em 0 !important;
            color: #5f6368 !important;
        }
        
        /* Footer */
        .footer {
            text-align: center !important;
            padding: 2em !important;
            margin-top: 3em !important;
            border-top: 1px solid #eee !important;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Divider */
        hr {
            margin: 2em 0 !important;
            border-color: #eee !important;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-header {
                font-size: 2.5em !important;
            }
            .sub-header {
                font-size: 1.2em !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

def create_hero_section():
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

def create_how_it_works():
    st.markdown('<h2>How It Works</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    steps = [
        {
            "title": "1. Upload Resume",
            "description": "Simply upload your existing resume in any common format (PDF, DOCX, etc.)"
        },
        {
            "title": "2. Add Job Link",
            "description": "Paste the LinkedIn job posting URL you're interested in"
        },
        {
            "title": "3. Get Your Custom Resume",
            "description": "Receive your tailored resume optimized for the specific job in seconds"
        }
    ]
    
    for col, step in zip(cols, steps):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <h3>{step['title']}</h3>
                    <p>{step['description']}</p>
                </div>
            """, unsafe_allow_html=True)

def create_features():
    st.markdown('<h2>Key Features</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>AI-Powered Customization</h3>
                <ul>
                    <li>✨ Smart keyword optimization</li>
                    <li>🎯 Skills matching</li>
                    <li>📊 Experience highlighting</li>
                    <li>✅ ATS-friendly formatting</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3>Professional Features</h3>
                <ul>
                    <li>📁 Multiple format export options</li>
                    <li>🔄 Version history</li>
                    <li>👁️ Real-time preview</li>
                    <li>🚀 One-click application ready</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

def create_pricing():
    st.markdown('<h2>Pricing Plans</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    plans = [
        {
            "name": "Basic",
            "price": "Free",
            "features": ["3 resume customizations/month", "Basic formatting", "PDF export"],
            "cta": "Start Free",
            "highlight": False
        },
        {
            "name": "Pro",
            "price": "$19/month",
            "features": ["Unlimited customizations", "Advanced AI optimization", "All export formats", "Priority support"],
            "cta": "Go Pro",
            "highlight": True
        },
        {
            "name": "Enterprise",
            "price": "Custom",
            "features": ["Team management", "API access", "Custom integration", "Dedicated support"],
            "cta": "Contact Us",
            "highlight": False
        }
    ]
    
    for col, plan in zip(cols, plans):
        with col:
            style = 'border: 2px solid #1a73e8;' if plan['highlight'] else ''
            st.markdown(f"""
                <div class="pricing-card" style="{style}">
                    <h3>{plan['name']}</h3>
                    <h2>{plan['price']}</h2>
                    <ul>
                        {''.join(f'<li>{feature}</li>' for feature in plan['features'])}
                    </ul>
                    <a href="#" class="cta-button">{plan['cta']}</a>
                </div>
            """, unsafe_allow_html=True)

def footer():
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("Version: 1.0.0")
    with col2:
        st.markdown("Last Updated: 2025-01-04")
    with col3:
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        st.markdown(f"Current Time: {current_time}")

def main():
    create_hero_section()
    create_how_it_works()
    create_features()
    create_pricing()
    footer()

if __name__ == "__main__":
    main()
