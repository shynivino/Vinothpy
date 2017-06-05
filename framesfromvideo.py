## pip install opencv-python
##video must be saved in same directory
import cv2
vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,image = vidcap.read()
count = 0
success = True
while success and count <= 50:
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
print("completed")

