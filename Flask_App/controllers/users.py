import re
from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.user import User
from Flask_App.models.login import Login
from Flask_App.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if session.get('user_id') == True:
        user_id = session['user_id']
        return redirect(f'/recipes/{user_id}')
    elif session.get('user_name') == True:
        uQuery = 'SELECT * FROM users WHERE first_name = %(first_name)s;'
        uData = {'first_name': session['user_name']}
        user_in_db = User.get_all(uQuery, uData)
        user_id = user_in_db[0].id
        return redirect(f'/recipes/{user_id}')
    return render_template("index.html")


@app.route('/create/user', methods=['POST'])
def create_user():
    uData = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    pw1_hash = bcrypt.generate_password_hash(request.form['pass1'])
    pw2_hash = bcrypt.generate_password_hash(request.form['pass2'])

    pData = {
        'pass1': pw1_hash,
        'pass2': pw2_hash
    }

    if not User.registration_validation(request.form) or not Login.password_validation(request.form):
        return redirect('/')
    new_user = User.save(uData)
    session['user_name'] = request.form['fname']
    session['user_id'] = new_user
    pData['user_id'] = new_user
    Login.save(pData)

    return redirect(f'/recipes/{new_user}')


@app.route('/logout')
def loggedout():
    session.clear()
    return redirect("/")


@app.route('/login', methods=['POST'])
def login():

    uQuery = 'SELECT * FROM users WHERE email = %(email)s;'
    uData = {'email': request.form['email']}
    user_in_db = User.get_all(uQuery, uData)
    if user_in_db == False:
        flash("Invalid Email/Password")
        return redirect("/")
    user_id = user_in_db[0].id

    lQuery = "SELECT * FROM logins WHERE user_id = %(user_id)s;"
    lData = {'user_id': user_id}
    user_password = Login.get_all(lQuery, lData)

    if not user_in_db or not user_password:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_password[0].pass1, request.form['pass']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_name'] = user_in_db[0].first_name
    return redirect(f"/recipes/{user_in_db[0].id}")


@app.route('/recipes/<int:user_id>')
def get_recpies(user_id):
    if session.get('user_id') == False or session.get('user_name') == False:
        return redirect('/')

    lQuery = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
    lData = {'user_id': user_id}
    user_recipes = Recipe.get_all(lQuery, lData)

    return render_template('welcome.html', recipes=user_recipes)

# @app.route('/users')
# def user():
#     query = "SELECT * FROM users;"
#     users = User.get_all(query)
#     return render_template("results.html", all_users=users)

# @app.route('/edit_page/<int:user_id>')
# def edit_page(user_id):
#     query = "SELECT * FROM users WHERE id = %(id)s;"
#     data = {
#         'id': user_id
#     }
#     user = User.get_all(query, data)
#     print(user)
#     return render_template("edit_page.html", user=user[0])


# @app.route('/update/<int:user_id>', methods=['POST'])
# def update(user_id):
#     query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
#     data = {
#         'id': user_id,
#         "fname": request.form['fname'],
#         "lname": request.form['lname'],
#         "email": request.form['email']
#     }
#     user = User.edit_user(query, data)
#     print(user)
#     return redirect(f"/show/{user_id}")


# @app.route('/delete/<int:user_id>')
# def remove_user(user_id):
#     query = "DELETE FROM users WHERE id = %(id)s;"
#     data = {
#         'id': user_id,
#     }
#     User.remove_user(query, data)
#     return redirect('/users')
