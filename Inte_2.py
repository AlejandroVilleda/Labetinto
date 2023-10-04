import pygame
import sys

TAMANO_CUADRO = 30    # Tamaño de los cuadros
TAMANO_MUNEQUITO = 17 # Tamaño del muñeco

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

# Coordenadas iniciales del muñequito
pos_x = 0
pos_y = 9

# Abre la matriz de lectura
with open('./Laberinto.txt', 'r') as f:
    # Lee la matriz
    lineas = f.readlines()

# Inicializa la matriz
matriz = []

# Iterar a través de las líneas y crear una lista de listas (matriz)
for linea in lineas:
    fila = [int(valor) for valor in linea.strip().split(',')]
    matriz.append(fila)

# Dimensiones de la ventana
ANCHO = len(matriz[0]) * TAMANO_CUADRO
ALTO = len(matriz) * TAMANO_CUADRO

# Inicializar pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto")

# Cargar la imagen del muñeco y redimensionarla
muneco_img = pygame.Surface((TAMANO_MUNEQUITO, TAMANO_MUNEQUITO))
muneco_img.fill(BLANCO)
muneco_img.set_colorkey(BLANCO)
pygame.draw.circle(muneco_img, NEGRO, (TAMANO_MUNEQUITO // 2, TAMANO_MUNEQUITO // 2), TAMANO_MUNEQUITO // 2)
muneco_img = muneco_img.convert_alpha()

# Crear una fuente para mostrar la letra 'V'
fuente_v = pygame.font.Font(None, 24)

# Crear una matriz para rastrear las áreas visitadas por el muñeco
areas_visitadas = [[False for _ in fila] for fila in matriz]

# Crear una fuente para mostrar coordenadas generales
fuente = pygame.font.Font(None, 20)

# Crear una matriz para rastrear las áreas descubiertas
areas_descubiertas = [[False for _ in fila] for fila in matriz]

# Texto para fuente de V
letra_v = fuente_v.render('V', True, NEGRO)


def dibujar_muneco():
    ventana.blit(muneco_img, (pos_x * TAMANO_CUADRO, pos_y * TAMANO_CUADRO))


# Funcion que visualiza los alrededores del muñeco
def sensor_mirar():
    areas_descubiertas[pos_y][pos_x] = True

    if pos_y + 1 < len(matriz):
        areas_descubiertas[pos_y + 1][pos_x] = True
    if pos_x + 1 < len(matriz[0]):
        areas_descubiertas[pos_y][pos_x + 1] = True
    if pos_y - 1 >= 0:
        areas_descubiertas[pos_y - 1][pos_x] = True
    if pos_x - 1 >= 0:
        areas_descubiertas[pos_y][pos_x - 1] = True

    areas_visitadas[pos_y][pos_x] = True


ganado = False;

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            # Mover el muñeco
            if evento.key == pygame.K_LEFT:
                if pos_x > 0 and matriz[pos_y][pos_x - 1] == 1:
                    pos_x -= 1
                    sensor_mirar()
            elif evento.key == pygame.K_RIGHT:
                if pos_x < len(matriz[0]) - 1 and matriz[pos_y][pos_x + 1] == 1:
                    pos_x += 1
                    sensor_mirar()
            elif evento.key == pygame.K_UP:
                if pos_y > 0 and matriz[pos_y - 1][pos_x] == 1:
                    pos_y -= 1
                    sensor_mirar()
            elif evento.key == pygame.K_DOWN:
                if pos_y < len(matriz) - 1 and matriz[pos_y + 1][pos_x] == 1:
                    pos_y += 1
                    sensor_mirar()
    if pos_x == 14 and pos_y == 1:
        ganado = True

    # Dibujar el laberinto
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if not areas_descubiertas[fila][columna]:
                color = GRIS  # Si no se ha descubierto, pintar de gris
            else:
                color = BLANCO if matriz[fila][columna] == 1 else NEGRO
            pygame.draw.rect(ventana, color,
                             (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))
            if areas_visitadas[fila][columna]:
                letra_v_rect = letra_v.get_rect()
                letra_v_rect.topleft = (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO)
                ventana.blit(letra_v, letra_v_rect)
    # Dibujar el muñeco
    dibujar_muneco()
    if ganado:
        mensaje = '¡Haz ganado!'
        fuente_ganado = pygame.font.Font(None, 36)
        mensaje_renderizado = fuente_ganado.render(mensaje, True, BLANCO)
        ventana.blit(mensaje_renderizado, (
        ANCHO // 2 - mensaje_renderizado.get_width() // 2, ALTO // 2 - mensaje_renderizado.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(5000)  # Espera 5 segundos

        pygame.quit()
        sys.exit()

    # Mostrar coordenadas generales en la ventana
    coordenadas = f'Coordenadas: ({pos_x}, {pos_y})'
    texto = fuente.render(coordenadas, True, BLANCO)
    ventana.blit(texto, (10, 10))
    pygame.display.update()

    # Coordenadas de inicio.
    inicio_i = f'In'
    ini_i = fuente.render(inicio_i, True, NEGRO)
    ventana.blit(ini_i, (0, 9 * TAMANO_CUADRO))  # Coordenadas (0, 9) multiplicadas por el tamaño de cuadro

    inicio_f = f'F'
    ini_f = fuente.render(inicio_f, True, NEGRO)
    ventana.blit(ini_f,
                 (14 * TAMANO_CUADRO, 1 * TAMANO_CUADRO))  # Coordenadas (14, 1) multiplicadas por el tamaño de cuadro

    pygame.display.update()