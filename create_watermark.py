import cv2
import numpy as np
from IPython.display import Image, display

def imshow(img):
    _, encoded = cv2.imencode('.png', img)
    display(Image(encoded))
    cv2.imwrite('./assets/output/imshow_result.jpg', img)


img = cv2.imread('./assets/input/my_icon.jpeg')
mark = cv2.imread('./assets/input/watermark.jpg')

x, y = 1, 1
roi = np.s_[y : y + mark.shape[0], x : x + mark.shape[1]]

img[roi] = cv2.addWeighted(img[roi], 1, mark, 0.3, 0)

imshow(img)