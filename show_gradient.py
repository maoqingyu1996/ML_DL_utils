import cv2
import matplotlib.pyplot as plt

image_path = ['1.jpg', '1_hazy.jpg']
# image_path = ['2.jpg', '2_hazy.jpg']
# image_path = ['3.jpg', '3_hazy.jpg']
# image_path = ['1425.png', '1425_10.png']
image_path = ['1446.png', '1446_10.png']
real_path = 'real.jpeg'


i_clear = cv2.imread(image_path[0], 1)  # 读取
i_hazy = cv2.imread(image_path[1], 1)
i_real = cv2.imread(real_path, 1)

print(i_real.shape)
print(i_clear.shape)

# i_clear = cv2.cvtColor(i_clear, cv2.COLOR_BGR2GRAY)  # BGR-RGB
# i_hazy = cv2.cvtColor(i_hazy,cv2.COLOR_BGR2GRAY)

i_clear = cv2.cvtColor(i_clear, cv2.COLOR_BGR2RGB)  # BGR-RGB
i_hazy = cv2.cvtColor(i_hazy,cv2.COLOR_BGR2RGB)
i_real = cv2.cvtColor(i_real,cv2.COLOR_BGR2RGB)

sobelx_c = cv2.convertScaleAbs(cv2.Sobel(i_clear, cv2.CV_64F, 1, 0, ksize=3))
sobely_c = cv2.convertScaleAbs(cv2.Sobel(i_clear, cv2.CV_64F, 0, 1,ksize =3))
sobel_clear = cv2.addWeighted(sobelx_c, 0.5, sobely_c, 0.5, 0)

sobelx_h = cv2.convertScaleAbs(cv2.Sobel(i_hazy, cv2.CV_64F, 1, 0, ksize=3))
sobely_h = cv2.convertScaleAbs(cv2.Sobel(i_hazy, cv2.CV_64F, 0, 1,ksize =3))
sobel_hazy = cv2.addWeighted(sobelx_h, 0.5, sobely_h, 0.5, 0)

sobelx_r = cv2.convertScaleAbs(cv2.Sobel(i_real, cv2.CV_64F, 1, 0, ksize=3))
sobely_r = cv2.convertScaleAbs(cv2.Sobel(i_real, cv2.CV_64F, 0, 1,ksize =3))
sobel_real = cv2.addWeighted(sobelx_r, 0.5, sobely_r, 0.5, 0)

# i_low_clear = i_clear - sobel_clear
# i_low_hazy = i_hazy - sobel_hazy
# gm = cv2.sqrt(sobelx ** 2 + sobely ** 2)
plt_camp = 'gray'
plt.subplot(231), plt.imshow(i_clear, cmap=plt_camp)
plt.subplot(232), plt.imshow(i_hazy, cmap=plt_camp)
plt.subplot(233), plt.imshow(i_real, cmap=plt_camp)
plt.subplot(234), plt.imshow(sobel_clear, cmap=plt_camp)
plt.subplot(235), plt.imshow(sobel_hazy, cmap=plt_camp)
plt.subplot(236), plt.imshow(sobel_real, cmap=plt_camp)
cv2.imwrite('clear_sobel.jpg', sobel_clear)
cv2.imwrite('hazy_sobel.jpg', sobel_hazy)
cv2.imwrite('real_sobel.jpg', sobel_real)


plt.figure()
plt.show()