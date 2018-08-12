from . import auth
from .model import Account
from flask import redirect, url_for, render_template, flash, request
from flask_login import logout_user, login_user
from app.forms import LoginForm, RegisterForm
from app import db


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

            flash('Login efetuado com sucesso!')

            return redirect(next)

        flash('E-mail ou senha estão incorretos. Por favor verifique!')
        return redirect(url_for('.login')), 500

    return render_template('auth/login.jinja2', form=form)


@auth.route('/request/register', methods=['GET', 'POST'])
def request_register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = Account.query.filter_by(email=form.email.data)

        if user:
            flash('Usuário já existe!')

        user = Account(
            form.first_name.data,
            form.last_name.data,
            form.email.data,
            form.password.data)

        db.session.add(user)
        db.session.commit()

        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('.login')
            
        flash('Usuário registrado com sucesso!')
        return redirect(next)

    return render_template('auth/request_register.jinja2', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Snif... Thanks for use the ocomunitario. Comeback always...')
    return redirect(url_for('auth.login'))
