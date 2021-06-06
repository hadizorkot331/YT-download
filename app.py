from flask import Flask, render_template, request
import pytube
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        home = os.path.expanduser("~")
        link = request.form.get("video-link")
        yt = pytube.YouTube(link)
        yt.streams.filter(progressive=True).first().download(os.path.join(home, "Downloads"))
        return render_template('index.html')