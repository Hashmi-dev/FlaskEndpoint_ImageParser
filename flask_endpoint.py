from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




@app.route('/parse-image', methods=['POST'])
def parse_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))


    text = pytesseract.image_to_string(img).strip()
    return jsonify({"text": text if text else "(No text detected)"})

if __name__ == '__main__':
    app.run(debug=True)

