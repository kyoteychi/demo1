from flask import Flask, render_template, request, redirect, flash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(256)  # Необходимо для работы flash()

root = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(root, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('upload.html')

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('upload.html')

        file_save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_save_path)
        flash('File successfully uploaded')
        return render_template('upload.html')

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)