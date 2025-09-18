import streamlit as st
import google.generativeai as genai
import os
from pdfextracter import text_extractor_pdf
from docxextracter import text_extracter_docx
from imageextracter import text_extracter_image

# Configure the model

key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model=genai.GenerativeModel('gemini-2.5-flash-lite')

#Upload the file in sidebar

st.sidebar.title(':orange[UPLOAD YOUR MoM NOTES HERE]')
st.sidebar.subheader('Only upload IMAGES, PDFs and DOCX files')
user_file=st.sidebar.file_uploader('Upload Your File',type=['pdf','docx','png','jpg','jpeg'])
if user_file:
  if user_file.type=='application/pdf':
    user_text=text_extractor_pdf(user_file)
  elif user_file.type=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    user_text=text_extracter_docx(user_file)
  elif user_file.type in ['image/png','image/jpg','image/jpeg']:
    user_text=text_extracter_image(user_file)
  else: 
    st.sidebar.error('Please Upload pdf , docx or image file')


# Main page 

st.title(':blue[MINUTES OF MEETING :] :grey[AI assisted MoM generator in a standardized form from meeting motes.]')

tips='''Tips to use this app
* Upload your meeting in sidebar(image,pdf,docx)
* click on generate MOM and get the standardized MOM's'''
st.write(tips)

if st.button('Generate MoM'):
  if user_text is None:
    st.error('Text is not generated')
  else:
    with st.spinner('Processing your data.....'):
      prompt=f'''You are an AI assistant that creates professional Minutes of Meeting (MoM) from any document (PDF, DOCX, or image). 

      Instructions:
      1. Read the content of the uploaded document carefully.
      2. Extract the following details wherever available:
          - Meeting Date & Time
          - Venue / Platform
          - Attendees
          - Agenda Items
          - Discussion Points
          - Decisions Made
          - Action Items (include person responsible and deadline if mentioned)
      3. Organize the extracted information into a clean, structured MoM format.
      4. Present the output as a readable, concise text suitable for official sharing.
      5. If any information is missing, leave it blank or note as "Not mentioned."

      Example format:
      
      Title: Title of the meeting as the heading 
      Date:  
      Time:  
      Venue/Platform:  
      Attendees:  

      Agenda:  
       - Item 1  
       - Item 2  

      Discussion Points:  
       - Point 1  
       - Point 2  

      Decisions Made:  
       - Decision 1  
       - Decision 2  

      Action Items:  
       - Task 1 → Responsible: Person A → Deadline: DD-MM-YYYY  
       - Task 2 → Responsible: Person B → Deadline: DD-MM-YYYY  

      Generate the MoM based on the content provided.

      use bulletin points and highlights or bolds important keypoints so that everything is clean and nothing important is missed 
      user uploaded document is {user_text}

      generate the output in a format that it can be copied and pasted in a word document.

      user uploaded document is {user_text}
      '''

      response=model.generate_content(prompt)
      st.markdown(response.text)

    
      st.download_button(
      label="Download Report as PDF",
      data=response.text,
      file_name="Structural_Defect_Report.docx",
      mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
      )