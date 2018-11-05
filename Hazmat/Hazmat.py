

#== IMPORTS ==#

from skimage.measure import compare_ssim
import imutils,cv2,ctypes,time,sys
from PIL import ImageGrab
import png,win32gui,ctypes,cv2,numpy as np,argparse,imutils,glob,pyscreenshot
from PIL import ImageGrab,ImageTk,Image,ImageFile
import time as t
import pyautogui as p


#== FUNCTIONS ==#
def isColourMatch(pic1,pic2):
  avgColour1 = np.average(np.average(pic1,axis=0),axis=0)
  avgColour2 = np.average(np.average(pic2,axis=0),axis=0)
  dif1 = abs(avgColour1[0] - avgColour2[0])
  dif2 = abs(avgColour1[1] - avgColour2[1])
  dif3 = abs(avgColour1[2] - avgColour2[2])
  if dif1 > colourThreshold or dif2 > colourThreshold or dif3 > colourThreshold:
    return False
  else:
    return True

def takeShot(filename, bbox, save=True):
  open(filename,"w").close() # Delete file
  if save:
    img = ImageGrab.grab(bbox)
    img.save(filename)
  else:
    img = ImageGrab.grab(bbox)
  return img

def getPixelByteWidth():
  filename = "temp.png"
  img = takeShot(filename)
  pixelByteWidth = 4 if png.Reader(filename).read_flat()[3]['alpha'] else 3
  open(filename).close() # Delete photo
  return pixelByteWidth



def resizeImage(img,maxSize): 
  height,width = img.shape[:2]
  shrinkMulti = 0.99
  while height>maxSize or width>maxSize:
    height *= shrinkMulti
    width *= shrinkMulti
  img = cv2.resize(img,(int(width),int(height)))
  return img

def findMatch(pic1name, pic2name): 
  # load the image image, convert it to grayscale, and detect edges
  pic1 = cv2.imread(pic1name)
  pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
  pic1 = resizeImage(pic1,150)
  pic1 = cv2.Canny(pic1, 50, 200)
  (tH, tW) = pic1.shape[:2]
  cv2.imshow("Template-gray", pic1)
  cv2.imshow("Template", template)
  # load the image, convert it to grayscale, and initialize the
  # bookkeeping variable to keep track of the matched region
  pic2 = cv2.imread(pic2name)
  gray = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)
  found = None

  # loop over the scales of the image

  for scale in np.linspace(0.2, 1.0, 20)[::-1]:
    # resize the image according to the scale, and keep track
    # of the ratio of the resizing
    resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
    
    r = gray.shape[1] / float(resized.shape[1])

    # if the resized image is smaller than the template, then break
    # from the loop
    if resized.shape[0] < tH or resized.shape[1] < tW:
      break
    # detect edges in the resized, grayscale image and apply template
    # matching to find the template in the image
    edged = cv2.Canny(resized, 50, 200)
    result = cv2.matchTemplate(edged, pic1, method)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    # check to see if the iteration should be visualized
    if visualize:
      # draw a bounding box around the detected region
      clone = np.dstack([edged, edged, edged])
      cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
        (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
      cv2.imshow("Visualize", clone)
      cv2.waitKey(0)

    # if we have found a new maximum correlation value, then ipdate
    # the bookkeeping variable
    colMatch = True
    '''
    if found != None:
      (_, maxLoc, r) = found
      (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
      (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
      cropped = resizeImage(frame[startY:endY,startX:endX],50)
      colMatch = isColourMatch(cropped,template)'''
    if found == None or maxVal > found[0] and colMatch:
      found = (maxVal, maxLoc, r)

  # unpack the bookkeeping varaible and compute the (x, y) coordinates
  # of the bounding box based on the resized ratio
  (_, maxLoc, r) = found
  (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
  (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

  # draw a bounding box around the detected result and display the image
  cv2.rectangle(pic2, (startX, startY), (endX, endY), (0, 0, 255), 2)
  pic2 = resizeImage(pic2, 600)
  cv2.imshow("Image",pic2)
  cv2.waitKey(1)
  return found, startX,startY,endX,endY

#== GLOBALS ==#
# Methods - each identifies patterns in different ways
methods = [cv2.TM_CCOEFF,
           cv2.TM_CCOEFF_NORMED,
           cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED,
           cv2.TM_SQDIFF,
           cv2.TM_SQDIFF_NORMED]
method = methods[0] # Pick one
# Maximum size of one of the dimensions of output image
maxSize = 400
# Show image at each iteration or not
visualize = 0
# Threshold for match to be considered
threshold = 0 # Changes over time
thresholdError = 1000 # Dif between max thresh and value for it to be true
# FPS Inverse Mutltiplier - alternative to changing FPS
fpsScale = 5 # e.g. if 4, it will quarter the FPS.
# The threshold for avg colour (255) difference.
colourThreshold = 30 # Doesn't Work properly

#== MAIN ==#
pic1name = 'Flammable.png'
pic2name = 'capture.jpg'
cap = cv2.VideoCapture('Hazmat.mp4')
template = cv2.imread(pic1name)
template = resizeImage(template, maxSize)
frameCount = 0
while True:
  frameCount += 1
  res,frame = cap.read()
  frame = resizeImage(frame, maxSize)
  if frameCount % fpsScale == 0: # Only process data on every fpsScale'th frame
    cv2.imwrite(pic2name,frame)
    (maxVal, maxLoc, r), startX, startY, endX,endY = findMatch(pic1name,pic2name)
    cropped = resizeImage(frame[startY:endY,startX:endX],50)
    colMatch = isColourMatch(cropped,template)
    #print(maxVal,maxLoc,r,colMatch)
    cv2.imshow("cropped",cropped)
    match = False
    if maxVal > threshold:
      threshold = maxVal
      print("Threshold has been raised! Previous matches may be incorrect!")
    if maxVal > threshold-thresholdError:
      print("Match!")
    

'''
THRESHOLD TABLE - shows recommended for each method
TM_CCOEFF: >8000000
TM_CCOEFF_NORMED: 0.35
'''


