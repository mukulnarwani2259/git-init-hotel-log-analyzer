import streamlit as st
import collections
import re
import pandas as pd

st.set_page_config(page_title="Hotel Log Analyzer", layout="wide")

st.title("Hotel Log Analyzer")
st.write("Enter your log content below to identify repetitive information and patterns.")

log_input = st.text_area("Input log file content:", height=300, placeholder="Paste your logs here...")

if st.button("Analyze Logs"):
    if log_input.strip():
        words = re.findall(r'\w+', log_input)
        word_counts = collections.Counter(words)
        sorted_counts = word_counts.most_common()

        st.subheader("Pattern Analysis")
        for word, count in sorted_counts:
            st.write(f"**{word}** - {count} {'times' if count > 1 else 'time'}")

        st.divider()
        df = pd.DataFrame(sorted_counts, columns=["Pattern/Word", "Count"])
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Please paste some log content to begin analysis.")
