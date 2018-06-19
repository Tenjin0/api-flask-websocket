from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_folder="static/dist")
socketio = SocketIO(app)

from routes import index
import websockets

if __name__ == "__main__":
    app.run(debug=True)

