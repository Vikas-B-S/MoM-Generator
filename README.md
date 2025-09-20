# AI-Powered Minutes of Meeting (MoM) Generator

## 📌 Project Overview
This project is a **Streamlit-based AI application** that generates professional and structured **Minutes of Meeting (MoM)** from uploaded notes in **PDF, DOCX, or image** formats.  
It leverages **Google Generative AI (Gemini)** to process raw meeting notes and transform them into a clean, standardized MoM format ready for official use.

## 🚀 Features
- Upload meeting notes (PDF, DOCX, PNG, JPG, JPEG).  
- AI-powered text extraction from documents and images.  
- Automatic generation of structured MoMs with sections like:
  - Meeting Title  
  - Date & Time  
  - Venue / Platform  
  - Attendees  
  - Agenda Items  
  - Discussion Points  
  - Decisions Made  
  - Action Items (with responsible person & deadlines)  
- Download generated MoMs directly as a **Word document**.  
- Handles errors gracefully (missing or unclear data marked as *Not Mentioned*).  

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** – for UI & app deployment  
- **PyPDF** – for PDF text extraction  
- **python-docx** – for Word file generation  
- **Google Generative AI (Gemini 2.5 Flash Lite)** – for MoM generation  
- **OpenCV / OCR** (optional) – for image-to-text extraction  

## 📖 How to Use
1. Clone this repository:  
   ```bash
   git clone https://github.com/Vikas-B-S/MoM-Generator.git
   cd  MoM-Generator
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set your **Google API Key**:  
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

4. Run the app:  
   ```bash
   streamlit run MoM_generator.py
   ```

5. Upload your meeting notes and generate MoMs instantly!

## 📂 Project Structure
```
.
├── MoM_generator.py                 # Main Streamlit app
├── pdfextracter.py        # PDF text extraction logic
├── docxextracter.py       # DOCX text extraction logic
├── imageextracter.py      # Image text extraction logic (OCR)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## 🎯 Skills Demonstrated
- Text Extraction (PDF, DOCX, Image)  
- Natural Language Processing (NLP)  
- Generative AI Prompt Engineering  
- Streamlit App Development  
- Document Automation  

---

💡 *This project demonstrates how AI can assist in creating standardized documentation, saving time and improving productivity in corporate environments.*

