from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.user import User
from Flask_App.models.login import Login
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# ROUTE TO LOGIN W/ VALIDATION, SETS SESSION DATA


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

    if not bcrypt.check_password_hash(user_password[0].pass1, request.form['pass']):
        flash("Invalid Email/Password")
        return redirect('/')
    # session.clear()
    session['user_name'] = user_in_db[0].first_name
    session['user_id'] = user_in_db[0].id
    return redirect(f"/recipes/{user_id}")

# ROUTE TO LOGOUT & CLEAR SESSION DATA


@app.route('/logout')
def loggedout():
    session.clear()
    return redirect("/")
