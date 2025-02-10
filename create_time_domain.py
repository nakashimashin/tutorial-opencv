from VideoDigitalWatermarking import *

fnin = 'assets/input/my_icon.jpeg'
fnout = 'assets/output/time_domain_result.jpg'

secret_data = [1,1,1,1,0,0,0,0]

rgb_data = readColorImage(fnin)
red_data = getRgbLayer(rgb_data, rgb=RED)
embeded_red_data = embedBitReplace(red_data, secret_data, bit=1, interval=0)

height = red_data.shape[0]
width = red_data.shape[1]
for i in np.arange(height):
    for j in np.arange(width):
        rgb_data[i][j][RED] = embeded_red_data[i][j]

writeImage(fnout, rgb_data)