from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    most_common_word = ""
    word_counts = {}
    file_uploaded = False

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file:
                text = file.read().decode('utf-8').lower()
                words = text.split()
                word_counts = Counter(words)
                most_common_word = word_counts.most_common(1)[0][0]
                file_uploaded = True

    return render_template('index.html', most_common_word=most_common_word,
                           word_counts=word_counts, file_uploaded=file_uploaded)

if __name__ == '__main__':
    app.run(debug=True)