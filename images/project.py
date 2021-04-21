# Call packages
import requests
import urllib.request
import base64
import time
import json
import os
import collections
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import imutils
import math
plt.style.use('dark_background')

# Image capture from Station -> save it as photo.jpg


def StationWork():
    url = 'http://172.16.62.115:8080/photo.jpg'

    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url)

    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

    # Finally decode the array to OpenCV usable format ;)
    img = cv2.imdecode(imgNp, -1)

    # Save Image as photo.jpg
    cv2.imwrite('photo.jpg', img)

    # put the image on screen
    # plt.figure(figsize=(12,10))
    # plt.axis("off")
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.show()


# Using ALPR api to get String from CAR PLATE
def plateText(IMAGE_PATH):
    # Secret key from ALPR site
    SECRET_KEY = 'sk_3ad45d755d67600b8fcb0a78'

    # Open Image
    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    # search on API from Photo
    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=kor&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data=img_base64)
    json_data = r.json()
    x1_co = json_data['results'][0]['coordinates'][0]['x']
    y1_co = json_data['results'][0]['coordinates'][0]['y']
    x2_co = json_data['results'][0]['coordinates'][2]['x']
    y2_co = json_data['results'][0]['coordinates'][2]['y']

    # Crop plate from Original Image
    # error point will be +- 20 by y-axis
    img = Image.open(IMAGE_PATH)
    area = (x1_co, y1_co-20, x2_co, y2_co+20)
    crop = img.crop(area)
    crop.save('found_plate.jpg')


# Multiscale Template matching
def multiscale(template_name, gray ):
    # template will be 2 options. 
    # One is evmark2.png ( only Electronic Vehicle mark on plate. )
    # the other will be evorno.png ( this image for double check. )
    template_ori = cv2.imread(template_name)
    template = cv2.cvtColor(template_ori, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]

    found = None

    # loop over the scales of the image ( multiply 2 ~ 0.1 on Original image)
    for scale in np.linspace(0.1, 2.0, 50)[::-1] :

        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
        
        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        # if we have found a new maximum correlation value, then update
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r, scale, tW, tH)
    return found

# Find Highest correlation from Original Image by EV mark templates.
def FindRectangle():
    image = cv2.imread('found_plate.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# All these code for check.
#    template_ori = cv2.imread('evmark2.png')
#    template = cv2.cvtColor(template_ori, cv2.COLOR_BGR2GRAY)
#    template = cv2.Canny(template, 50, 200)
#    (tH, tW) = template.shape[:2]
#    print( multiscale('evmark2.png', gray) )
#    print( multiscale('evorno.png', gray) )
    found = None
    (_, maxLoc, r, scale, tW, tH) = multiscale('evmark2.png', gray)

    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
    if maxLoc <= (image.shape[1] * 0.15, image.shape[0] * 0.15): # Check if Square locate on left part of plate.
        evorno = True # If Square located on left. We assume that it's Electronic Vehicle
    else:
        evorno = False # If not, Suppose it is General Vehicle

    if evorno == True: # one more check : If evorno = True, Second multiscale Template Matching by evorno.png
        (_, maxLoc1, r1, scale1, tW, tH) = multiscale('evorno.png', gray)
        (startX1, startY1) = (int(maxLoc1[0] * r1), int(maxLoc1[1] * r1))
        (endX1, endY1) = (int((maxLoc1[0] + tW) * r1), int((maxLoc1[1] + tH) * r1))
        x_dif = abs(maxLoc[0]-maxLoc1[0]) # check difference betweed two results from Template matching
        y_dif = abs(maxLoc[1]-maxLoc1[1])

        if x_dif < 15 and y_dif < 15: # if Two points are close enough, it will be Electronic Vehicle.
            evorno = True
            last_image = cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            last_image = cv2.rectangle(last_image, (startX1, startY1), (endX1, endY1), (0, 255, 255), 2)
    else:
        evorno = False
        last_image = image

#    print(evorno)
#    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.show()
    return (last_image, evorno) # Return Image, truth
        
# Feature Matching in Image with trueev2.png
def ShowMatches(img):
    MIN_MATCH_COUNT = 3

    # Template Imag
    img1 = cv2.imread('trueev2.png') # this image have 3 special points from Electronic Vehicle plate.

    # Load Cropped Image
    img2 = cv2.imread(img)

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.6*n.distance: # 0.6 is 
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1, 1, 2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts)

        matchesMask = None
        h, w, d = img1.shape
        pts = np.float32([ [0, 0], [0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts, M)
        img2 = cv2.polylines(img2, [np.int32(dst)], False,255,3, cv2.LINE_AA)
    

    else:
        matchesMask = None
    print("Matches are found {}".format(len(good)))


    if len(good) < 1:
        plateIs = 'General Vehicle'
        img3 = img2
    else:
        plateIs = 'Eletronic Vehicle'

        draw_params = dict(matchColor = (0, 255, 0), # draw matches in green color
                       singlePointColor= None, # draw only inliers
                       flags= 0)
        img3 = cv2.drawMatches(img1, kp1, img2,kp2,good,None,**draw_params)
#    if len(good) < 3:
#        ori_img = cv2.imread(img)
#        o_w, o_h, o_g = ori_img.shape
#        o_w, o_h, o_g = np.int(o_w/2), np.int(o_h/2), np.int(o_g/2)
#        texted_image = cv2.putText(img=np.copy(ori_img), text=plateIs, org=(o_h, o_w),fontFace=1, fontScale=5, color=(0,0,255), thickness=2) 
#    else:
#        texted_image = cv2.putText(img=np.copy(img3), text=plateIs, org=(5, 50),fontFace=1, fontScale=1, color=(0,0,255), thickness=2)

#    plt.figure(figsize=(12, 10))
#    plt.axis("off")
#    plt.imshow(cv2.cvtColor(texted_image, cv2.COLOR_BGR2RGB)), plt.show()
    cv2.imwrite('saved.jpg', img3)
    return plateIs


# import image from IPwebcam. it's testing code. We suppose it will be on Charging system
def realtime_plate_recog():
    StationWork()
    FindRectangle('photo.jpg')
    ShowMatches()


def checkplate(image_name):

    image = image_name
    # calculate size of image
    KB = int( math.floor(os.path.getsize(image)/1024) )
    
    # if image size is smaller than 300KB, print this
    if KB < 30:
        result = "이미지 크기가 {}KB 입니다. 높은 화질의 이미지를 올려주세요.".format( KB )
        print(result)
        return result
    
    else:
        plateText(image)
        plate_name = 'found_plate.jpg' # saved from platText function
        plate = cv2.imread(plate_name)
        hsv_img = cv2.cvtColor(plate, cv2.COLOR_BGR2HSV) # image BGR color convert to hsv
        
        #################################
        # Blue color range -> Electronic Vehicle
        blue_mask = cv2.inRange(hsv_img, (85,80,20) , (125,255,255) )
        blue = cv2.bitwise_and(plate, plate, mask = blue_mask ) # if each point in range, result won't be 0.
        count_blue = np.count_nonzero( blue != 0 ) # count != 0 check how many blue points in Image.
        ##################################
        # print('Detected blue points {}'.format( count_blue )) # find blue points as 0
        
        ##################################
        # Green color -> General Vehicle
        green_mask = cv2.inRange(hsv_img, (40,80,20), (80,255,255) )
        green = cv2.bitwise_and(plate, plate, mask= green_mask )
        count_green = np.count_nonzero(green !=0 )
        ##################################
        # print('Detected Green points {}'.format( count_green ))
        
        ##################################
        # White color -> General Vehicle
        white_mask = cv2.inRange(hsv_img, (0,0,170) , (131, 255, 255) )
        white = cv2.bitwise_and(plate, plate, mask = white_mask)
        count_white = np.count_nonzero(white != 0)
        ##################################
        # print('Detected White points {}'.format( count_white ))
        
        ##################################
        # yellow color -> Commercial car
        yellow_mask = cv2.inRange(hsv_img, (15,80,20) , (35, 255, 255) )
        yellow = cv2.bitwise_and(plate, plate, mask = yellow_mask)
        count_yellow = np.count_nonzero(yellow != 0)
        ##################################
        # print('Detected Yellow points {}'.format( count_yellow ) )
        
        
        plate_list = [blue, green, white, yellow] # each plate Image list.
        value_list = [count_blue, count_green, count_white, count_yellow] # each number of points will be list.
        
        max_value = max(value_list) # Find max count in Value list
        index = value_list.index(max_value) # Find Index in Value list
        car_kinds = ['Electronic Vehicle','Not Electronic Vehicle']
        match_result = ShowMatches(plate_name) # show Feature Matching result
        save = cv2.imread('saved.jpg')
        
        if index == 0: # if blue points detected
            if FindRectangle()[1] == True: # Double check from Template Matching
                car = car_kinds[0] # Car will be EV
                plate_img = FindRectangle()[0]
                plt.subplot(211)
                plt.axis("off")
                plt.imshow(cv2.cvtColor( plate_img , cv2.COLOR_BGR2RGB))
                plt.subplot(212)
                plt.axis("off")
                plt.imshow(cv2.cvtColor( save, cv2.COLOR_BGR2RGB))
                plt.show()
            else: # Color = Blue but nothing detected from Template Matching
                car = car_kinds[1]
                plt.axis("off")
                plt.imshow(cv2.cvtColor( save, cv2.COLOR_BGR2RGB)) 
                plt.show()
        
        else: # When they found White or Green Color.
            car = car_kinds[1]
            plt.axis("off")
            plt.imshow(cv2.cvtColor( save, cv2.COLOR_BGR2RGB)) 
            plt.show()
            
        print( "This Car is {}".format(car) )
        return ( car , save )
    #    print(car)
        # print("This Car is {}".format(car) )
        # plt.imshow( cv2.cvtColor(plate_list[index], cv2.COLOR_BGR2RGB) )