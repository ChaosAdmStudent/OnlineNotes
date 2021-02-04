from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note 
from . import db 
import json 


# This file will be a blueprint of our app
# Means it has roots/urls inside here 

views = Blueprint('views',__name__) 

@views.route('/', methods=['GET','POST'])  # This is a decorator for a function called home, i.e, we want to add functionality defined inside the Blueprint 'route' decorator to our home() function. The home page is routed to when website is reached "/"" 
@login_required 
def home(): 

    if request.method == 'POST': 
        data = request.form.get('note') 
        new_note = Note(data=data, user_id = current_user.id) 
        db.session.add(new_note) 
        db.session.commit()  
        flash('Note saved!', 'message')

    return render_template("home.html") 

@views.route('/delete-note', methods=['POST'])
def delete_note(): 
    note = json.loads(request.data) 
    noteId = note['noteId'] 
    note = Note.query.get(noteId) 
    
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note) 
            db.session.commit()  
            flash('Successfully deleted message','message') 
    
    return jsonify({})



