import google.generativeai as genai
import cv2
import os
from PIL import Image
import numpy as np

def text_extracter_image(image_path):
    # Lets load and process the image
    file_bytes=np.asarray(bytearray(image_path.read()),dtype=np.uint8)
    image=cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # To convert bgr to rgb
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # to convert bgr to grey
    _,image_bw=cv2.threshold(image_grey,150,255,cv2.THRESH_BINARY) # To convert grey to black and white


    final_image =Image.fromarray(image_bw)

    key=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=key)
    model=genai.GenerativeModel('gemini-2.5-flash-lite')

    prompt='''You act as an OCR application on the given image and extract the text from it.
    Give only the text as output, do not give any explanation or description.'''


    response=model.generate_content([prompt,final_image])
    return response.text
