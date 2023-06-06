from flask import jsonify, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm,\
    PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm

@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return jsonify({"status": "success", "message": "Logged in"})
        return jsonify({"status": "failure", "message": "Invalid email or password."})
    return jsonify({"status": "failure", "message": "Invalid form data."})


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"status": "success", "message": "Logged out"})


@auth.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        return jsonify({"status": "success", "message": "A confirmation email has been sent to you by email."})
    return jsonify({"status": "failure", "message": "Invalid form data."})
