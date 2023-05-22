import pygame, random

# definindo as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# definindo outras constantes do jogo
LARGURAJANELA = 400
ALTURAJANELA = 500
VEL = 6
ITERACOES = 30
TAMANHOBLOCO = 20

# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']

# definindo a função moverBloco(), que registra a posição do bloco
def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']

# inicializando pygame
pygame.init()

relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Teclado e Mouse')

# criando jogador
jogador = {'objRect': pygame.Rect(300, 100, 50, 50), 'cor': VERDE, 'vel': VEL}

# definindo o dicionario que guardará as direcoes pressionadas
teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}

# inicializando outras variáveis
contador = 0
blocos = []
deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        # quando uma tecla é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True

        # quando uma tecla é solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False

        # quando um botao do mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({'objRect': pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': 1})
    contador += 1
    if contador >= ITERACOES:
        # adicionando um novo bloco
        contador = 0
        posX = random.randint(0, LARGURAJANELA - TAMANHOBLOCO)
        posY = -TAMANHOBLOCO
        velRandom = random.randint(1, VEL + 3)
        blocos.append({'objRect': pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': velRandom})

    # preenchendo o fundo de janela com a cor preta
    janela.fill(PRETO)

    # movendo o jogador
    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    # desenhando jogador
    pygame.draw.rect(janela, jogador['cor'], jogador['objRect'])

    # checando se jogador bateu em algum bloco ou se bloco saiu da janela para retirá-lo da lista
    for bloco in blocos[:]:
        bateu = jogador['objRect'].colliderect(bloco['objRect'])
        if bateu or bloco['objRect'].y > ALTURAJANELA:
            blocos.remove(bloco)

    # movendo e desenhando os blocos
    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.rect(janela, bloco['cor'], bloco['objRect'])

    # atualizando a janela
    pygame.display.update()

    relogio.tick(40)

# encerrando módulos de Pygame
pygame.quit()