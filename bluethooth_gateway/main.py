from flask import Flask, request
import os
from threading import Thread

app = Flask(__name__)


def play_sound(command):
    print("play sound")
    if command == "no_face":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Loi\ khuon\ mat.mp3')
    elif command == "wrong_ticket":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Khong\ khop\ ve.mp3')
    elif command == "no_licence_plate":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Khong\ co\ bien\ so.mp3')


@app.route("/sound")
def hello():
    command = request.args.get('command')
    sound_thread = Thread(target=play_sound, args=(command, ))
    sound_thread.start()
    return "ok", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
