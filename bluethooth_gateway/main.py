from flask import Flask, request
import os
from threading import Thread

app = Flask(__name__)


def play_sound(message):
    print("play sound")
    if message == "Lỗi khuôn mặt":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Loi\ khuon\ mat.mp3')
    elif message == "Không khớp vé":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Khong\ khop\ ve.mp3')
    elif message == "Không có biển số":
        os.system('mpg321 /home/pi/PiCrown4.0/bluethooth_gateway/Khong\ co\ bien\ so.mp3')


@app.route("/sound")
def hello():
    message = request.args.get('message')
    sound_thread = Thread(target=play_sound, args=(message, ))
    sound_thread.start()
    return "ok", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
