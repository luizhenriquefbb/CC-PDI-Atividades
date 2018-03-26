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
	img2 = convertAllRGBtoYIQ(img)

	
	# Converter todos os pixels para RGB
	img3 =  convertAllYIQtoRGB(img2)


	# exibir imagem em uma janela separada
	cv2.imshow('image',img3)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	
	# salvar arquivo transformado
	# TODO: cv2.imwrite('image.png',img3)




def RGBtoYIQ(b,g,r):
	y = 0.299*r + 0.587*g + 0.114*b
	i = 0.596*r - 0.274*g - 0.322*b
	q = 0.211*r - 0.523*g + 0.312*b


	return [trunc(y),trunc(i),trunc(q)]

def YIQtoRGB(y,i,q):
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

def convertAllRGBtoYIQ(img):
	'''
	 le todo uma imagem e converte para YIQ pixel a pixel
	 parametros:
	 	img: [[[RGB]]]
	 	return: novaImagem
	'''
	height = len(img)
	width = len(img[0])

	# Usar metodo pixel a pixel
	newImage = []
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append(RGBtoYIQ(img[h][w][2], img[h][w][1], img[h][w][0]))

	return convertArrayToNumpy(newImage)

def convertAllYIQtoRGB(img):
	'''
	 le todo uma imagem e converte para RGB pixel a pixel
	 parametros:
	 	img: [[[YIQ]]]
	 	return: novaImagem
	'''
	height = len(img)
	width = len(img[0])

	# Usar metodo pixel a pixel
	newImage = []
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append(YIQtoRGB(img[h][w][2], img[h][w][1], img[h][w][0]))

	return convertArrayToNumpy(newImage)

if __name__ == '__main__':
	main()