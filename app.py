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

# Rest of your code remains the same as in the previous response...

# Add version info at the bottom of the footer
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

# Add the footer call at the end of your main() function
if __name__ == "__main__":
    main()
    footer()
