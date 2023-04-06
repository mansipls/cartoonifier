import cv2

# Read the input image and convert it to grayscale
input_image = cv2.imread('sample.jpeg')
# height = int(input_image.shape[0]*0.35)
# width = int(input_image.shape[1]*0.35)
# dim = (width, height)
# input_image = cv2.resize(input, dim)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray_image)

# Apply median blur to the grayscale image
blur_image = cv2.medianBlur(gray_image, 5)
cv2.imshow("median_blurring", blur_image)
# cv2.imshow("Median blurred_image", blur_image)
# Edge preserved blurring
blurred_image = cv2.edgePreservingFilter(
    input_image, flags=1, sigma_s=150, sigma_r=0.9
)
cv2.imshow("Edge Preserved blurring", blurred_image)


# Apply adaptive thresholding to the blurred image
thresholded_image = cv2.adaptiveThreshold(
    blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
cv2.imshow("threshold", thresholded_image)

# Convert the thresholded image to a BGR image
cartoon_image = cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)
cv2.imshow("cartoon_image", cartoon_image)
cartoon = cv2.bitwise_and(input_image, cartoon_image)
cv2.imshow("masking", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img_enhanced = cv2.detailEnhance(cartoon, sigma_s=80, sigma_r=0.6)
cv2.imwrite('output_image.jpg', cartoon)
