# Imports
from flask import Flask, make_response
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num_page>')
def index(num_page=0):
    return "Hello!!!"+str(num_page)

@app.route('/picture')
def picture():
    my_picture=BytesIO()
    Image.new("RGB", (400,300), "#13f").save(my_picture, "BMP")
    response=make_response(my_picture.getvalue())
    response.mimetype="image/bmp"
    return response

if __name__=='__main__':
    app.run(debug=True)
