import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

background = pygame.image.load(
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\PY\lab7\AndreyGubin.jpg")


def scale_image():
    bg_width, bg_height = background.get_size()
    screen_width, screen_height = screen.get_size()
    scale_factor = min(screen_width / bg_width, screen_height / bg_height)
    new_width = int(bg_width * scale_factor)
    new_height = int(bg_height * scale_factor)
    return pygame.transform.scale(background, (new_width, new_height)), new_width, new_height


songs = [
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Zabytyjj_tobojj_48331001.mp3",
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Za_tobojj_61745032.mp3",
    r"C:\Users\nurad\OneDrive\Рабочий стол\KBTU\Py\lab7\Andrejj_Gubin_-_Liza_62061433.mp3"
]

current_song = 0
pygame.mixer.init()
pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music = True
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music:
                    pygame.mixer.music.pause()
                    music = False
                else:
                    pygame.mixer.music.unpause()
                    music = True
            elif event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(
                (event.w, event.h), pygame.RESIZABLE)

    scaled_bg, bg_width, bg_height = scale_image()
    screen.fill((0, 0, 0))
    screen.blit(scaled_bg, ((screen.get_width() - bg_width) //
                2, (screen.get_height() - bg_height) // 2))
    pygame.display.flip()
