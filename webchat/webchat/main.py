from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketIO = SocketIO(app, cors_allowed_origins="*")

@socketIO.on('message')
def handle_message(message):
    print("Recieved message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html") 

if __name__ == "__main__":
    socketIO.run(app,host="localhost")
       