# Image Parsing with Flask & Python

A simple project demonstrating image upload, OCR, and web integration using Python and Flask. Users can upload an image through a web page, and the app extracts text from it using ```pytesseract```.

_____

# Key Learnings

Built a **Flask API** to handle image uploads and return JSON responses.

Used **Pillow** to process images and pytesseract for OCR.

Connected frontend (index.html) with Flask using JavaScript fetch().

Solved **CORS** issues to enable communication between frontend and backend.

Learned to debug browser and server errors, clean OCR output, and make text display neatly.
____
# How to Use

1. Run the Flask app:
```
python app.py
```
2. Open index.html in a browser.

3. Upload an image and view the extracted text.
____
Next Steps

* Improve UI with drag-and-drop.

* Add multi-line formatting or highlight detected text.

* Extend to object detection or table extraction.

* Deploy online for broader access.
