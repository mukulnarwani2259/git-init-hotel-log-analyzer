import streamlit as st
    import pandas as pd
    import re
    
    st.set_page_config(page_title="Hotel Log Analyzer", layout="wide")
    
    st.title("🏨 Hotel Log Analyzer")
    st.write("Upload your hotel system logs to extract guest activity automatically.")
    
    uploaded_file = st.file_uploader("Choose a log file (.txt or .log)", type=["txt", "log"])
    
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        
        # Simple regex to find patterns like: [2023-10-01] Guest: John Doe - Action: Check-in
        pattern = r"\[(?P<date>.*?)\]\s+Guest:\s+(?P<guest>.*?)\s+-\s+Action:\s+(?P<action>.*)"
        
        matches = [m.groupdict() for m in re.finditer(pattern, content)]
        
        if matches:
            df = pd.DataFrame(matches)
            st.subheader("Parsed Log Data")
            st.dataframe(df, use_container_width=True)
            
            # Summary Metrics
            col1, col2 = st.columns(2)
            col1.metric("Total Entries", len(df))
            col2.metric("Unique Guests", df['guest'].nunique())
        else:
            st.error("No valid log patterns found. Please ensure logs match the expected format.")
    
