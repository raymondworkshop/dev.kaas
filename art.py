import os
import uuid

from flask import Blueprint, render_template, request, redirect, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

basedir = os.path.abspath(os.path.dirname(__file__))

#bp = Blueprint('art', __name__)

from app import app
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'img')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Only Image ...'), FileRequired('Choose a file!')])
    submit = SubmitField('Upload')

def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        for f in request.files.getlist('photo'):
            filename = uuid.uuid4().hex
            photos.save(f, name=filename + '.')
        success = True
    else:
        success = False
    #return render_template('art/index.html', form=form, success=success)
    return redirect(url_for('manage_file'))

def art():
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('art/index.html', images=files_list)

def manage_file():
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('art/index.html', images=files_list)

def open_file(filename):
    file_url = photos.url(filename)
    return render_template('browser.html', file_url=file_url)

def delete_file(filename):
    file_path=photos.path(filename)
    os.remove(file_path)
    return redirect(url_for('manage_file'))
