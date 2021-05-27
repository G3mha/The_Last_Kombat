"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame

# Estabelece a pasta que contem as sprites.
LEFTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueLEFT.png'
RIGHTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png'
UPblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueUP.png'
DOWNblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueDOWN.png'
LEFTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png'
RIGHTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowRIGHT.png'
UPyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowUP.png'
DOWNyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowDOWN.png'
derezzedSONG_dir = 'AUDIO/DerezzedSong.ogg'
derezzedSFX_dir = 'AUDIO/DerezzedFX.ogg'
derezzedVFX_dir = 'SPRITES/VFX DEREZZED EXPLOSION.png'

# Algumas variáveis essenciais para a aplicação
screen_size = (1024,768) # Largura e altura da tela
lightcicle_size = (200,100) # Tamanho da bike
page_title = "Corrida de motos" # Define o nome desta página

# Define o código RGB das cores que utilizadas
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_LIGHT = (0,0,195)
YELLOW_GOLD = (255,215,0)


class yellowLightCicle(pygame.sprite.Sprite):
    def __init__(self, group, LEFTyellow_dir):
        super().__init__(group)
        self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
        self.rect = self.image.get_rect()
        self.set_position(1024,0)
        self.set_velocity(-0.4,0) # VALOR TESTE
        self.direction = "LEFT"
        self.trace = []

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction,LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir):
        if direction != self.direction:
            if direction == "UP":
                self.image = pygame.image.load(UPyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,0.4) # VALOR TESTE
            if direction == "DOWN":
                self.image = pygame.image.load(DOWNyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,-0.4) # VALOR TESTE
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(-0.4,0) # VALOR TESTE
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0.4,0) # VALOR TESTE
            self.direction = direction

    def update_position(self, time):
        self.position += self.velocity * time
        # self.trace.append(self.position)


# Rotina Inicial do jogo
pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo


# Rotinas de aúdio
pygame.mixer.music.load(derezzedSONG_dir)
pygame.mixer.music.set_volume(0.04)  # VALOR TESTE
pygame.mixer.music.play(-1)  # VALOR TESTE

# variável que declara o clock do jogo
clock = pygame.time.Clock()

# cria sprite da Moto Amarela
sprites = pygame.sprite.Group()
yellow = yellowLightCicle(sprites, LEFTyellow_dir)

# Início do main Loop
while True:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yellow.update_direction("LEFT",LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir)
            elif event.key == pygame.K_RIGHT:
                yellow.update_direction("RIGHT",LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir)
            elif event.key == pygame.K_UP:
                yellow.update_direction("UP",LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir)
            elif event.key == pygame.K_DOWN:
                yellow.update_direction("DOWN",LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir)

    # Rotinas da tela "estática"
    surface.fill(BLUE)
    thickness = 10
    # Desenha borda da tela
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (screen_size[0],0), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (0,screen_size[1]), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (screen_size[0],0), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (0,screen_size[1]), thickness)
    static_horizontal = 1024/6 # espaço entre cada quadrado
    static_vertical = 768/6 # espaço entre cada quadrado
    for static_lines in range(1,9):
        pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(static_lines*static_horizontal)), (1024,(static_lines*static_horizontal)), thickness) # linha horizontal
        pygame.draw.line(surface, BLUE_MIDNIGHT, ((static_lines*static_vertical),0), ((static_lines*static_vertical),768), thickness) # linha vertical

    sprites.draw(surface)
    yellow.update_position(time)


    # if trace.rect.collidepoint( ): # TODO definir trace
    #     mask_point = [int(circle_position[0] - sprite.rect.x), int(circle_position[1] - sprite.rect.y)]
    #     if sprite.mask.get_at(mask_point):
    #         sprite.kill()
    #         score += 1


    pygame.display.update() # atualiza o display
