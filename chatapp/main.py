from flask import Blueprint, render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/find-friend')
@login_required
def find_room():
    room = request.args.get('fiend_name', False)
    if not room:
        return render_template('find_room.html')
    return render_template('find_room.html')


@main.route('/chat')
@login_required
def chat():
    username = request.args.get('username')
    return render_template('chat.html', username=username)

