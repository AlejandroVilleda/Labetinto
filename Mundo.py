import pygame
import sys

TAMANO_CUADRO = 30
TAMANO_MUNEQUITO = 17

GRIS = (71, 75, 78)
CAFE = (161, 130, 98)
AZUL  = (59, 131, 189)
AMARILLO = (229, 190, 1)
VERDE = (0, 149, 57)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MORADO = (87, 35, 100)
ROJO = (255, 0 ,0)
VERDE_PERSONAJE = (0, 255, 0)       # COLOR PERSONAJE 1
NARANJA_PERSONAJE = (255, 64, 0)    # COLOR PERSONAJE 2
AZUL_PERSONAJE = (160, 206, 222)    # COLOR PERSONAJE 3

pos_x = 0
pos_y = 0

with open('C:/Users/S ALBERT FC/Documents/Mapa.txt', 'r') as f:
    lineas = f.readlines()

matriz = []
for linea in lineas:
    fila = [int(valor) for valor in linea.strip().split(',')]
    matriz.append(fila)

ANCHO = len(matriz[0]) * TAMANO_CUADRO
ALTO = len(matriz) * TAMANO_CUADRO

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa")

# Cargar imágenes de los personajes
personaje1 = pygame.image.load("personaje1.png")
personaje2 = pygame.image.load("personaje2.png")
personaje3 = pygame.image.load("personaje3.png")

# Definir función para mostrar el menú de selección de personaje
def mostrar_menu():
    ventana.fill(BLANCO)
    fuente = pygame.font.Font(None, 30)

    coordenadas = f'Escoja a su Personaje'
    texto = fuente.render(coordenadas, True, NEGRO)
    ventana.blit(texto, (115, 45))

    p1 = f'1'
    texto = fuente.render(p1, True, NEGRO)
    ventana.blit(texto, (85, 200))
    p2 = f'2'
    texto = fuente.render(p2, True, NEGRO)
    ventana.blit(texto, (211, 200))
    p3 = f'3'
    texto = fuente.render(p3, True, NEGRO)
    ventana.blit(texto, (345, 200))

    ventana.blit(personaje1, (60, 125))
    ventana.blit(personaje2, (183, 125))
    ventana.blit(personaje3, (317, 125))
    pygame.display.update()

# Bucle principal del programa
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.KEYDOWN:
#############################################################################################################################################################
            if evento.key == pygame.K_1: # Código para el personaje 1
                fuente_v = pygame.font.Font(None, 24)
                muneco_img = pygame.Surface((TAMANO_MUNEQUITO, TAMANO_MUNEQUITO))
                muneco_img.fill(BLANCO)
                muneco_img.set_colorkey(BLANCO)
                pygame.draw.circle(muneco_img, VERDE_PERSONAJE, (TAMANO_MUNEQUITO // 2, TAMANO_MUNEQUITO // 2), TAMANO_MUNEQUITO // 2)
                muneco_img = muneco_img.convert_alpha()

                fuente_v = pygame.font.Font(None, 20)
                fuente = pygame.font.Font(None, 20)
                areas_visitadas = [[False for _ in fila] for fila in matriz]

                def dibujar_muneco():
                    ventana.blit(muneco_img, (pos_x * TAMANO_CUADRO, pos_y * TAMANO_CUADRO))

                def sensor_mirar():
                    areas_visitadas[pos_y][pos_x] = True
                                        
                ganado = False;

                while True:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif evento.type == pygame.KEYDOWN:
                            # Mover el muñeco
                            if evento.key == pygame.K_LEFT:
                                if pos_x > 0:
                                    pos_x -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_RIGHT: 
                                if pos_x < len(matriz[0]) - 1:
                                    pos_x += 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_UP:
                                if pos_y > 0:
                                    pos_y -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_DOWN: 
                                if pos_y < len(matriz) - 1:
                                    pos_y += 1
                                    sensor_mirar()
                    if pos_x == 14 and pos_y == 14:
                        ganado = True

                    for fila in range(len(matriz)):             
                        for columna in range(len(matriz[0])):
                            if matriz[fila][columna] == 0:
                                color = GRIS
                            elif matriz[fila][columna] == 1:
                                color = CAFE
                            elif matriz[fila][columna] == 2:
                                color = AZUL
                            elif matriz[fila][columna] == 3:
                                color = AMARILLO
                            elif matriz[fila][columna] == 4:
                                color = VERDE
                            pygame.draw.rect(ventana, color, (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))
                            if areas_visitadas[fila][columna]:
                                letra_v_rect = letra_v.get_rect()
                                letra_v_rect.topleft = (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO)
                                ventana.blit(letra_v, letra_v_rect)

                    dibujar_muneco()
                    if ganado:
                        mensaje = '¡Haz ganado!'
                        fuente_ganado = pygame.font.Font(None, 36)
                        mensaje_renderizado = fuente_ganado.render(mensaje, True, BLANCO)
                        ventana.blit(mensaje_renderizado, (ANCHO // 2 - mensaje_renderizado.get_width() // 2, ALTO // 2 - mensaje_renderizado.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(2500)  # Espera 5 segundos

                        pygame.quit()
                        sys.exit()

                    coordenadas = f'Coordenadas: ({pos_x}, {pos_y})'
                    texto = fuente.render(coordenadas, True, NEGRO)
                    ventana.blit(texto, (10, 10))

                    letra_v = fuente_v.render('V', True, ROJO)

                    inicio = f'I'
                    texto = fuente.render(inicio, True, ROJO)
                    ventana.blit(texto, (0+5, 0+5))

                    if pos_x == 14 and pos_y == 14:
                        fin = f'F'
                        texto = fuente.render(fin, True, ROJO)
                        ventana.blit(texto, (pos_x*30 + 5, pos_y*30 + 5))
                    pygame.display.update()
#############################################################################################################################################################
            elif evento.key == pygame.K_2:          # Código para el personajee 2
                fuente_v = pygame.font.Font(None, 24)
                muneco_img = pygame.Surface((TAMANO_MUNEQUITO, TAMANO_MUNEQUITO))
                muneco_img.fill(BLANCO)
                muneco_img.set_colorkey(BLANCO)
                pygame.draw.circle(muneco_img, NARANJA_PERSONAJE, (TAMANO_MUNEQUITO // 2, TAMANO_MUNEQUITO // 2), TAMANO_MUNEQUITO // 2)
                muneco_img = muneco_img.convert_alpha()

                fuente_v = pygame.font.Font(None, 20)
                fuente = pygame.font.Font(None, 20)
                areas_visitadas = [[False for _ in fila] for fila in matriz]

                def dibujar_muneco():
                    ventana.blit(muneco_img, (pos_x * TAMANO_CUADRO, pos_y * TAMANO_CUADRO))

                def sensor_mirar():
                    areas_visitadas[pos_y][pos_x] = True
                                        
                ganado = False;

                while True:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif evento.type == pygame.KEYDOWN:
                            # Mover el muñeco
                            if evento.key == pygame.K_LEFT:
                                if pos_x > 0:
                                    pos_x -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_RIGHT: 
                                if pos_x < len(matriz[0]) - 1:
                                    pos_x += 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_UP:
                                if pos_y > 0:
                                    pos_y -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_DOWN: 
                                if pos_y < len(matriz) - 1:
                                    pos_y += 1
                                    sensor_mirar()
                    if pos_x == 14 and pos_y == 14:
                        ganado = True

                    for fila in range(len(matriz)):             
                        for columna in range(len(matriz[0])):
                            if matriz[fila][columna] == 0:
                                color = GRIS
                            elif matriz[fila][columna] == 1:
                                color = CAFE
                            elif matriz[fila][columna] == 2:
                                color = AZUL
                            elif matriz[fila][columna] == 3:
                                color = AMARILLO
                            elif matriz[fila][columna] == 4:
                                color = VERDE
                            pygame.draw.rect(ventana, color, (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))
                            if areas_visitadas[fila][columna]:
                                letra_v_rect = letra_v.get_rect()
                                letra_v_rect.topleft = (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO)
                                ventana.blit(letra_v, letra_v_rect)

                    dibujar_muneco()
                    if ganado:
                        mensaje = '¡Haz ganado!'
                        fuente_ganado = pygame.font.Font(None, 36)
                        mensaje_renderizado = fuente_ganado.render(mensaje, True, BLANCO)
                        ventana.blit(mensaje_renderizado, (ANCHO // 2 - mensaje_renderizado.get_width() // 2, ALTO // 2 - mensaje_renderizado.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(2500)  # Espera 5 segundos

                        pygame.quit()
                        sys.exit()

                    coordenadas = f'Coordenadas: ({pos_x}, {pos_y})'
                    texto = fuente.render(coordenadas, True, NEGRO)
                    ventana.blit(texto, (10, 10))

                    letra_v = fuente_v.render('V', True, ROJO)

                    inicio = f'I'
                    texto = fuente.render(inicio, True, ROJO)
                    ventana.blit(texto, (0+5, 0+5))

                    if pos_x == 14 and pos_y == 14:
                        fin = f'F'
                        texto = fuente.render(fin, True, ROJO)
                        ventana.blit(texto, (pos_x*30 + 5, pos_y*30 + 5))
                    pygame.display.update()
#############################################################################################################################################################
            elif evento.key == pygame.K_3:
                fuente_v = pygame.font.Font(None, 24)
                muneco_img = pygame.Surface((TAMANO_MUNEQUITO, TAMANO_MUNEQUITO))
                muneco_img.fill(BLANCO)
                muneco_img.set_colorkey(BLANCO)
                pygame.draw.circle(muneco_img, AZUL_PERSONAJE, (TAMANO_MUNEQUITO // 2, TAMANO_MUNEQUITO // 2), TAMANO_MUNEQUITO // 2)
                muneco_img = muneco_img.convert_alpha()

                fuente_v = pygame.font.Font(None, 20)
                fuente = pygame.font.Font(None, 20)
                areas_visitadas = [[False for _ in fila] for fila in matriz]

                def dibujar_muneco():
                    ventana.blit(muneco_img, (pos_x * TAMANO_CUADRO, pos_y * TAMANO_CUADRO))

                def sensor_mirar():
                    areas_visitadas[pos_y][pos_x] = True
                                        
                ganado = False;

                while True:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif evento.type == pygame.KEYDOWN:
                            # Mover el muñeco
                            if evento.key == pygame.K_LEFT:
                                if pos_x > 0:
                                    pos_x -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_RIGHT: 
                                if pos_x < len(matriz[0]) - 1:
                                    pos_x += 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_UP:
                                if pos_y > 0:
                                    pos_y -= 1
                                    sensor_mirar()
                            elif evento.key == pygame.K_DOWN: 
                                if pos_y < len(matriz) - 1:
                                    pos_y += 1
                                    sensor_mirar()
                    if pos_x == 14 and pos_y == 14:
                        ganado = True

                    for fila in range(len(matriz)):             
                        for columna in range(len(matriz[0])):
                            if matriz[fila][columna] == 0:
                                color = GRIS
                            elif matriz[fila][columna] == 1:
                                color = CAFE
                            elif matriz[fila][columna] == 2:
                                color = AZUL
                            elif matriz[fila][columna] == 3:
                                color = AMARILLO
                            elif matriz[fila][columna] == 4:
                                color = VERDE
                            pygame.draw.rect(ventana, color, (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))
                            if areas_visitadas[fila][columna]:
                                letra_v_rect = letra_v.get_rect()
                                letra_v_rect.topleft = (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO)
                                ventana.blit(letra_v, letra_v_rect)

                    dibujar_muneco()
                    if ganado:
                        mensaje = '¡Haz ganado!'
                        fuente_ganado = pygame.font.Font(None, 36)
                        mensaje_renderizado = fuente_ganado.render(mensaje, True, BLANCO)
                        ventana.blit(mensaje_renderizado, (ANCHO // 2 - mensaje_renderizado.get_width() // 2, ALTO // 2 - mensaje_renderizado.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(2500)  # Espera 5 segundos

                        pygame.quit()
                        sys.exit()

                    coordenadas = f'Coordenadas: ({pos_x}, {pos_y})'
                    texto = fuente.render(coordenadas, True, NEGRO)
                    ventana.blit(texto, (10, 10))

                    letra_v = fuente_v.render('V', True, ROJO)

                    inicio = f'I'
                    texto = fuente.render(inicio, True, ROJO)
                    ventana.blit(texto, (0+5, 0+5))

                    if pos_x == 14 and pos_y == 14:
                        fin = f'F'
                        texto = fuente.render(fin, True, ROJO)
                        ventana.blit(texto, (pos_x*30 + 5, pos_y*30 + 5))
                    pygame.display.update()
#############################################################################################################################################################
    mostrar_menu()

# Finalizar Pygame
pygame.quit()