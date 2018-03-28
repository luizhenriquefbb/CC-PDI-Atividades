import pdb
from numpy import mean

def calculateMeanAndAplly(p1,p2,p3):
    '''
    Calcula a media de tres pixels e retorna um pixel com essa media
    '''
    
    average = mean([p1,p2,p3])

    return [average,average,average]

def toGreen(p1,p2,p3):
    '''
    converte todo o pixel para a banda verde
    '''
    return [0,p2,0]

def toRed (p1,p2,p3):
    '''
    converte todo o pixel para a banda vermelha
    '''
    return [0,0,p3]

def toBlue (p1,p2,p3):
    '''
    converte todo o pixel para a banda azul
    '''
    return [p1,0,0]
    


