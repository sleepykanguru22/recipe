import re
from flask_app import app
from flask import render_template,redirect,session,request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/new')
def user_new():
    return render_template('new_user.html')

@app.route('/user/create', methods=['POST'])
def user_create():
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