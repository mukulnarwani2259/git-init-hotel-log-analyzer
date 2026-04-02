import streamlit as st
    import collections
    import re
    import pandas as pd
    
    st.set_page_config(page_title="Hotel Log Analyzer", layout="wide")
    
    st.title("🏨 Hotel Log Analyzer")
    st.write("Enter your log content below to identify repetitive information and patterns.")
    
    # Requirement: Text box for input log file content
    log_input = st.text_area("Input log file content:", height=300, placeholder="Paste your logs here...")
    
    if st.button("Analyze Logs"):
        if log_input.strip():
            # Clean and tokenize: Remove special characters and split into words
            # This covers patterns like 'INFO', 'read_physical_table', etc.
            words = re.findall(r'\w+', log_input)
            
            # Count occurrences
            word_counts = collections.Counter(words)
            
            # Sort by count in descending order as per requirement
            sorted_counts = word_counts.most_common()
            
            # Display Results
            st.subheader("Expected Output (Pattern Analysis)")
            
            # Create a formatted list for the specific requirement style
            for word, count in sorted_counts:
                st.write(f"**{word}** – {count} {'times' if count > 1 else 'time'}")
                
            # Also provide a tabular view for better readability
            st.divider()
            df = pd.DataFrame(sorted_counts, columns=['Pattern/Word', 'Count'])
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("Please paste some log content to begin analysis.")
    
