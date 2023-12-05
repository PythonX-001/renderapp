
#*TODO: add login form / save the chat /  user interface data coockies


from flask import Flask, render_template, request

import sys
from flask import jsonify
#*import my own libs; ai/image
from brain import who_created_me , generate_image



import os






app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Fibonacci")
def febo():
    return render_template("febo.html")

@app.route("/Elliot")
def febo():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(who_created_me(userText))

@app.route("/getimg")
def get_imgGen_response():
    userText = request.args.get('msg')
    image_urls = jsonify(generate_image(userText))
 
    return image_urls




if __name__ == "__main__":
    app.run()





