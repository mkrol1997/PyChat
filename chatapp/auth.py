from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from chatapp import db
from chatapp.forms import LoginForm, RegisterForm
from chatapp.models import User


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if request.form.get('password') == request.form.get('password2'):
            new_user = User(
                email=request.form["email"],
                password=generate_password_hash(password=request.form["password"], salt_length=8),
                first_name=request.form["first_name"],
                last_name=request.form.get('last_name'))
            try:
                db.session.add(new_user)
                db.session.commit()
            except exc.IntegrityError:
                flash("User already exist. Please log in.", "info")
                return redirect(url_for("auth.login"))
            else:
                flash('Account created', 'success')
                return redirect(url_for("auth.login"))
        else:
            flash("Both passwords must be the same. Please try again.", "error")
            return redirect(url_for("auth.register"))
    else:
        return render_template("register.html", form=form)


@auth.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = User.query.filter_by(email=request.form["email"]).first()
        if user:
            if check_password_hash(user.password, request.form["password"]):
                login_user(user)
                return redirect(url_for("main.find_room"))
            else:
                flash(message="Wrong password", category="error")
                return redirect(url_for("auth.login"))
        else:
            flash(message="This email is not registered", category="info")
            return redirect(url_for("auth.login"))
    else:
        return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(message='Successfully logged out', category='success')
    return redirect(url_for('auth.login'))
