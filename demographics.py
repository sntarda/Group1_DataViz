def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    st.title("Enrollment Demographics")
    st.write("\n\n")
        
    # Figure 1
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[1]. CLASSROOMS DEMOGRAPHICS BY AGE AND GENDER</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Program Age Group" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiZDUyNDIwZjQtMDkwYS00ZDQ0LWExZDYtZDFjZmVkNzJmODQzIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html = True)
    st.subheader("Figure 1: Table Matrix (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    

    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 2
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[2]. ACTIVE STUDENTS DEMOGRAPHICS BY CITY</h4>
    """, unsafe_allow_html=True)
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe title="Top Cities for School Enrollment (Heatmap)" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=4ec16432-4288-4f32-8aeb-bbdcb9237ab1&autoAuth=true&ctid=70de1992-07c6-480f-a318-a1afcba03983" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html = True)
    st.subheader("Figure 2: Filled Heatmap (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 3
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[3]. ACTIVE STUDENTS DEMOGRAPHICS BY CITY</h4>
    """, unsafe_allow_html=True)
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe src="https://prod-useast-b.online.tableau.com/t/samirtarda707500432c/views/StudentsDemographics/Sheet1?:embed=y&:display_count=yes&:showVizHome=no" width="1024" height="825"></iframe>', unsafe_allow_html=True)
    st.subheader("Figure 3: Heatmap (Tableau)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    
