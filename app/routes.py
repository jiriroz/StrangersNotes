from flask import request, render_template, flash, redirect, url_for

from app import app
from app.forms import NoteForm
from app import db
from app.models import Note


@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.args.get("name", "stranger")
    note = request.args.get("note")
    
    noteBody = ""
    if note is not None and note.isdigit():
        dispNote = Note.query.get(int(note))
        if dispNote is not None:
            noteBody = dispNote.body

    nameDisp = name[0].upper() + name[1:]
    user = {"username": nameDisp}
    form = NoteForm()
    if form.validate_on_submit():
        app.logger.info("Note submitted: {}".format(form.noteField.data))
    notes = Note.query.filter_by(username=name.lower())
    return render_template("index.html", user=user, form=form, notes=notes, noteBody=noteBody)
