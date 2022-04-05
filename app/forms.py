# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField  
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])