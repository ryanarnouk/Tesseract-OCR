# Tesseract-OCR
Optical Character Recognition made with Python and Tesseract
 
For this project I used Tesseract an Optical Character Recognition library and made a simple OCR engine that can recognize text from a document. The project also uses argparse to allow for command line usage

## Usage:
To use the script at the minimal level, you can simply run the script and add an image like this `--image image.jpg`
For Example:
`python scan.py --image image.jpg`

Also part of the script is some preprocessing options for example a blur may help in a noisy image
`python scan.py --image image.jpg --preprocess blur`

In addition, in an image where the font is small we can resize the image to something more sufficent
`python scan.py --image image.jpg --preprocess blur`

This is a small little project showcasing what you can do with OCR in such little lines of code, and you can implement stuff like this into mobile apps and more. 

This project was made with the latest stable version 3.05.01 and not the new unstable 4.0 version (as of March 2018)

Ryan A
