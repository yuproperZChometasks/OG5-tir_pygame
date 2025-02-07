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
target_image = pygame.image.load("image\target.jpg")  # Убедитесь, что у вас есть изображение яблока
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                current_time = pygame.time.get_ticks()
                if target_visible and current_time - last_shot_time >= shot_time:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if target_x <= mouse_x <= target_x + 50 and target_y <= mouse_y <= target_y + 50:
                        # Попадание
                        print("Попал!")
                        shot_time = int(shot_time * 0.9)  # Уменьшаем время на 10%
                        last_shot_time = current_time
                        target_x = random.randint(0, WIDTH - 50)
                        target_y = random.randint(0, HEIGHT - 50)

    # Проверяем, прошло ли время
    current_time = pygame.time.get_ticks()
    if current_time - last_shot_time >= shot_time:
        target_visible = True
        last_shot_time = current_time
        target_x = random.randint(0, WIDTH - 50)
        target_y = random.randint(0, HEIGHT - 50)

    # Отрисовка
    screen.fill(WHITE)
    if target_visible:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.flip()

# Завершение Pygame
pygame.quit()
