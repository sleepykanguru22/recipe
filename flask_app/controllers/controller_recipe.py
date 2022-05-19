
from flask_app import app
from flask import render_template,redirect,session,request, flash
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User
# from flask_app.models import Recipe, User


@app.route('/recipe/new')
def recipe_new():
    context ={
        'user':User.get_one({'id':session['uuid']})
    }    
    return render_template('new_recipe.html', **context)

@app.route('/recipe/create', methods=['POST'])
def recipe_create():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/new')
    data = {
        **request.form,
        'user_id': session['uuid']
    }  
    Recipe.create(data) 
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