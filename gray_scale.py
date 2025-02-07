import cv2

imread_result = cv2.imread('./assets/input/my_icon.jpeg', cv2.IMREAD_GRAYSCALE)

cv2.imwrite('./assets/output/imread_result.jpg', imread_result)

print(type(imread_result))
print(imread_result.shape)
print(imread_result.dtype)