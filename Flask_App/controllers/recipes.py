from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.user import User


@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/create/user', methods=['POST'])
# def create_user():
#     data = {
#         "fname": request.form['fname'],
#         "lname": request.form['lname'],
#         "email": request.form['email'],
#     }
#     new_user = User.save(data)
#     return redirect(f'/show/{new_user}')


# @app.route('/users')
# def user():
#     query = "SELECT * FROM users;"
#     users = User.get_all(query)
#     return render_template("results.html", all_users=users)


# @app.route('/show/<int:user_id>')
# def detail_page(user_id):
#     query = "SELECT * FROM users WHERE users.id = %(id)s;"
#     data = {
#         'id': user_id
#     }

#     results = User.get_all(query, data)

#     return render_template("details_page.html", user=results[0])


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
