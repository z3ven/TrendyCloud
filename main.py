import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/files'

trendy_cloud = Flask(__name__)
trendy_cloud.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@trendy_cloud.route('/')
def index():
    return render_template('index.html')


@trendy_cloud.route('/upload-file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(trendy_cloud.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))
        return render_template('suc-upload.html')
    return 0


@trendy_cloud.route('/upload/', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')


@trendy_cloud.route('/download-file/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename)

trendy_cloud.run()
