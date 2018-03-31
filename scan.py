from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='add path to input image')
ap.add_argument('-p', '--preprocess', type=str, default='thresh', help='type of preprocessing to be done')
args = vars(ap.parse_args())

# load the image and convert to grayscale for better accuracy
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the image (create a binary image)
if args['preprocess'] == 'thresh':
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove noise
if args["preprocess"] == 'blur':
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# write the grayscale image to disk as temporary file 
filename = '{}.png'.format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image
im = Image.open(filename)

# some images text is to small so we should resize those images
if args["preprocess"] == "resize":
    # if the user in the command line says to resize resize the image
    # implement using resize function and keeping same aspect ratio increase 200 percent 
    basewidth = im.width * 5 # you can change around with the basewidth to recieve optimal results
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth, hsize), Image.ANTIALIAS)
    print(im.width, im.height) # print the width and height of the image

text = pytesseract.image_to_string(im)
os.remove(filename)
print(text)

cv2.imshow('Image', image)
cv2.imshow('Output', gray)
cv2.waitKey(0)
