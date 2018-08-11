from . import auth
from .model import Account
from flask import redirect, url_for, render_template, flash, request
from flask_login import logout_user, login_user
from app.forms import LoginForm, RegisterForm


@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Account.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)

            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('admin.home')

            return redirect(next)

        flash('E-mail ou senha estão incorretos. Por favor verifique!')

    return render_template('auth/login.jinja2', form=form)


@auth.route('/request/register')
def request_register():
    form = RegisterForm()
    return render_template('auth/request_register.jinja2', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Snif... Thanks for use the ocomunitario. Comeback always...')
    return redirect(url_for('auth.login'))
