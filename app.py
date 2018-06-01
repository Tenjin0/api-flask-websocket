from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder="static/dist")
socketio = SocketIO(app)

from routes import index

@socketio.on('connect')
def connect_handler():
    print('connected')
    emit('response', {'meta': 'WS connected'})

@socketio.on('myevent')
def my_event(msg):
    print('my event', msg)
    emit('response', {'meta': 'WS connected'})

if __name__ == "__main__":
    app.run(debug=True)

