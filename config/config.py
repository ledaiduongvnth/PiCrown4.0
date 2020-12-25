# -*- coding: utf-8 -*-
#===============================================================================
# Messages
#===============================================================================
COMMON_ERROR_HANDLING = u'Xin vui lòng quẹt thẻ.'
COMMON_ERROR = u'Hệ thống nhận diện đang bị lỗi:'
CONNECTION_LOSS_CAM = u'Mất kết nối đến camera.'
CONNECTION_LOSS_SERVER = u'Mất kết nối đến server nhận diện.'
CONNECTION_LOSS_DOOR = u'Mất kết nối đến barrier.'

#===============================================================================
# Application configs
#===============================================================================
MAX_FPS = 10.0 # can set phu hop de pi khong bi qua tai
PROFILE_DISPLAY_MAX_TTL = 4 # thoi gian profile hien thi sau khi nguoi di qua (second)

OPACITY = 255
SCREEN_W = 1280
SCREEN_H = 800

COLOR_OK = (100, 230, 0)
COLOR_EXCEPTION = (40, 40, 230)

#===============================================================================
# User configs
#===============================================================================
BASE_IP = '10.61.212.'
MY_IP_SUFFIX = 13
PI_CF = {'cam_ip': 3, 'server': 20, 'roi_translation': (0, 0.05)}

SUPPORT_EMAIL = "admin@support.com"

NOTICE_LINES = [
    #u'Hệ thống đang trong quá trình thu thập dữ liệu.',
    #u'Nếu hệ thống không nhận diện bạn hoặc nhận chậm.',
    #u'Xin gửi (mã nhân viên của bạn, thời điểm qua cửa) đến:',
    #u'{}'.format(SUPPORT_EMAIL),
    #u'Để chúng tôi có thể khắc phục trong thời gian sớm nhất.',
]
