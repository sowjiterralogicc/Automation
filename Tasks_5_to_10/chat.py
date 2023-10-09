from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('message')    #It listens for events with the name 'message'.
def handle_message(data):
    message = data['message']
    username = data['username']
    print(f"Received message from {username}: {message}")
    socketio.emit('message', data, room=None, namespace='/')  #It then uses socketio.emit to emit
    # the same 'message' event back to all connected clients (room=None) in the root namespace ('/')
if __name__ == '__main__':
    socketio.run(app, debug=True)
