from flask import Flask
import os
from threading import Thread

app = Flask(__name__)


def play_sound():
    os.system('mpg321 /home/pi/PiCrown4.0/sound.mp3')


@app.route("/sound")
def hello():
    sound_thread = Thread(target=play_sound)
    sound_thread.start()
    return "ok", 200


if __name__ == "__main__":
    app.run()
