from threading import Thread
import time
import socket
import cv2
import numpy


class Inspector(Thread):

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "It's just the beginning of something great!"

    CAMERA_OFFSET = 1
    ENCODE_RATE = 50

    def __init__(self, port = UDP_PORT):
        Thread.__init__(self)
        self.port = port
        self.is_running = False

    def __str__(self):
        return repr(self) + self.port

    def start_inspector(self):
        self.is_running = True
        self.start()

    def stop_inspector(self):
        self.is_running = False

    def is_active(self):
        return self.is_running

    def run(self):
        cap = cv2.VideoCapture(0)
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY) ,self.ENCODE_RATE]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        previousImageSize = 0
        while self.is_active():
            for i in range(self.CAMERA_OFFSET):
                ret, frame = cap.read()

            if frame is None:
                continue

            result, imgencode = cv2.imencode('.jpeg', frame, encode_param)
            data = numpy.array(imgencode)
            imageAsString = data.tostring()

            print len(imageAsString)

            if len(imageAsString) > 65534:
            	continue

            imageSize = str(len(imageAsString))
            if imageSize == previousImageSize:
                continue
            previousImageSize = imageSize
            for i in range(8-len(imageSize)):
                imageSize ='0' + imageSize

            sock.sendto(imageSize, (self.UDP_IP, self.UDP_PORT))
            sock.sendto(imageAsString, (self.UDP_IP, self.UDP_PORT))

        cap.release()
        sock.close()

