from googletrans import Translator
import cv2
import pytesseract
from flask import Flask, request, render_template
	

app = Flask(__name__)
#for windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@app.route('/', methods=['GET','POST'])
def home():
  if request.method == 'POST':
    image = request.files['picture']
    image.save("IMG.jpg")

    languaje = request.form['languaje']
    print(languaje)

    if languaje != "ninguno":

      text = main(lan=languaje)
    else:
      text = main()
    return render_template('result.html', text=text)

  
  return render_template('index.html')


def main(lan=None):
  config = ('-l eng --oem 1 --psm 3')
 
  im = cv2.imread("IMG.jpg", cv2.IMREAD_COLOR)
  text = pytesseract.image_to_string(im, config=config)
  
  if lan:
    text = translate(text, lan) 

  return text 

def translate(text, lenguaje):
  translator = Translator()
  result = translator.translate(text, dest=lenguaje)
  return result.text



if __name__ == '__main__':
  app.run(debug=True, port=5000)
  

  
  
 