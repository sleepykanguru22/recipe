import re
from flask_app import app, bcrypt
from flask import render_template,redirect,session,request, flash
from flask_app.models.model_user import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/user/login', methods=['POST'])
def user_new():
    if not User.validate_login(request.form):
        return redirect('/')
    return render_template('new_user.html')
    # redirect to dashboard

@app.route('/user/create', methods=['POST'])
def user_create():
    if not User.validate(request.form):
       return redirect('/')  
    # need to change model user file name keep getting error of undefined
    # since the file is imported do I need to put the file name in this fucntion?
    
    hash_password=bcrypt.generate_password_hash(request.form['password'])
    #hash password
    data ={
        **request.form,
        'password':hash_password
    }
    # extracts everything from request.form can be used when data:dict is using same fields & few modifications
    user_id=User.create(data)
    session['uuid'] = user_id
    return redirect('/')

@app.route('/user/<int:id>')
def user_show(id):
    return render_template('user_show.html')

@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template('user_edit.html')

@app.route('/user/<int:id>/update',methods=['POST'])
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')