import re
from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.user import User
from Flask_App.models.recipe import Recipe


@app.route('/add_new_recipe')
def add_new_recipe():
    return render_template('add_new_recipe.html')


@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    user_id = session['user_id']
    data = {
        "name": request.form['name'],
        "date": request.form['date'],
        "thirty": request.form['thirty'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "user_id": session['user_id']
    }

    Recipe.save(data)

    return redirect(f'/recipes/{user_id}')


@app.route('/show_recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    query = "SELECT * FROM recipes WHERE id = %(id)s;"
    data = {
        'id': recipe_id
    }
    results = Recipe.get_all(query, data)

    return render_template("view_recipe.html", recipe=results[0])


@app.route('/edit_page/<int:recipe_id>')
def edit_recipe(recipe_id):
    query = "SELECT * FROM recipes WHERE id = %(id)s;"
    data = {
        'id': recipe_id
    }
    results = Recipe.get_all(query, data)

    return render_template("edit_recipe.html", recipe=results[0])


@app.route('/update/<int:recipe_id>', methods=['POST'])
def update(recipe_id):
    query = "UPDATE recipes SET name=%(name)s, date=%(date)s, thirty= %{thirty}s, description=%(description)s, instructions=%(instructions)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        'id': recipe_id,
        "name": request.form['name'],
        "date": request.form['date'],
        "thirty": request.form['thirty'],
        "description": request.form['description'],
        "instructions": request.form['instructions']
    }
    Recipe.edit_recipe(query, data)
    return redirect(f"/show_recipe/{recipe_id}")
