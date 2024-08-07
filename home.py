import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def create_contribution_table():
    # Data for the table
    data = {
        "Tasks": ["Project Proposal", "Dataset Preparation", "Visualization Graphs", "Website Design", "Meetings & Communication", "Presentation Slides", "Presentation Participation"],
        "Samir": ["100%", "100%", "50%", "Support", "100%", "50%", "Present & Active"],
        "Uzair": ["Support", "Support", "50%", "100%", "100%", "50%", "Present & Active"],
        "Vamsi": ["Support", "0", "0", "0", "20%", "0", "0"],
        "Venkatesh": ["Support", "0", "Support", "0", "20%", "0", "0"]
    }
    contributions = pd.DataFrame(data)
    return contributions

def main():
    st.markdown("<h1 style='text-align: center;'>FINAL GROUP PROJECT</h1>", unsafe_allow_html=True)

    # Enhanced header styles
    st.markdown("""
    <h2 style='text-align: center;'>CSCE 5320.003: Scientific Data Visualization</h2>
    <h3 style='text-align: center;'>PROJECT TITLE: School Strategic Analytics | Finance & Enrollment</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h3 style='text-align: center; font-weight: bold; color: #3478f6; margin-bottom: -10px;'>GROUP 1 MEMBERS:</h3>
    <p style='text-align: center; margin-top: 0px; font-size: 20px; font-weight: bold;'>Samir Tarda, Uzair Naeem, Vamsi Krishna, and Venkatesh Thentu</p>
    """, unsafe_allow_html=True)

    # Divider
    st.image('top_data-science-divider-1.png', width=700, output_format='auto')
    st.write("\n\n")

    # Project Introduction using Markdown with HTML for styling
    st.markdown("""
    <div style='text-align: justify;'>
        <strong><em>Welcome to our project homepage. This project is designed to provide strategic insights 
        into school operations, focusing on finance and enrollment metrics. Explore various tabs to 
        see interactive visualizations and gain a deeper understanding of the data.</em></strong>
    </div>
    """, unsafe_allow_html=True)

    # Image example with custom width and center alignment
    st.write("\n")
    st.image('data-analytics1.jpg', width=700, output_format='auto')
    st.image('data-analytics2.png', width=700, output_format='auto')
    st.image('workflowdiagram.jpg', width=700, output_format='auto')
    
    # Divider
    st.image('top_data-science-divider-1.png', width=700, output_format='auto')
    st.write("\n\n")
    
    # Column layout for insights and actions with better visual formatting
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Insights")
        st.markdown("""
        * Overview of enrollment trends
        * Financial performance analysis
        * Program contributions to revenue
        * School demographics
        """)
    with col2:
        st.markdown("## Actions")
        st.markdown("""
        * Adjust resource allocation based on trends
        * Plan for future enrollment changes
        * Optimize financial strategies
        * Revisit and adjust marketing strategies to compensate for the decrease in enrollment
        """)

    # Divider
    st.image('top_data-science-divider-1.png', width=700, output_format='auto')
    st.write("\n\n")
    
    st.markdown("""
    <div style='text-align: left;'>
        <h3>GROUP MEMBERS CONTRIBUTION</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create and display the contribution table
    contributions = create_contribution_table()
    
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(contributions)
    gb.configure_default_column(editable=True, groupable=True)
    gb.configure_column("Tasks", editable=False)
    grid_options = gb.build()
    
    # Display the table with AgGrid
    AgGrid(contributions, gridOptions=grid_options, enable_enterprise_modules=True)
