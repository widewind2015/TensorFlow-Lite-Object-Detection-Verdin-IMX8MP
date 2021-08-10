import cv2


def show_webcam(mirror=False):
    #gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg,width=1280,height=720,framerate=30/1 ! jpegdec ! videoconvert ! waylandsink
    cam = cv2.VideoCapture(" v4l2src device=/dev/video0 ! image/jpeg,width=1280,height=720,framerate=30/1 ! jpegdec ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    if not cam.isOpened():
        print("Cannot capture from camera. Exiting.")
        quit()
    fps = 24
    frame_width = 1280
    frame_height = 720
    # cam = cv2.VideoCapture("v4l2src  device=/dev/video0   ! image/jpeg,width=1280,height=720,framerate=30/1 ! jpegdec ! appsink")
    #cam.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
    #cam.set(3,1280)
    #cam.set(4,720)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    #cam.set(cv2.CAP_PROP_FPS, fps)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=False)


if __name__ == '__main__':
    main()