
from flask import Flask, render_template, request
from brain import who_created_me
import sys



import os






app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(who_created_me(userText))


if __name__ == "__main__":
    app.run()





