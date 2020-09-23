import cv2

path = "arcoiris.jpg"
img = cv2.imread(path, 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

imgErosao = cv2.erode(img, kernel, iterations=4)

imgAbertura = cv2.dilate(imgErosao, kernel, iterations=4)

cv2.imshow('Imagem Original', img)
cv2.imshow('Abertura', imgAbertura)

cv2.waitKey(0)
