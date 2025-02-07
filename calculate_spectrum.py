# 周波数振幅スペクトルの計算
# Laplacianフィルタ(8近傍)を使用する

import numpy as np

laplacian_filter = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

print(f"Laplacianフィルタ: {laplacian_filter}")

result_fft2 = np.fft.fft2(laplacian_filter)
print(f"周波数スペクトル: {result_fft2}")

result_fft2_abs = np.abs(result_fft2)
print(f"周波数振幅スペクトル(絶対値): {result_fft2_abs}")