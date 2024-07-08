import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
import plotly.express as px
import seaborn as sns
from base64 import b64encode
import altair as alt
def web_portfolio():
    st.set_page_config(page_title="Jamla Ahmad's Portfolio",page_icon="👨‍💻")
    page=st.sidebar.radio("Go To",["Home","About","Project","Education","Skills & Certifications","Contact"])
    if page=="Home":
        st.write(f"""
             <div class="title" style="text-align:center;">
             <span style='font-size:32px'>Hello! My name is Jamal Ahmad </span>👋
             </div>
             """,unsafe_allow_html=True)
        st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)
        with open("jam.jpeg","rb")as img_file:
            img="data:image/jpeg;base64,"+ b64encode(img_file.read()).decode()
        #st.write(f"""
        #<div style="display:flex;justify-content:center;">
        #<div class ="box">
        #<img src="{img}" alt="Jamal Ahmad" style="width:200px;height:300px;">
        #</div>
        #</div>
        #""",
        #unsafe_allow_html=True)
            st.write(f"""
            <style>
             @keyframes slowTilt {{
             0%,100%{{
             transform: rotate(0deg);
            }}
            50% {{
            transform:rotate(5deg);
            }}
            }}
            .box img {{
            width:200px;
            height:220px;
            
            border-radius:50%;
            animation: slowTilt 2s ease-in-out infinite;
             }}
         </style>
         <div style="display : flex; justify-content:center;">
         <div class="box">
         <img src="{img}">
         </div>
         </div>
         """,
         unsafe_allow_html=True)
        st.write(f"""
                <div class=
                "subtitle" style="text-align:center;">Computer Science Engineering Student-AI&ML</div>
                """,
                unsafe_allow_html=True)
        st.write(f"""
                    <div class=
                     "title"=style="text-align:left;color:#ffff00;"> <!-- Wite text color -->
                     <span style='font-size:30px'>About me:</span>
                    </div>
                     <div class="title fadeIn "style="text-align:left;">I am Jamal pursuing B.Tech CSE at Baddi University of Emerging Sciences & Technology,H.P. My journey into the world of artificial intelligence and machine learning began with a fascination for how these technologies can transform industries and improve lives.Beyond technical skills, I am committed to continuous learning and staying at the forefront of AI/ML advancements.In addition to my technical skills, I bring strong communication and problem-solving abilities to the table, allowing me to effectively collaborate with cross-functional teams and stakeholders. I am driven by a passion for innovation and a desire to make a meaningful impact through AI and machine learning. </div>
                     """,
          unsafe_allow_html=True)
        st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:30px;'>Projects:</span>
                </div>
                <div class="title fadeIn "style="text-align:left;"> I have implemented my knowledge and skills in some projects.</div>
               <div style='font-size:25px;'color:#333;'>➡️ Prediction model</div>
               <div style='font-size:18px;'color:#333;'>The main motive of this project is to predict the results of the olympic games. The developed model is trained on 80% data of the provided dataset tested on about 20% of the data.The project is build using the various python libraries (Numpy,Pandas,Matplotlib,Seaborn)and is based on linear regression machine learning algorithm. </div>
                """,
            unsafe_allow_html=True)
        st.write("""
                 <div class=
                "title"=style="text-align:left">
                <span style='font-size:30px;'>Qualifications</span>
                </div>
                """,
            unsafe_allow_html=True)
        qualifications = [
           {'name':'💠Bachelor\'s Degree in Computer Science: Baddi University Of Emerging Sciences And Technology', 'year': '2022-2026(pursuing)'},
          {'name': '💠Higher Secondary School: Kanti Secondary School ', 'year': '2022'},
          {'name':' 💠Secondary School:  Siddhartha  Pratibha English School','year':'2019'}
         ]
    
        for qual in qualifications:
             st.write(f"### {qual['name']}")
             st.write(f"- Year: {qual['year']}")
             #st.image('path_to_image.png', caption='Certificate or Achievement', use_column_width=True)
             st.write('')
             st.markdown('---') 
        st.subheader('Skills & Certifications:')
        st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:22px; font-weight:bold'>Skills</span><br>
                <span style='font-size:20px;'>Technical skills:</span><br>
                <span style='font-size:18px;'> -C programming language</span><br>
                <span style='font-size:18px;'> -C++ programming language</span><br>
                <span style='font-size:18px;'> -Python programming language</span><br>
                <span style='font-size:18px;'> -Pandas,Matplotlib,Numpy</span><br>
                <span style='font-size:18px;'> -MySQL</span><br>
                <span style='font-size:20px;'>Soft Skills:</span><br>
                <span style='font-size:18px;'> Problem-solving,Teamwork, Communication.</span><br>
                 <span style='font-size:22px; font-weight:bold'>Certifications</span><br>
                 <span class="animate__animated animate__fadeIn" style='font-size:20px;'>
                 - Prediction Project Using Python <br>
                - Machine Learning<br>
                - Basics of Python Data Wrangling<br>
                -Pandas<br>
                - Verizon - Cloud Platform Job Simulation<br>
                - Crash course on Python<br>
            </span>
                </div>
                """,
                 unsafe_allow_html=True) 
        font_awesome_css = """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        """

        # HTML and CSS for social media icons in the contact section
        contact_section = """
        <style>
        .contact-section {
     text-align: center;
     padding: 20px;
     margin-top: 40px;
     border-top: 2px solid #ccc;
        }
        .contact-section h2 {
      margin-bottom: 20px;
        }
        .contact-icons {
         display: flex;
         justify-content: center;
         gap: 30px;
         margin-top: 10px;
        }
        .contact-icons a {
          text-decoration: none;
         color: inherit;
            }
        .contact-icons i {
     font-size: 30px;
     color: #4c4c4c;
     transition: color 0.3s;
        }
        .contact-icons i:hover {
         color: #0077b5; /* Example hover color */
            }
        </style>
        <div class="contact-section">
         <h2>Contact Me</h2>
            <p>You can reach me through these social media platforms:</p>
        <div class="contact-icons">
        <a href="https://linkedin.com/in/jamal-ahmad-faruki-488b8b243" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/khanjamal59" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://facebook.com/khanzamal11?mibextid=ZbWKwL" target="_blank"><i class="fab fa-facebook"></i></a>
        <a href="mailto:00zamalahmed11@gmail.com" target="_blank"><i class="fas fa-envelope"></i></a>
         </div>
        </div>
        <div class="title" style="text-align:center;">
        &copy; 2024 Jamal Ahmad. All rights reserved.
     </div>
        """
        st.markdown(font_awesome_css + contact_section, unsafe_allow_html=True)       
        
    if page=="About":
        st.subheader("Welcome to About page")
        st.write(f"""
                    <div class=
                     "title"=style="text-align:left;color:#ffff00;"> <!-- Wite text color -->
                     <span style='font-size:30px'>About me</span>
                    </div>
                     <div class="title fadeIn "style="text-align:left;">I am Jamal pursuing B.Tech CSE at Baddi University of Emerging Sciences & Technology,H.P. My journey into the world of artificial intelligence and machine learning began with a fascination for how these technologies can transform industries and improve lives.Beyond technical skills, I am committed to continuous learning and staying at the forefront of AI/ML advancements.In addition to my technical skills, I bring strong communication and problem-solving abilities to the table, allowing me to effectively collaborate with cross-functional teams and stakeholders. I am driven by a passion for innovation and a desire to make a meaningful impact through AI and machine learning. </div>
                     """,
          unsafe_allow_html=True)
    if page=="Project":
        st.subheader("Welcome to Project page")
        st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:30px;'>Projects</span>
                </div>
                <div style='font-size:18px;'> I have implemented my knowledge and skills in some projects.</div>
                <div style='font-size:25px;'color:#333;'>➡️ Prediction model</div>
                <div style='font-size:18px;'color:#333;'>The main motive of this project is to predict the results of the olympic games. The developed model is trained on 80% data of the provided dataset tested on about 20% of the data.The project is build using the various python libraries (Numpy,Pandas,Matplotlib,Seaborn)and is based on linear regression machine learning algorithm. </div>
                """,
            unsafe_allow_html=True)
        st.markdown(
                    """
             <style>
             .custom-link {
            font-size: 18px;
            color: blue;
            text-decoration: none;
            }
           .custom-link:hover {
            text-decoration: underline;
            }
            </style>

            <div class="custom-div">
            <a href="https://github.com/khanjamal59/project-of-machine-learning" target="_blank" class="custom-link">
                click here to visit project
            </a>
            </div>
            """
           , unsafe_allow_html=True
                 )
    
        st.write(f"""
                    <div class=
                     "title"=style="text-align:left;color:#ffff00;"> <!-- Wite text color -->
                     <span style='font-size:23px'>➡️Interactive Visualization</span>
                    </div>
                    """,
                    unsafe_allow_html=True)
        st.write('Here is an example of an interactive 3D scatter plot:')
    
           # Generate random data for example
        np.random.seed(0)
        data = pd.DataFrame(
        np.random.randn(1000, 3),
        columns=['a', 'b', 'c']
         )
    
        scatterplot = pdk.Deck(
        map_style='',
        initial_view_state=pdk.ViewState(
            latitude=28.3974,
            longitude=84.1258,
            zoom=0,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=data,
                get_position=['a', 'b'],
                get_text='Place Name',
                get_color='c',
                get_radius=100,
                opacity=0.8,
                pickable=True,
            ),
        ],
        )
    
        st.pydeck_chart(scatterplot)
    if page=="Education":
         st.subheader('Welcome to Qualifications Page')
         st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:22px;'>Educational Details Visualization</span>
                </div>
                """,
                 unsafe_allow_html=True)   
         # Sample data (replace with your own dataset)
         data = {
                    'Institution name': ['Secondary School', 'Higher Secondary School', 'Bachelor\'s Degree'],
            'Years': [2019, 2022, 2026]
            }
         sns.set(style='whitegrid')  # Set the style of the plot
         plt.figure(figsize=(8, 6))  # Set the size of the plot

            # Create the point plot
         sns.pointplot(x='Years', y='Institution name', data=data, markers='^', color='blue')

          # Customize labels and title
         plt.xlabel('Year Of Graduation',fontsize=16,color='purple')
         st.pyplot(plt)
         st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:22px;'>Institution Details</span>
                </div>
                """,
                unsafe_allow_html=True)
    
         qualifications = [
           {'name': 'Bachelor\'s Degree in Computer Science: Baddi University Of Emerging Sciences And Technology', 'year': '2022-2026(pursuing)'},
          {'name': 'Higher Secondary School: Kanti Secondary School ', 'year': '2022'},
          {'name':' Secondary School:  Siddhartha  Pratibha English School','year':'2019'}
         ]
    
         for qual in qualifications:
             st.write(f"### {qual['name']}")
             st.write(f"- Year: {qual['year']}")
             #st.image('path_to_image.png', caption='Certificate or Achievement', use_column_width=True)
             st.write('')
             st.markdown('---') 
    if page=="Skills & Certifications":
        st.subheader('Welcome to Skills & Certifications Page')
        st.write(f"""
                <div class=
                "title"=style="text-align:left">
                <span style='font-size:22px; font-weight:bold'>Skills</span><br>
                <span style='font-size:20px;'>Technical skills:</span><br>
                <span style='font-size:18px;'> -C programming language</span><br>
                <span style='font-size:18px;'> -C++ programming language</span><br>
                <span style='font-size:18px;'> -Python programming language</span><br>
                <span style='font-size:18px;'> -Pandas,Matplotlib,Numpy</span><br>
                <span style='font-size:18px;'> -MySQL</span><br>
                <span style='font-size:20px;'>Soft Skills:</span><br>
                <span style='font-size:18px;'> Problem-solving,Teamwork, Communication.</span><br>
                 <span style='font-size:22px; font-weight:bold'>Certifications</span><br>
                 <span class="animate__animated animate__fadeIn" style='font-size:20px;'>
                 - Prediction Project Using Python <a href="https://www.linkedin.com/in/jamal-ahmad-faruki-488b8b243/overlay/1720114221059/single-media-viewer/?profileId=ACoAADyCSOgB3_YFJqjR26Fcyk4I8z8nMQxtbws" target="_blank">(View)</a><br>
                - Machine Learning <br>
                - Basics of Python Data Wrangling<br>
                -Pandas<br>
                - Crash Course on Python <a href="https://coursera.org/share/291f5e8614e02a46d169fb5fa17a6747" target="_blank">(View)</a><br>
                - Verizon - Cloud Platform Job Simulation<a href="https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Verizon%20Communications%20Inc./aNJGnRtgfiK5fQqcR_Verizon_HekLF2mXavEHtsCd7_1719409460141_completion_certificate.pdf" target="_blank">(View)</a><br>
                </span>
                </div>
                """,
                 unsafe_allow_html=True)            
        st.subheader('Skills & Certifications Visualization')

         # Data for skills
        skills_data = pd.DataFrame({
        'Skill': ['C', 'C++', 'Python', 'Pandas', 'Matplotlib', 'Numpy', 'MySQL'],
        'Proficiency': [5, 5, 5, 5, 5, 5, 5]  # Example proficiency levels (out of 10)
            })

        # Bar chart for skills
        st.header('Skills Proficiency')
        skills_chart = alt.Chart(skills_data).mark_bar().encode(
        x='Proficiency',
        y=alt.Y('Skill', sort='-x'),
        color='Skill',
        tooltip=['Skill', 'Proficiency']
        ).properties(
        width=600,
        height=300
        )
        st.altair_chart(skills_chart, use_container_width=True)

        # Data for certifications
        certifications_data = pd.DataFrame({
        'Certification': [
            'Prediction project Using  Python',
            'Machine learning',
            'Python data wrangling',
            'Pandas',
            'Verizon - Cloud Platform Job Simulation',
            'Crash Course on Python'
        ],
        'Completion Year': [2024, 2023, 2024,2024,2024,2023]
       })

       # Table for certifications
        st.header('Certifications')
        st.table(certifications_data)
    if page=="Contact": 
        font_awesome_css = """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        """

        # HTML and CSS for social media icons in the contact section
        contact_section = """
        <style>
        .contact-section {
     text-align: center;
     padding: 20px;
     margin-top: 40px;
     border-top: 2px solid #ccc;
        }
        .contact-section h2 {
      margin-bottom: 20px;
        }
        .contact-icons {
         display: flex;
         justify-content: center;
         gap: 30px;
         margin-top: 10px;
        }
        .contact-icons a {
          text-decoration: none;
         color: inherit;
            }
        .contact-icons i {
     font-size: 30px;
     color: #4c4c4c;
     transition: color 0.3s;
        }
        .contact-icons i:hover {
         color: #0077b5; /* Example hover color */
            }
        </style>
        <div class="contact-section">
         <h2>Contact Me</h2>
            <p>You can reach me through these social media platforms:</p>
        <div class="contact-icons">
        <a href="https://pinterest.com/jamalfaruki9816" target="_blank"><i class="fab fa-pinterest"></i></a>
        <a href="https://linkedin.com/in/jamal-ahmad-faruki-488b8b243" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/khanjamal59" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://facebook.com/khanzamal11?mibextid=ZbWKwL" target="_blank"><i class="fab fa-facebook"></i></a>
        <a href="https://instagram.com/khanzamal11?igsh=NDQ4dWk4emN1ajRz" target="_blank"><i class="fab fa-instagram"></i></a>
        <a href="mailto:00zamalahmed11@gmail.com" target="_blank"><i class="fas fa-envelope"></i></a>
        <a href="https://replit.com/@00zamalahmed11" target="_blank"><i class="fas fa-code"></i></a> 
         </div>
        </div>
        """

        st.markdown(font_awesome_css + contact_section, unsafe_allow_html=True)           
if __name__ == '__main__':
     web_portfolio() 
