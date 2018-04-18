from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app)