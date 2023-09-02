import pygame

pygame.init()

janela = pygame.display.set_mode([1280,720])
titulo = pygame.display.set_caption("Pong")

win = pygame.image.load("assets/win.png")

pontos1 = 0
pontos1_img = pygame.image.load("assets/score/0.png")
pontos2 = 0
pontos2_img = pygame.image.load("assets/score/0.png")

campo = pygame.image.load("assets/field.png")


player1 = pygame.image.load("assets/player1.png")
player1_y = 290
player1_movimentocima = False
player1_movimentobaixo = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 290

bola = pygame.image.load("assets/ball.png")
bola_x = 617
bola_y = 337
bola_dir = -5
bola_dir_y = 1


def movimento_player1():
    global player1_y
    if player1_movimentocima:
        player1_y -= 3
    else:
        player1_y += 0
    if player1_movimentobaixo:
        player1_y += 3
    else:
        player1_y += 0
    if player1_y <= -52:
        player1_y = -52
    elif player1_y >= 623:
        player1_y = 623

def movimento_player2():
    global player2_y
    player2_y = bola_y

def movimento_bola():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    global pontos1
    global pontos1_img
    global pontos2
    global pontos2_img

    bola_x += bola_dir
    bola_y += bola_dir_y

    if bola_x <= 130:
        if player1_y < bola_y + 46:
            if player1_y + 146 > bola_y:
                bola_dir *= -1
                bola_dir += 2


    if bola_x >= 1100:
        if player2_y < bola_y + 46:
            if player2_y + 146 > bola_y:
                bola_dir *= -1
                bola_dir += -2

    if bola_y > 680:
        bola_dir_y *= -1
    elif bola_y <= 0:
        bola_dir_y *= -1

    if bola_x < -47: #relacionado ao player1
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        bola_dir = -5
        pontos2 += 1
        pontos2_img = pygame.image.load("assets/score/" + str(pontos2) + ".png")


    elif bola_x > 1327: #relacionado ao player2
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        bola_dir = 5
        pontos1 += 1
        pontos1_img = pygame.image.load("assets/score/" + str(pontos1) + ".png")
def imagems():
    if pontos1 or pontos2 < 10:
        janela.blit(campo, (0, 0))
        janela.blit(player1, (50, player1_y))
        janela.blit(player2, (1150, player2_y))
        janela.blit(bola, (bola_x, bola_y))
        janela.blit(pontos1_img, (500, 50))
        janela.blit(pontos2_img, (710, 50))
        movimento_bola()
        movimento_player1()
        movimento_player2()
    else:
        janela.blit(win, (300, 300))

loop = True
while loop:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            loop = False
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_w:
                player1_movimentocima = True
            if eventos.key == pygame.K_s:
                player1_movimentobaixo = True
        if eventos.type == pygame.KEYUP:
            if eventos.key == pygame.K_w:
                player1_movimentocima = False
            if eventos.key == pygame.K_s:
                player1_movimentobaixo = False

    imagems()
    pygame.display.update()