import cv2 #openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import pdb
import config
import numpy as np
from questao1 import *
from questao2 import *

def main():
	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(config.imageToRead)
	# img = cv2.cvtColor(cv2.imread(config.imageToRead),  cv2.COLOR_BGR2RGB)
	
	# imageResult = questao1(img)
	imageResult = questao2(img, 'green')

	# salvar arquivo transformado
	cv2.imwrite('newImage.png',imageResult)

def questao1(originalImage):

	# Converter todos os pixels para YIQ
	# img2 = convertAllBGRtoYIQ(img)
	img2 = applyToAllPixels(originalImage, BGRtoYIQ)
	
	# Converter todos os pixels para RGB
	# img3 =  convertAllYIQtoBGR(img2)
	img3 = applyToAllPixels(img2, YIQtoBGR)


	# TODO: exibindo errado por algum motivo
	# # exibir imagem em uma janela separada
	# cv2.imshow('image',img3)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return img3

def questao2(originalImage, color = 'gray'):
	'''
	Coloca a imagem em modo monocromatico

	Parametros:
		originalImage: ----
		color: string que siginfica a banda escolhida:
			gray: --- (default)
			red: ---
			green:---
			blue: ---
	'''

	imageResult = None

	if (color == 'gray'):
		# media dos  valores de cada pixel
		imageResult = applyToAllPixels(originalImage, calculateMeanAndAplly)
	

	# para cores primarias basta remover os outros valores
	elif (color == 'red'):
		imageResult = applyToAllPixels(originalImage, toRed)
	elif (color == 'blue'):
		imageResult = applyToAllPixels(originalImage, toBlue)
	elif (color == 'green'):
		imageResult = applyToAllPixels(originalImage, toGreen)
	else:
		print("cor invalida")
	
	return imageResult

def convertArrayToNumpy(array):
	'''	
	Coloca um array em forma de numpy_array pq eh o tipo de objeto que o openCV usa
	'''
	array_numPy = np.empty((len(array), len(array[0]), 3), dtype = 'int64')

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