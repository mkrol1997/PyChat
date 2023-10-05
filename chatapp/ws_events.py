from chatapp.websockets import socketio
from flask_socketio import emit


@socketio.on('connect')
def handle_handshake():
    print('Connected!')


@socketio.on('new_message')
def handle_new_message(message):
    emit('chat', {'message': message}, broadcast=True)

