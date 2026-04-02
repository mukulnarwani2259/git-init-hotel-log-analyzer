import re
from collections import Counter
from io import StringIO

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Hotel Log Analyzer", layout="centered")

st.title("Hotel Log Analyzer")
st.write("Paste log content below to find repetitive patterns (word frequency) sorted by count (descending).")

log_text = st.text_area(
    "Input log file content",
    height=250,
    placeholder="Example:\nINFO   read_physical_table: message 1   This is test mail\nINFO   read_physical_data: message 2    Lets plan outdoor trip\nINFO   read_physical_memory: message 3 : Goa is the best",
)

col1, col2 = st.columns(2)
with col1:
    case_sensitive = st.checkbox("Case sensitive", value=False)
with col2:
    keep_numbers = st.checkbox("Keep numbers (e.g., 123)", value=True)

min_word_len = st.slider("Minimum token length", min_value=1, max_value=10, value=1)

analyze = st.button("Analyze")

def tokenize(text: str, *, case_sensitive: bool, keep_numbers: bool, min_word_len: int) -> list[str]:
    if not case_sensitive:
        text = text.lower()

    # Token pattern:
    # - words with letters/underscore
    # - optionally numbers as tokens
    if keep_numbers:
        pattern = r"[A-Za-z_]+|\d+"
    else:
        pattern = r"[A-Za-z_]+"

    tokens = re.findall(pattern, text)
    tokens = [t for t in tokens if len(t) >= min_word_len]
    return tokens

if analyze:
    if not log_text.strip():
        st.warning("Please paste some log content first.")
    else:
        tokens = tokenize(
            log_text,
            case_sensitive=case_sensitive,
            keep_numbers=keep_numbers,
            min_word_len=min_word_len,
        )

        counts = Counter(tokens)

        if not counts:
            st.info("No tokens found with the current settings.")
        else:
           *

