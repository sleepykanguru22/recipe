
from flask_app import app
from flask import render_template,redirect,session,request, flash
from flask_app.models.recipe import Recipe


@app.route('/recipe/new')
def recipe_new():
    return render_template('new_recipe.html')

@app.route('/recipe/create', methods=['POST'])
def recipe_create():
    return redirect('/')

@app.route('/recipe/<int:id>')
def recipe_show(id):
    return render_template('recipe_show.html')

@app.route('/recipe/<int:id>/edit')
def recipe_edit(id):
    return render_template('recipe_edit.html')

@app.route('/recipe/<int:id>/update',methods=['POST'])
def recipe_update(id):
    return redirect('/')

@app.route('/recipe/<int:id>/delete')
def recipe_delete(id):
    return redirect('/')