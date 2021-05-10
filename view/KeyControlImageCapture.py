from djitellopy import tello
import KeyPressModule as kb
import time
import cv2

kb.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()
def getKeyInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50g`

    if kb.getKey("LEFT"):  lr = -speed
    elif kb.getKey("RIGHT"): lr = speed

    if kb.getKey("UP"):  fb = speed
    elif kb.getKey("DOWN"): fb = -speed

    if kb.getKey("w"):  ud = speed
    elif kb.getKey("s"): ud = -speed

    if kb.getKey("a"):  yv = speed
    elif kb.getKey("d"): yv = -speed

    if kb.getKey("q"):  me.land()
    if kb.getKey("e"):  me.takeoff()

    if kb.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)
    return [lr, fb, ud, yv]


while True:
    vals = getKeyInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


