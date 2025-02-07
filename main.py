import pygame

import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир: Стреляй в яблоки!")

# Загрузка изображения яблока
target_image = pygame.image.load("target.jpg")  # Убедитесь, что у вас есть изображение яблока
target_img = pygame.transform.scale(target_image, (50, 50))  # Масштабируем изображение

# Начальные параметры
target_x = random.randint(0, WIDTH - 50)
target_y = random.randint(0, HEIGHT - 50)
target_visible = True
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

shot_time = 1000  # Время на выстрел в миллисекундах
last_shot_time = pygame.time.get_ticks()




runnig = True

while runnig:
    pass



pygame.quit()
