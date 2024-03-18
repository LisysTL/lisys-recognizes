# read_csv_app.py
import streamlit as st
import pandas as pd

# from util import set_background

# set_background('pix/3.png')

def main():
    st.title("Read CSV File")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Display DataFrame
        st.write("CSV file content:")
        st.dataframe(df)

if __name__ == "__main__":
    main()
