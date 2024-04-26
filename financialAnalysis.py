import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    # Drop unnecessary columns
    columns_to_drop = ['Student Name', 'First Name', 'Last Name', 'Sibling Name', 'Adjustment', 'Age', 'Date', 'Charge Category', 'Discount Type']
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')  # Use errors='ignore' to avoid errors if a column doesn't exist
    
    # Check if the columns exist before attempting to manipulate them
    monetary_columns = ['Billing Amount', 'Original Charge', 'Discount Amount']
    for column in monetary_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column].replace('[\$,]', '', regex=True), errors='coerce')
        else:
            print(f"Column {column} not found in DataFrame.")
    
    return df

def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    # Figure 1
    st.title("Financial Analysis")
    st.write("\n\n")
    
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[1]. HISTORY OF Tuition CHARGES: Original Vs. Actual</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Total Revenue over 2 years" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiYjYxNTE4YWUtM2E0ZC00ODMyLThiMmMtZWUyYTE1YjExMGZhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 1: Line Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 2
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[2]. HISTORY OF Tuition CHARGES By Qurater</h4>
    """, unsafe_allow_html=True)
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Revenue by Querter" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiOWYxZDI5ZmUtMGIzZi00NmQwLWFjZTMtZTdmZDllZjM3NWY0IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 2: Line & Clustered Column Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 3
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[3]. PROGRAM CONTRIBUTION TO REVENUE BY Schedule</h4>
    """, unsafe_allow_html=True)
    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Program Schedules Revenue Contribution" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNDkxYjVmNjQtYjRjYS00MDgyLWE1YmYtMDBlYzc2YTA0MTg1IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 3: Ribbon Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 4
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[4]. DISCOUNT DISTRIBUTION Over Two School Years</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Discount Amount by Discount Type" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNGUxODNiMGUtNzk4ZS00YjM4LTlhYzktYjllYjRhOTAwNmNhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 4: Treemap (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 5
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[5]. DISCOUNT DISTRIBUTION For Active Enrollments</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe width="1024" height="612" src="https://lookerstudio.google.com/embed/reporting/3716267f-7edf-4b56-9f90-1ddb3630af02/page/z3GyD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 5: BUBBLE CHART (Google Looker Studio)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 6
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[6]. TUITION STAT SUMMARY For Active Enrollments</h4>
    """, unsafe_allow_html=True)

    file_path = 'students_info.csv'
    df = load_data(file_path)
    
    # Proceed with using df only after verifying the needed columns are present
    if 'Status' in df.columns:
        active_df = df[df['Status'] == 'Active']
        st.write("Data Overview for Active Enrollments:")
        st.write(active_df.describe().round(2))  # Show statistical summary for active enrollments
        st.subheader("Figure 2: Description Summary Table (Python)")
        st.write("\n\n")
        st.subheader("Analysis")
        st.write("Analyze here")

    else:
        st.error("Required columns are missing from the data.")


    if __name__ == "__main__":
        main()
        
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 7
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[7]. PROGRAM TUITION BILLING BY MONTH For Active Students</h4>
    """, unsafe_allow_html=True)
    
    
