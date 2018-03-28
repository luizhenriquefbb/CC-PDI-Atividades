def addBrightness(b,g,r,parameters):
    '''
    Adiciona brilho a uma imagem de acordo com o valor brightness dado

	Parametros:
		parameters : Dicionario {'brightness': int}
    '''
    brightness = parameters.get('brightness')
    b = b + brightness
    g = (g + brightness)
    r = (r + brightness)
    if b > 255:
        b = 255
    elif g > 255:
        g = 255
    elif r > 255:
        r = 255
    
    return [b,g,r]
