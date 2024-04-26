import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Definir la clase Ball para representar las bolitas
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y, weight):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.weight = weight

    def draw(self, gravity, index):
        offset_y = index * 90  # Ajustar la posición vertical de la información
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.Font(None, 24)
        text = font.render(f"Velocidad: ({self.speed_x}, {self.speed_y})", True, WHITE)
        screen.blit(text, (10, 10 + offset_y))
        text_weight = font.render(f"Peso: {self.weight}", True, WHITE)
        screen.blit(text_weight, (10, 40 + offset_y))
        text_gravity = font.render(f"Gravedad: {gravity}", True, WHITE)
        screen.blit(text_gravity, (10, 70 + offset_y))
        pygame.draw.circle(screen, self.color, (150, 25 + offset_y), 5)  # Dibujar círculo de color al lado de la velocidad
        pygame.draw.circle(screen, self.color, (150, 55 + offset_y), 5)  # Dibujar círculo de color al lado del peso

    def update(self, gravity):
        self.speed_y += gravity / self.weight  # Aplicar la gravedad según el peso
        self.x += self.speed_x
        self.y += self.speed_y

        # Verificar los límites de la pantalla y cambiar de dirección si es necesario
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y + self.radius >= HEIGHT:
            if abs(self.speed_y) < 1:  # Detener el rebote si la velocidad vertical es muy baja
                self.y = HEIGHT - self.radius  # Ajustar la posición vertical para que quede en el borde inferior
                self.speed_y = 0  # Detener el movimiento vertical
            else:
                self.speed_y *= -0.9  # Invertir la dirección y reducir la velocidad vertical para simular el rebote

# Función principal del juego
def main():
    ball_red = Ball(WIDTH // 3, HEIGHT // 3, 20, RED, 3, 3, 1)  # Peso de 1 para la bola roja
    ball_blue = Ball(2 * WIDTH // 3, 2 * HEIGHT // 3, 20, BLUE, -3, -3, 2)  # Peso de 2 para la bola azul

    gravity = 0.2  # Gravedad general del sistema

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        # Actualizar y dibujar las bolitas
        ball_red.update(gravity)
        ball_red.draw(gravity, 0)
        ball_blue.update(gravity)
        ball_blue.draw(gravity, 1)

        pygame.display.flip()

# Ejecutar la función principal :D
if __name__ == "__main__":
    main()
