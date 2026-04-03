import streamlit as st
import collections
import re
import pandas as pd

st.set_page_config(page_title="Hotel Log Analyzer", layout="wide")

st.title("Hotel Log Analyzer")
st.write("Enter your log content below to identify repetitive information and patterns.")

log_input = st.text_area(
    "Input log file content:",
    height=300,
    placeholder="Paste your logs here...",
)


col1, col2 = st.columns([1, 1])
with col1:
    ignore_case = st.checkbox("Ignore case", value=True)
with col2:
    min_count = st.number_input("Minimum count", min_value=1, value=2, step=1)

if st.button("Analyze Logs"):
    if not log_input.strip():
        st.warning("Please paste some log content to begin analysis.")
        st.stop()

    text = log_input.lower() if ignore_case else log_input
    words = re.findall(r"\w+", text)

    if not words:
        st.info("No words found in the input.")
        st.stop()

    word_counts = collections.Counter(words)
    sorted_counts = [(w, c) for (w, c) in word_counts.most_common() if c >= min_count]

    if not sorted_counts:
        st.info("No patterns met the minimum count threshold.")
        st.stop()

    st.subheader("Pattern Analysis")
    for word, count in sorted_counts:
        st.write(f"**{word}** - {count} {'times' if count > 1 else 'time'}")

    st.divider()
    df = pd.DataFrame(sorted_counts, columns=["Pattern/Word", "Count"])
    st.dataframe(df, use_container_width=True)
