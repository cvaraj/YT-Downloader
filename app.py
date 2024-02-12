from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    return 'Download completed successfully!'

@app.route('/progress')
def progress():
    # Implement logic to get the progress of the download (e.g., check file size or percentage completion)
    # Return the progress as a response
    # For demonstration purposes, I'm returning a hardcoded value
    return 'progress:' + str(50)  # For example, return 50% progress

if __name__ == '__main__':
    app.run(debug=True)