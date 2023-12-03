from flask import Flask, render_template, request
import requests
from flask import jsonify

#*import my own libs; ai/image

from ImgGen import generate_image

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

    # Download and save images



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    image_urls = jsonify(generate_image(userText))
 
    return image_urls




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


