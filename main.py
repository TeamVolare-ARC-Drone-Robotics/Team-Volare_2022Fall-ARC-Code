#Import Modules
from djitellopy import Tello
import cv2
drone = Tello()

#Connect before anything
drone.connect()
#Start Code
drone.takeoff()
drone.streamon()

drone.flip_forward()

drone.streamoff()
drone.land()
#End Code

#Eitan's Test Commit 2