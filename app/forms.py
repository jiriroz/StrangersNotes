from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    noteField = TextAreaField("Your Note", validators=[DataRequired()])
    submit = SubmitField("Save")
