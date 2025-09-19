import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Dimensões da janela padrão
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Janela redimensionável
pygame.display.set_caption("Jogo com Redimensionamento de Tela")

# Cor de fundo
WHITE = (255, 255, 255)  # Cor de fundo da tela será branca

# Carregar a imagem do personagem
player_image = pygame.image.load("Isaac.png")  # Coloque o nome correto da sua imagem aqui
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centraliza a imagem

# Velocidade de movimento
VELOCITY = 8
GRAVITY = 0.2  # Gravidade que puxa o personagem para baixo
JUMP_STRENGTH = 20  # Força do pulo (quanto maior, mais alto o pulo)
is_jumping = False  # Verifica se o personagem está pulando
velocity_y = 0  # Velocidade vertical inicial do personagem

# Atualiza posição do personagem conforme o tamanho da tela
def update_player_position():
    global player_rect
    player_rect.center = (current_width // 2, current_height // 2)  # Centraliza a imagem ao centro da tela

# Função para verificar e controlar os redimensionamentos
def handle_resize(event):
    global screen, current_width, current_height
    current_width, current_height = event.w, event.h
    screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
    update_player_position()

# Limites de movimento (para não sair da tela)
def handle_boundaries():
    global player_rect, current_width, current_height
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > current_width:
        player_rect.right = current_width
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > current_height:
        player_rect.bottom = current_height

# Função para realizar o pulo
def jump():
    global velocity_y, is_jumping
    if not is_jumping:
        velocity_y = -JUMP_STRENGTH  # Inicia o pulo para cima
        is_jumping = True

# Função para atualizar o movimento do pulo
def update_jump():
    global velocity_y, player_rect, is_jumping
    velocity_y += GRAVITY  # Simula a gravidade
    player_rect.y += velocity_y  # Atualiza a posição Y do personagem

    # Se o personagem estiver tocando o chão novamente, para o pulo
    if player_rect.bottom >= HEIGHT:
        player_rect.bottom = HEIGHT
        velocity_y = 0
        is_jumping = False

# Loop principal
running = True
current_width, current_height = WIDTH, HEIGHT
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            handle_resize(event)

    # Verificação das teclas sendo apertadas
    keys = pygame.key.get_pressed()

    # Movimentação básica (setas)
    if keys[pygame.K_LEFT]:  # Move para a esquerda
        player_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:  # Move para a direita
        player_rect.x += VELOCITY
    if keys[pygame.K_UP]:  # Move para cima
        player_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:  # Move para baixo
        player_rect.y += VELOCITY
    if keys[pygame.K_SPACE]:  # Pular
        jump()

    # Atualiza pulo (se necessário)
    update_jump()

    # Limita o movimento para não sair da tela
    handle_boundaries()

    # Desenha fundo
    screen.fill(WHITE)

    # Desenha a imagem na tela
    screen.blit(player_image, player_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
