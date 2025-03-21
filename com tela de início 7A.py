import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
largura, altura = 1080, 1920
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cobrinha")

# Carregar a imagem de fundo
fundo = pygame.image.load("Espaco.jpg").convert()  # Certifique-se que o arquivo está na pasta
fundo = pygame.transform.scale(fundo, (largura, altura))  # Ajustar a imagem ao tamanho da tela

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
cinza = (50, 50, 50, 180)  # Cinza semi-transparente
# Cores adicionais para a tela de início
cinza_claro = (150, 150, 150)
amarelo = (255, 255, 0)

# Configuração da cobrinha
tamanho = 20

# Bordas brancas
borda_espessura = 10

# Fontes para textos
fonte = pygame.font.Font(None, 50)
fonte_game_over = pygame.font.Font(None, 100)
fonte_titulo = pygame.font.Font(None, 150)   # Para o título "SnakePoint"
fonte_jogar = pygame.font.Font(None, 80)       # Para o botão "Jogar"
fonte_credito = pygame.font.Font(None, 40)     # Para os créditos "Gil Productions"

# Botões de controle (para o jogo)
botao_tamanho = 100
pos_centro_x = largura // 2
pos_baixo = altura - 200  # Posição base dos botões

botoes = {
    "cima": pygame.Rect(pos_centro_x - botao_tamanho // 2, pos_baixo - botao_tamanho + 300, botao_tamanho + 30, botao_tamanho + 30),
    "baixo": pygame.Rect(pos_centro_x - botao_tamanho // 2, pos_baixo + botao_tamanho + 300, botao_tamanho + 30, botao_tamanho + 30),
    "esquerda": pygame.Rect(pos_centro_x - botao_tamanho - 150, pos_baixo + 300, botao_tamanho + 30, botao_tamanho + 30),
    "direita": pygame.Rect(pos_centro_x + botao_tamanho + 50, pos_baixo + 300, botao_tamanho + 30, botao_tamanho + 30),
}

def desenhar_botoes():
    """ Desenha os botões de controle com setas. """
    for botao in botoes.values():
        pygame.draw.rect(tela, branco, botao, 2)

    # Setas dentro dos botões
    pygame.draw.polygon(tela, branco, [(botoes["cima"].centerx - 10, botoes["cima"].centery + 10),
                                       (botoes["cima"].centerx + 10, botoes["cima"].centery + 10),
                                       (botoes["cima"].centerx, botoes["cima"].centery - 10)])

    pygame.draw.polygon(tela, branco, [(botoes["baixo"].centerx - 10, botoes["baixo"].centery - 10),
                                       (botoes["baixo"].centerx + 10, botoes["baixo"].centery - 10),
                                       (botoes["baixo"].centerx, botoes["baixo"].centery + 10)])

    pygame.draw.polygon(tela, branco, [(botoes["esquerda"].centerx + 10, botoes["esquerda"].centery - 10),
                                       (botoes["esquerda"].centerx + 10, botoes["esquerda"].centery + 10),
                                       (botoes["esquerda"].centerx - 10, botoes["esquerda"].centery)])

    pygame.draw.polygon(tela, branco, [(botoes["direita"].centerx - 10, botoes["direita"].centery - 10),
                                       (botoes["direita"].centerx - 10, botoes["direita"].centery + 10),
                                       (botoes["direita"].centerx + 10, botoes["direita"].centery)])

def desenhar_bordas():
    """ Desenha as bordas na parte superior, laterais e acima dos botões. """
    # Borda superior
    pygame.draw.rect(tela, branco, (0, 0, largura, borda_espessura))
    # Borda esquerda
    pygame.draw.rect(tela, branco, (0, 0, borda_espessura, altura))
    # Borda direita
    pygame.draw.rect(tela, branco, (largura - borda_espessura, 0, borda_espessura, altura))
    # Borda inferior (acima dos botões)
    pygame.draw.rect(tela, branco, (0, altura - 0, largura, borda_espessura))

def tela_game_over():
    """ Exibe a tela de game over e espera o jogador pressionar 'Recomeçar'. """
    while True:
        tela.fill(cinza)  # Tela escura com efeito de game over

        # Texto "Fim de Jogo!"
        texto_game_over = fonte_game_over.render("Fim de Jogo!", True, vermelho)
        tela.blit(texto_game_over, (largura // 2 - 200, altura // 2 - 200))

        # Botão de "Recomeçar"
        botao_recomecar = pygame.Rect(largura // 2 - 100, altura // 2, 200, 80)
        pygame.draw.rect(tela, azul, botao_recomecar)
        texto_recomecar = fonte.render("Recomeçar", True, branco)
        tela.blit(texto_recomecar, (botao_recomecar.x + 30, botao_recomecar.y + 20))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_recomecar.collidepoint(evento.pos):
                    return  # Sai da tela de game over e reinicia o jogo

def tela_inicio():
    """ Exibe a tela de início até o jogador pressionar 'Jogar'. """
    rodando = True
    while rodando:
        # Tela toda preta
        tela.fill(preto)

        # Título "SnakePoint" com efeito brilhante
        texto_titulo = fonte_titulo.render("SnakePoint", True, branco)
        tela.blit(texto_titulo, (largura // 2 - texto_titulo.get_width() // 2, 300))

        # Botão "Jogar" escrito em cinza
        botao_jogar = pygame.Rect(largura // 2 - 150, altura // 2, 300, 100)
        pygame.draw.rect(tela, cinza_claro, botao_jogar)
        texto_jogar = fonte_jogar.render("Jogar", True, preto)
        tela.blit(texto_jogar, (botao_jogar.x + (botao_jogar.width - texto_jogar.get_width()) // 2,
                                botao_jogar.y + (botao_jogar.height - texto_jogar.get_height()) // 2))

        # "Gil Productions" no rodapé esquerdo, em amarelo e pequeno
        texto_credito = fonte_credito.render("Gil Productions", True, amarelo)
        tela.blit(texto_credito, (20, altura - 50))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    rodando = False  # Sai da tela de início e começa o jogo

def reiniciar_jogo():
    """ Reinicia as configurações do jogo. """
    global cobra, direcao, comida, pontuacao
    cobra = [(largura // 2, altura // 2)]
    direcao = (tamanho, 0)
    comida = (random.randint(0, (largura - tamanho) // tamanho) * tamanho,
              random.randint(0, (altura - tamanho) // tamanho) * tamanho)
    pontuacao = 0

# Chama a tela de início antes de iniciar o jogo
tela_inicio()

# Loop principal do jogo
rodando = True
relogio = pygame.time.Clock()

while rodando:
    reiniciar_jogo()

    while True:
        # Desenha o fundo espacial
        tela.blit(fundo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != (0, tamanho):
                    direcao = (0, -tamanho)
                elif evento.key == pygame.K_DOWN and direcao != (0, -tamanho):
                    direcao = (0, tamanho)
                elif evento.key == pygame.K_LEFT and direcao != (tamanho, 0):
                    direcao = (-tamanho, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-tamanho, 0):
                    direcao = (tamanho, 0)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if botoes["cima"].collidepoint(x, y) and direcao != (0, tamanho):
                    direcao = (0, -tamanho)
                elif botoes["baixo"].collidepoint(x, y) and direcao != (0, -tamanho):
                    direcao = (0, tamanho)
                elif botoes["esquerda"].collidepoint(x, y) and direcao != (tamanho, 0):
                    direcao = (-tamanho, 0)
                elif botoes["direita"].collidepoint(x, y) and direcao != (-tamanho, 0):
                    direcao = (tamanho, 0)

        # Movimentação da cobrinha
        nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
        # Teletransporte nas bordas
        nova_cabeca = (nova_cabeca[0] % largura, nova_cabeca[1] % altura)
        cobra.insert(0, nova_cabeca)

        # Verificar colisão com o próprio corpo
        if cobra[0] in cobra[1:]:
            tela_game_over()
            break

        # Comer a comida
        if nova_cabeca == comida:
            pontuacao += 1
            comida = (random.randint(0, (largura - tamanho) // tamanho) * tamanho,
                      random.randint(0, (altura - tamanho) // tamanho) * tamanho)
        else:
            cobra.pop()

        # Desenhar elementos do jogo
        pygame.draw.rect(tela, vermelho, (*comida, tamanho, tamanho))
        for segmento in cobra:
            pygame.draw.rect(tela, verde, (*segmento, tamanho, tamanho))

        # Exibir pontuação
        tela.blit(fonte.render(f"Pontos: {pontuacao}", True, branco), (largura // 2 - 50, 20))

        # Desenhar botões e bordas
        desenhar_botoes()
        desenhar_bordas()

        pygame.display.update()
        relogio.tick(10)