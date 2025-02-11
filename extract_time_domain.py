from VideoDigitalWatermarking import *

fn_cover = 'assets/input/my_icon.jpeg'
fn_stego = 'assets/output/time_domain_result.jpg'

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

red_cover = getRgbLayer(rgb_cover, rgb=RED)
red_stego = getRgbLayer(rgb_stego, rgb=RED)

secret_data = extractBitReplace(red_cover, red_stego, 8, bit=1, interval=0)
print(secret_data)
