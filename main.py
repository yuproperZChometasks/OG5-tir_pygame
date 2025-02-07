import pygame

import pygame
import random
import time

# Инициализация Pygame
pygame.init()




# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир: Стреляй в яблоки!")

# Загрузка изображения яблока
# target_image = pygame.image.load("image\target.jpg")  # Убедитесь, что у вас есть изображение яблока

target_image = pygame.image.load("target.jpg")  # Убедитесь, что у вас есть изображение яблока
target_img = pygame.transform.scale(target_image, (80, 80))  # Масштабируем изображение

# Начальные параметры
target_x = random.randint(0, WIDTH - 80)
target_y = random.randint(0, HEIGHT - 80)
target_visible = True
# Цвета
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

shot_time = 4000  # Время на выстрел в миллисекундах
last_shot_time = pygame.time.get_ticks()

runnig = True

while runnig:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                current_time = pygame.time.get_ticks()
                if target_visible and current_time - last_shot_time < shot_time:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if target_x <= mouse_x <= target_x + 80 and target_y <= mouse_y <= target_y + 80:
                        # Попадание
                        print("Попал!")
                        shot_time = int(shot_time * 0.9)  # Уменьшаем время на 10%
                        last_shot_time = current_time
                        target_x = random.randint(0, WIDTH - 80)
                        target_y = random.randint(0, HEIGHT - 80)

    # Проверяем, прошло ли время
    current_time = pygame.time.get_ticks()
    if current_time - last_shot_time >= shot_time:
        target_visible = True
        last_shot_time = current_time
        target_x = random.randint(0, WIDTH - 80)
        target_y = random.randint(0, HEIGHT - 80)

    # Отрисовка
 
    if target_visible:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

# Завершение Pygame
pygame.quit()
