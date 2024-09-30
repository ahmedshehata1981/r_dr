import streamlit as st
import numpy as np
import pandas as pd
import pyodbc

def fetch_and_display_data():
    # Connect to the database
    server = ''
    database = ''
    username = ''
    password = ''
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()

    # Execute the query
    query1 = '''SELECT
        TOP 10000
        [dbo].[11-dr_delivery].[dr_delivery_no],
        FORMAT([dbo].[11-dr_delivery].[ddate],'MM-dd-yyyy') AS "dr_date"
    FROM
        [dbo].[11-dr_delivery]
    ORDER BY
        [dbo].[11-dr_delivery].[ddate] DESC;'''
    r_dr = pd.read_sql(query1, conn)

    # Display the data in a Streamlit table
    st.dataframe(r_dr)

    # Provide an option to download the data as an Excel file
    st.download_button(
        label='Download as Excel',
        data=r_dr.to_csv(index=False, encoding='utf-8').encode(),
        file_name='R-DR.csv'
    )

    # Close the database connection
    conn.close()

# Main Streamlit app
st.title('SQL Server Data Retrieval')
st.button('Fetch Data', on_click=fetch_and_display_data)
