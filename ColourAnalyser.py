import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import time

kernal = np.ones((15,1),np.uint8)
kernal2 = np.ones((5,1),np.uint8)


boundaries = [
    ([40, 0, 0], [160, 255, 30]), #black
    ([100, 100, 0], [104, 130, 255]),#brown
    ([145,50,0], [180,100,255]), #red
    ([150,60,0], [255,120,150]),#orange
    ([105,00,0], [110,55,255]),#yellow
    ([59,134,61], [139,154,81]),#green
    ([65,153,61], [145,213,81]),#blue
    ([30,28,130], [50,35,200]),#violet
    ([110,108,0],[115,115,255]),#grey
    ([70,0,0], [110,70,255]),#white
]


#setup for detector
params = cv2.SimpleBlobDetector_Params()
params.minThreshold=1
params.maxThreshold=255
params.filterByArea=True
params.minArea = 2
params.maxArea = 150
params.filterByColor = False
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
    
    
def ImageAnalyser(img2):
    img=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    #remove the part of resistor between bands
    removalMask = cv2.inRange(img,(75,40,40), (103,250,255))
    img[removalMask == 255] = [0,0,0]
    bandArray = []
    i = 0
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
            
        # find the colours within boundary
        mask = cv2.inRange(img, lower, upper)
        image = cv2.bitwise_and(img, img, mask = mask)
        
        #remove noise and connect parts
        renewImg = cv2.dilate(image,kernal,iterations = 3)
        renewImg = cv2.erode(renewImg,kernal,iterations = 2)
        renewImg = cv2.erode(renewImg,kernal2,iterations = 1)
        
        #cv2.imshow("images" + str(i), renewImg) #input for testing
        
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(renewImg) #find keypoints
        numOfBands = len(keypoints)
        print(numOfBands)
        #make array of keypoints and value
        for x in keypoints:
            if (numOfBands > 0):
                bandArray.append([i,x.pt[0]])
        i = i + 1
    value = CalculateVal(bandArray)
    return value
    
def CalculateVal(bandArray):
    #order the array according to x co-ordinates
    for g in range(len(bandArray)):
        tick = 0
        for j in bandArray:
            tick = tick+1
            if (tick < len(bandArray)):
                comparison = bandArray[tick]
                if j[1] > comparison[1]:
                    bandArray[tick] = j
                    bandArray[(tick-1)] = comparison
        
    print(bandArray)
    resistorVal = 0
    count = 1
    #calculate value of array
    for g in bandArray:
        if count == 1:
            resistorVal = (int(g[0]) * 100)
        if count == 2:
            resistorVal = resistorVal+(int(g[0]) * 10)
        if count == 3:
            resistorVal = resistorVal+(int(g[0]))
        if count == 4:
            if (g[0] == 1 or g[0] == 2):
                resistorVal = resistorVal*(10**int(g[0]))
        count = count + 1
        print(resistorVal)
    return resistorVal