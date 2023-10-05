from flask import Blueprint, render_template, request


main = Blueprint('auth', __name__)


@main.route('/')
def login():
    return render_template('login.html')


@main.route('/chat')
def chat():
    username = request.args.get('username')
    return render_template('chat.html', username=username)
