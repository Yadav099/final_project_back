
# Importing all libraries
import cv2
import os
import time
from werkzeug.utils import secure_filename

from app import app
def wait(user_data):
        user_data.save("data.mp4")

        time.sleep(5)

def video_converter(user_data):
    print(user_data)
    wait(user_data)
    if 1!=2:
        cam = cv2.VideoCapture('/home/yadav_padiyar/Desktop/finalColleg/Final_back/data.mp4')
        try:
            # creating a folder named data
            if not os.path.exists('data'):
                os.makedirs('data')
        # if not created then raise error

        except OSError:
            print('Error: Creating directory of data')
        # frame
        currentframe = 0
        while (True):
            # reading from frame
            ret, frame = cam.read()
            if ret:
                # if video is still left continue creating images
                name = './data/frame' + str(currentframe) + '.jpg'
                print('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()
        return "done"
