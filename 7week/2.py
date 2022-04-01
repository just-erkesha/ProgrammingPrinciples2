import pygame#access the PyGame framework.
pygame.init()#initializes all the modules required for PyGame

_songs = ['song1.mp3', 'song2.mp3', 'song3.mp3']
music_number = int(0)
current_music = (_songs[music_number])
pygame.mixer.music.load(current_music)
pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)


def play_next_song():
    global _songs,current_music,music_number
    #pygame.mixer.music.stop()

    if music_number ==int(len(_songs)-1):
        music_number=int(0)
    else: music_number+=1

    current_music = (_songs[music_number])
    pygame.mixer.music.load(current_music)
    pygame.mixer.music.play()
    


def play_prev_song():
    global _songs,current_music,music_number

    if music_number ==int(0):
        music_number=int(len(_songs)-1)
    else: music_number-=1
    current_music = (_songs[music_number])
    pygame.mixer.music.load(current_music)
    pygame.mixer.music.play()


display = pygame.display.set_mode((100,100))
open = True
clock = pygame.time.Clock()

pygame.display.update()


while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        if event.type == MUSIC_END:
            play_next_song()
        if event.type==pygame.KEYDOWN and event.key== pygame.K_SPACE:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        if event.type==pygame.KEYDOWN and event.key== pygame.K_LEFT:
            play_prev_song()
        if event.type==pygame.KEYDOWN and event.key== pygame.K_RIGHT:
            play_next_song()
    


    display.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()