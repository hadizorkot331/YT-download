from flask import Flask, render_template, request, send_file
import pytube
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        link = request.form.get("video-link")
        yt = pytube.YouTube(link)
        home = os.path.expanduser("~")
        yt.streams.filter(progressive=True).first().download(output_path=os.path.join(home, "Downloads"))
        return render_template('index.html')