from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.recipe import Recipe

# ROUTE TO ADD NEW RECIPES PAGE


@app.route('/add_new_recipe')
def add_new_recipe():
    return render_template('add_new_recipe.html')

# ROUTE TO CREATE THE NEW RECIPE


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

# ROUTE TO EDIT RECIPE PAGE


@app.route('/edit_page/<int:recipe_id>')
def edit_recipe(recipe_id):

    query = "SELECT * FROM recipes WHERE id = %(id)s;"
    data = {'id': recipe_id}
    results = Recipe.get_all(query, data)

    return render_template("edit_recipe.html", recipe=results[0])

# ROUTE TO UPDATE A RECIPE


@app.route('/edit_recipe/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):

    data = {
        'id': recipe_id,
        "name": request.form['name'],
        "date": request.form['date'],
        "thirty": request.form['thirty'],
        "description": request.form['description'],
        "instructions": request.form['instructions']
    }
    Recipe.edit_recipe(data)

    return redirect(f"/show_recipe/{recipe_id}")

# ROUTE TO VIEW SINGLE RECIPE


@app.route('/show_recipe/<int:recipe_id>')
def view_recipe(recipe_id):

    query = "SELECT * FROM recipes WHERE id = %(id)s;"
    data = {'id': recipe_id}
    results = Recipe.get_all(query, data)

    return render_template("view_recipe.html", recipe=results[0])

# ROUTE TO GET ALL RECIPES WITH SPECIFIC USER DEFINED DATE


@app.route('/show_this_date/<recipe_date>')
def recipes_on_this_date(recipe_date):

    query = "SELECT * FROM recipes WHERE date = %(date)s;"
    data = {'date': recipe_date}
    results = Recipe.get_all(query, data)

    return render_template("welcome.html", recipes=results)

# ROUTE TO DELETE A RECIPE


@app.route('/delete/<int:recipe_id>')
def remove_recipe(recipe_id):

    query = "DELETE FROM recipes WHERE id = %(id)s;"
    data = {'id': recipe_id}

    Recipe.remove_recipe(query, data)
    return redirect('/')
