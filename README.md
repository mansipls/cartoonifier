# cartoonifier


#Objective:
To cartoonify any image using opencv and python 
This can serve as a stencil for artists and illustrators

#Procedure:

Cartoonify any image using Open-cv, python
Step-1
Grayscaling the sample input image
Step-2
median blurring is used to remove noise, before thresholding the image
Step-3
Adaptive thresholding is applied to the image after median blurring
Step-4
The original image is then blurred using edge preserving blurring function
Step-5
The two images in Step 3 and Step 4 are then masked using bitwise and operator to give the final cartoonified image.
