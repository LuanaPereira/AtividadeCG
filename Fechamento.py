import cv2

path = "arcoiris.jpg"
img = cv2.imread(path, 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

imgDilatacao = cv2.dilate(img, kernel, iterations=4)
imgFechamento = cv2.erode(imgDilatacao, kernel, iterations=4)

cv2.imshow('Imagem Original', img)
cv2.imshow('Fechamento', imgFechamento)

cv2.waitKey(0)
