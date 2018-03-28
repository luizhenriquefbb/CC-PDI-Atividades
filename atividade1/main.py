import cv2 #openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import pdb
import config
import numpy as np
from math import trunc

def main():
	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(config.imageToRead)
	# img = cv2.cvtColor(cv2.imread(config.imageToRead),  cv2.COLOR_BGR2RGB)
	

	# Converter todos os pixels para YIQ
	# img2 = convertAllBGRtoYIQ(img)
	img2 = applyToAllPixels(img, BGRtoYIQ)
	
	# Converter todos os pixels para RGB
	# img3 =  convertAllYIQtoBGR(img2)
	img3 = applyToAllPixels(img2, YIQtoBGR)


	# TODO: exibindo errado por algum motivo
	# # exibir imagem em uma janela separada
	# cv2.imshow('image',img3)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	
	# salvar arquivo transformado
	cv2.imwrite('newImage.png',img3)




def BGRtoYIQ(b,g,r):
	y = 0.299*r + 0.587*g + 0.114*b
	i = 0.596*r - 0.274*g - 0.322*b
	q = 0.211*r - 0.523*g + 0.312*b


	return [y,i,q]

def YIQtoBGR(y,i,q):
	r = (y + 0.956*i + 0.621*q)
	if r > 255:
		r = 255
	elif r < 0:
		r = 0

	g = (y - 0.272*i - 0.647*q)
	if g > 255:
		g = 255
	elif g < 0:
		g = 0

	b = (y - 1.106*i + 1.703*q)
	if b > 255:
		b = 255
	elif b < 0:
		b = 0

	return [trunc(b),trunc(g),trunc(r)]

def convertArrayToNumpy(array):
	'''	
	Coloca um array em forma de numpy_array pq eh o tipo de objeto que o openCV usa
	'''
	array_numPy = np.empty((len(array), len(array[0]), 3))

	for row in range(len(array)):
		for colunm in range(len(array[row])):
			array_numPy[row][colunm] = array[row][colunm]

	return array_numPy

def applyToAllPixels(img, action):
	'''
	Aplica uma uma funcao para todos os pixels
	parametros:
		img: array.numpy ou simplesmente um array 3-dimensional que contem os pixels
		action: acao que vai ser implementada nos pixels
	'''

	height = len(img)
	width = len(img[0])

	# Usar metodo pixel a pixel
	newImage = []
	for h in range(height):
		newImage.append([])
		for w in range(width):
			# print(img[h][w])
			newImage[-1].append(action(img[h][w][0], img[h][w][1],  img[h][w][2]))

	return convertArrayToNumpy(newImage)

if __name__ == '__main__':
	main()