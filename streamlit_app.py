import streamlit as st
import pandas as pd

def main():
    st.title("CSV Data Viewer")

    # Load CSV file
    file_path = "Stunting_Dataset.csv"  # Specify the path to your CSV file here
    df = pd.read_csv(file_path)

    # Display the DataFrame
    st.write("### Data from CSV file")
    st.write(df)

if __name__ == "__main__":
    main()
