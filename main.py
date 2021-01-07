#!/usr/bin python
import os
from flask import *
from threading import Thread
import requests

from piutils.draw import *
from piutils import utils as ut
import logging

import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

logger = ut.get_logger("pi_render_service")
app = Flask(__name__)
hnd = DisplayRequestHandle()
logo = cv2.imread("logo.png", cv2.IMREAD_COLOR)


@app.route('/display', methods=['POST', 'GET'])
def display():
    global hnd
    try:
        message=request.values['message']
        lane_id=request.values['lane_id']
        is_landscape=request.values.get('is_landscape', None)
        status=request.values.get('status', None)
        if status == "STOP":
            requests.get(bluethooth_url, params={"message": message})

        try:
            is_landscape = int(is_landscape)
        except:
            is_landscape = 1

        logging.info('request={}, laneid={}, is_landscape={}'.format(request, lane_id, is_landscape))
        if (message != 'Unknown'):
            license_plate_text=request.values.get('license_plate_text', '')
            encoded_profile_image=request.values['profile_image']
            encoded_license_plate_image=request.values['license_plate_image']

            hnd.add(Profile(encoded_profile_image, encoded_license_plate_image, status, lane_id, message, license_plate_text, is_landscape))
    except Exception as ex:
        ut.handle_exception(ex)

    return jsonify(success = True)


def make_screen_img(left_img, right_img):
    rgba = np.zeros((SCREEN_H, SCREEN_W, 4), np.uint8)
    tl, br = ut.get_default_roi('R', rgba.shape[1], rgba.shape[0], roi_translation, roi_l_w_ratio)
    if ut.not_null_roi(tl, br):
        cv2.rectangle(rgba, tl, br, (100, 200, 0, OPACITY), 3)
    tl, br = ut.get_default_roi('L', rgba.shape[1], rgba.shape[0], roi_translation, roi_l_w_ratio)
    if ut.not_null_roi(tl, br):
        cv2.rectangle(rgba, tl, br, (100, 200, 0, OPACITY), 3)

    if left_img is not None:
        rgba[:, 0:int(SCREEN_W / 2), 0:3] = left_img
        rgba[:, 0:int(SCREEN_W / 2), 3] = OPACITY

    if right_img is not None:
        rgba[:, int(SCREEN_W / 2):SCREEN_W, 0:3] = right_img
        rgba[:, int(SCREEN_W / 2):SCREEN_W, 3] = OPACITY

    return rgba


def runImageRendererThread():
    first_run = True
    write_error = False
    cnt = 0
    while True:
        t0 = time.time()
        try:
            if hnd.check_update() or first_run or write_error:
                first_run = False
                img = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)
                l, r = hnd.render_left_right(img)

                if l is not None:
                    height, width, channels = l.shape
                    resized_logo_image = cv2.resize(logo, (int(width / 5), int(height / 10)), interpolation=cv2.INTER_AREA)
                    l[0:int(height / 10), int(width - width / 5): width] = resized_logo_image

                if r is not None:
                    height, width, channels = r.shape
                    resized_logo_image = cv2.resize(logo, (int(width / 5), int(height / 10)), interpolation=cv2.INTER_AREA)
                    r[0:int(height / 10), int(width - width / 5): width] = resized_logo_image

                logger.info('time: {}: update screen image'.format(t0))

                try:
                    bgra = make_screen_img(l, r)
                    if bgra is not None:
                        cv2.imwrite(screen_file, bgra)
                        cnt = cnt + 1
                        write_error = False

                except Exception as ex:
                    ut.handle_exception(ex)
                    logger.info('notify file Not OK')
                    write_error = True

                if not write_error:
                    # notify the png display service
                    with open(screen_file + '.screen.log', 'w') as f:
                        f.write('OK\n')
                        logger.info('notify screen OK, cnt %d' % cnt)

            # if (os.path.exists(screen_file)):
            #     screen = cv2.imread(screen_file)
            #     cv2.imshow('', screen)
            #     cv2.waitKey(1)

        except Exception as ex:
            ut.handle_exception(ex)

        ut.limit_fps_by_sleep(MAX_FPS, t0)


if __name__ == '__main__':
    render_dir = "./log"
    screen_file = "./log/screen.png"
    cam_type = ut.get_config('cam_type', 0)
    roi_translation = ut.get_config('roi_translation', (0, 0))
    roi_l_w_ratio = ut.get_config('roi_l_w_ratio', 0.5)
    Thread(target=runImageRendererThread).start()
    http_server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
