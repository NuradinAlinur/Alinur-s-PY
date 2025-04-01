import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))

# ПРАВИЛЬНЫЙ СПОСОБ УКАЗАНИЯ ПУТЕЙ
background = pygame.image.load(
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\PY\lab7\AndreyGubin.jpg")
background = pygame.transform.scale(background, (300, 300))

songs = [
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Zabytyjj_tobojj_48331001.mp3",
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Za_tobojj_61745032.mp3",
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Liza_62061433.mp3"
]

current_song = 0

pygame.mixer.init()

# Запуск первой песни
pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music = True
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза и продолжение
                if music:
                    pygame.mixer.music.pause()
                    music = False
                else:
                    pygame.mixer.music.unpause()
                    music = True

            elif event.key == pygame.K_RIGHT:  # Следующая песня
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:  # Предыдущая песня
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()
