def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    st.title("Active Enrollment Trends")
    st.write("\n\n")
    
    # Figure 1
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[1]. STUDENT COUNTS DISTRIBUTION BY PROGRAM AND SCHEDULE</h4>
    """, unsafe_allow_html=True)
    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Students Counts by Program" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiMjk2NjhhOGYtYzE1NS00ZjBkLWFkZWQtZmJjMGZiMDU3YzdkIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 1: Pi Chart & Table Matrix (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")

    # Figure 2
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[2]. ACTIVE STUDENTS DASHBOARD</h4>
    """, unsafe_allow_html=True)
    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe src="https://prod-useast-b.online.tableau.com/t/samirtarda707500432c/views/Dashboard/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no" width="1024" height="825"></iframe>', unsafe_allow_html=True)
    st.subheader("Figure 2: Bar Chart & Stacked Bar Chart (Tableau)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
