from pathlib import Path
import streamlit as st
from PIL import Image

current=Path(__file__).parent if"__file__" in locals() else Path.cwd()
css=current/"styles"/"style.css"
pdf=current/"images"/"sample.pdf"
profile=current/"images"/"profile.png"

PAGE_TITLE="Digital CV |Roger Collins"
PAGE_ICON=":wave:"
name="Roger Collins"
description="Contract software developer ,Senior Data Analyst supported by decision making"
email="karthisdn2005@gmail.com"
socialmedia={
    "LinkedIn":"www.linkedin.com/in/karthikeyan-r-cs-student-b6193a305",
    "Youtube":"www.youtube.com",
    "GitHub":"https://github.com"
}
Projects={
    "🏆 Personal Portfolio Website":"www.google.com",
    "🏆 Library Management System":"www.google.com",
    "🏆 Weather Forecasting System":"www.google.com",
    "🏆 Online Chat Application":"www.google.com"
}
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
#include css and pdf file
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(pdf,"rb") as pdf_file:         #rb is read binary
    pdfbyte=pdf_file.read()
image=Image.open(profile)

#hero section
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(image,width=230)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(label="🧾 Download Resume",
                       data=pdfbyte,
                       file_name=pdf.name)
    st.write("📩",email)
    #links
    st.write("#")
    cols=st.columns(len(socialmedia))
    for index,(platform,link) in enumerate(socialmedia.items()):
        cols[index].write(f"[{platform}]({link})")

    #experience and qualifications
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
        """
- 7years of experience in software developement
- Skilled in python,java,javascript etc
- Good communication skills
- Excelent team player and displaying strong sense
""")
    
st.write("#")
st.subheader("Hard skills")
st.write(
        """
- 💻 Programming: Python (Streamlit ,Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗂️ Databases: Postgres, MongoDB, MysQL
""")
#work history
st.write("#")
st.subheader("Work History")
st.write("---")
st.write("**Digital Marketing Manager**")
st.write("June 2015 - Present")
st.write("Responsibilities:")
st.write(""" 
- Managed complex domestic and international travel for executives.
- Decreased expense management costs by 35%.
- Hired, trained, and guided a team of assistants.
""")

st.write("#")
st.write("**Software Developer**")
st.write("June 2010 - 2011")
st.write("Responsibilities:")
st.write(""" 
- Managed complex domestic and international travel for executives.
- Decreased expense management costs by 35%.
- Hired, trained, and guided a team of assistants.
""")

st.write("#")
st.write("**WebApp developer**")
st.write("June 2011 - 2014")
st.write("Responsibilities:")
st.write(""" 
- Managed complex domestic and international travel for executives.
- Decreased expense management costs by 35%.
- Hired, trained, and guided a team of assistants.
""")
st.write("---")
st.write("#")
st.subheader("Projects and accomplishments")
st.write("#")
for project,link in Projects.items():
    st.write(f"[{project}]({link})")
    