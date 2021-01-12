# 1. import library yang diperlukan
import pygame
from pygame.locals import *
import math
<<<<<<< HEAD
from random import randint
=======
>>>>>>> 84fb25c94136594f736f65817dc011e77d150c52

# 2. inisialisasi game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = {
    "top": False,
    "bottom": False,
    "left": False,
    "right": False
}

running = True
<<<<<<< HEAD
playerpos = [100, 100]

score = 0
arrows = [] # list dari arrows

enemy_timer = 100 # waktu kemunculan
enemies = [[width, 100]] # list yang menampung koordinat musuh

=======

playerpos = [100, 100]
>>>>>>> 84fb25c94136594f736f65817dc011e77d150c52

# 3. load game assets
# load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
<<<<<<< HEAD
arrow = pygame.image.load("resources/images/bullet.png")
enemy_img = pygame.image.load("resources/images/badguy.png")
=======
>>>>>>> 84fb25c94136594f736f65817dc011e77d150c52

# 4. game loop
while(running):
    # 5. clear screen
    screen.fill(0)

    # 6. draw game object
    # draw grass
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_width()+1)):
            screen.blit(grass, (x*100, y*100))

    # draw castle
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # draw player
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation, new_playerpos)

<<<<<<< HEAD
    # 6.1 draw arrows
    for bullet in arrows:
        arrow_index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        # jika lewat layar maka hapus bullet dari list
        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            arrows.pop(arrow_index)
        arrow_index+=1

        #draw the arrow
        for projectile in arrows:
            new_arrow = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(new_arrow, (projectile[1], projectile[2]))

    # 6.2 draw enemy
    # waktu musuh akan muncul
    enemy_timer -= 1
    if enemy_timer == 0:
        # buat musuh baru
        enemies.append([width, randint(50, height-32)])
        # reset enemy timer to random time
        enemy_timer = randint(1, 100)

    index = 0
    for enemy in enemies:
        # musuh bergerak dengan kecepatan 5 pixel ke kiri
        enemy[0] -= 2
        # hapus musuh saat akan mencapai batas layar sebelah kiri
        if enemy[0] < -64:
            enemy.pop(index)

    # gambar musuh ke layar
    # for enemy in enemies:
        screen.blit(enemy_img, enemy)




=======
>>>>>>> 84fb25c94136594f736f65817dc011e77d150c52
    # 7. update screen
    pygame.display.flip()

    # 8. event loop
    for event in pygame.event.get():
        #even while exit button onclick
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

<<<<<<< HEAD
        # tembak!!
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrows.append([angle, new_playerpos[0]+32, new_playerpos[1]+32])

=======
>>>>>>> 84fb25c94136594f736f65817dc011e77d150c52
        # cek key bawah dan key atas
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_a:
                keys["left"] = True
            elif event.key == K_s:
                keys["bottom"] = True
            elif event.key == K_d:
                keys["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_a:
                keys["left"] = False
            elif event.key == K_s:
                keys["bottom"] = False
            elif event.key == K_d:
                keys["right"] = False

    if keys["top"]:
        playerpos[1] -= 5
    elif keys["bottom"]:
        playerpos[1] += 5
    elif keys["left"]:
        playerpos[0] -= 5
    elif keys["right"]:
        playerpos[0] += 5
