from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request


@app.get("/")
@app.get("/users")
def all_users():
    users = User.find_all()
    return render_template("read_all.html", users=users)


@app.get("/users/new")
def create_user():

    return render_template("create_user.html")


@app.post("/users/new")
def create_new_user():
    print(request.form)
    user_id = User.create(request.form)
    print("THIS IS THE NEW USERS ID: " + str(user_id))

    return redirect("/users")


@app.get("/users/<int:user_id>")
def user_details(user_id):
    """This route displays one users' details"""

    user = User.find_by_id(user_id)
    if user == None:
        return "Cannont find user."

    return render_template("user_details.html", user=user)


@app.get("/users/<int:user_id>/edit")
def user_edit(user_id):
    """This route displays the edit form"""

    user = User.find_by_id(user_id)
    if user == None:
        return "Cannont find user."
    return render_template("edit_user.html", user=user)


@app.post("/users/edit")
def update_user():
    """This route processes the Edit form"""

    user_id = request.form["user_id"]
    User.update(request.form)

    return redirect(f"/users/{user_id}")


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """This route deletes a user"""
    User.delete_by_id(user_id)
    return redirect("/users")
