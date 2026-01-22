SmartDoc OCR

SmartDoc OCR is a full-stack web application that extracts text from images and PDFs using OCR, optionally summarizes the extracted content using AI, and allows users to export results in multiple formats.
The project is designed with modular architecture, offline-first OCR, and user-controlled AI usage, making it transparent and privacy-aware.

🚀 Features

✅ Image OCR (JPG, PNG)

✅ PDF OCR with smart detection

Text-based PDFs (no OCR needed)

Scanned PDFs (OCR applied automatically)

✅ Advanced image preprocessing for better accuracy

✅ Optional AI-based text summarization

✅ Export extracted text as:

TXT

JSON

PDF

✅ Clean & responsive UI using Bootstrap

✅ Works even without AI (offline OCR)

🧠 Why SmartDoc OCR?

Most AI tools provide black-box OCR, where users have no control over how data is processed.

SmartDoc OCR is different because:

OCR works independently of AI

AI summarization is optional

Data stays on your system (privacy-friendly)

Structured export formats supported

Modular & explainable architecture

This makes the project suitable for education, internal tools, and privacy-sensitive use cases.

🛠️ Tech Stack
Layer	Technology
Backend	Django (Python)
OCR Engine	Tesseract OCR
Image Processing	OpenCV, Pillow
PDF Handling	PyMuPDF, pdf2image
AI Summarization	OpenAI API (optional)
Frontend	HTML, Bootstrap 5
Version Control	Git
IDE	VS Code

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd smartdoc-ocr

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install System Dependencies (macOS)
brew install tesseract poppler

🔑 Optional: Enable AI Summarization

Create a .env file in project root:

OPENAI_API_KEY=your_api_key_here


AI summarization is optional.
The project works fully without it.

▶️ Run the Project
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

📤 How It Works

User uploads an image or PDF

System detects file type

OCR extracts text

Text is cleaned and structured

User may optionally request AI summary

User can export results in desired format

🧪 Supported File Types

.jpg

.png

.pdf

🧯 Error Handling

AI quota limits handled gracefully

OCR failures do not crash the app

Safe fallback when AI is unavailable

📌 Use Cases

Digitizing scanned documents

Academic notes extraction

Resume & form processing

Document archiving

OCR learning & experimentation

🔮 Future Enhancements

Multi-language OCR selection from UI

User authentication & history

Table extraction from PDFs

Cloud storage integration

OCR confidence scoring

👨‍💻 Developer Notes

Designed with separation of concerns

OCR, AI, and Export layers are independent

Easy to extend or replace components

Interview-ready architecture

🏁 Conclusion

SmartDoc OCR is a practical, transparent, and modular OCR system that balances automation, control, and privacy.
It demonstrates real-world backend engineering concepts beyond simple API usage.

📜 License

This project is for educational and demonstration purposes.
