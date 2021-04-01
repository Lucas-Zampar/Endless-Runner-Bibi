import pygame, sys
from decimal import Decimal 

from classes.Constantes import *
from classes.Background import Background
from classes.Dino import Dino
from classes.Menina import Menina


def detectar_colisao(menina, dino):
    """
    Função responsável por detectar a colisão entre o dino e a heroina menina. Para tanto, realiza uma comparação entre os pontos de ambas as sprites. 
    Caso a coordenada x do ponto inferior direito do sprite da menina esteja no intervalo entre as coordenadas x dos pontos inferiores direito e esquerdo
    do sprite atual do dino e a coordenada y deste ponto da menina for menor que as dos pontos superiores do dino, ocorreu colisão, pois tal comparação 
    demonstra intersecção entre as duas imagens quando a menina realiza o salto ou está correndo. O mesmo vale para as coordenadas do ponto inferior esquerdo da menina.    
    """   
    if (dino.coordenada_retangular_inferior_esquerda.x <= menina.coordenada_retangular_inferior_direita.x <= dino.coordenada_retangular_inferior_direita.x
        and menina.coordenada_retangular_inferior_direita.y >= dino.coordenada_retangular_superior_direita.y):
        print('colisao1')
        return True
    
    if (dino.coordenada_retangular_inferior_esquerda.x <= menina.coordenada_retangular_inferior_esquerda.x <= dino.coordenada_retangular_inferior_direita.x 
        and menina.coordenada_retangular_inferior_esquerda.y >+ dino.coordenada_retangular_superior_direita.y):
        print('colisao2')
        return True
     
    return False

def detectar_pontuacao(menina, dino):
    """
    Função responsável por atribuir pontuação a menina. No intervalo de tempo necessário para a menina executar o salto, o dino já saiu da tela. 
    Dessa forma, caso não tenha havido colisão, toda vez que o dino sair da tela, há atribuição de pontos.
    """
    if dino.coordenada_retangular_inferior_direita.x + dino.velocidade_horizontal <=0:
        menina.ganhar_pontos()

def imprimir_pontuacao(tela, fonte_pontuacao, menina):
    """
    Imprime pontuação na tela
    """ 
    #define o render da pontuacao
    pontuacao = fonte_pontuacao.render(texto_pontuacao.format(menina.pontos), True, (255,255,255))
    #imprime a mensagem na tela
    tela.blit(pontuacao, (largura_tela//2+200, 30))   

def imprimir_game_over(tela, fonte_game_over):
    #define o render da mensagem game over
    mensagem_game_over = fonte_game_over.render(texto_game_over, True, (255,255,255))
    #define a variável na qual as coordenadas retangulares da mensagem game over serão armazenadas
    mensagem_game_over_rect = mensagem_game_over.get_rect()
    #define as coordenadas retangulares da menssagem
    mensagem_game_over_rect.center = (largura_tela//2, altura_tela//2)
    #imprime a mena
    tela.blit(mensagem_game_over, mensagem_game_over_rect)

def definir_timer():
    #define um timer
    pygame.time.set_timer(pygame.USEREVENT, intervalo_tempo_dificuldade)


#inicializa o pygame
pygame.init()
#define a tela de exibição
tela = pygame.display.set_mode((largura_tela, altura_tela))
#define o clock
clock = pygame.time.Clock()

#instancia o objeto background 
background = Background(tela)
#instancia o objeto dino
dino = Dino(tela)
#instancia o objeto menina
menina = Menina(tela)

#define a fonte para a menssagem de game over 
fonte_game_over = pygame.font.SysFont(tipo_fonte, tamanho_fonte_game_over, True, False)
#define a fonte para o texto da pontuação
fonte_pontuacao = pygame.font.SysFont(tipo_fonte, tamanho_fonte_pontuacao, True, False)

definir_timer()

while True: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            #encerra pygame
            pygame.quit()
            #encerra programa
            sys.exit()
        if evento.type == pygame.KEYDOWN: 
            #se houver pressionamento de tecla
            if evento.key == pygame.K_SPACE:
                #se a tecla for espaço
                #muda animação da menina para saltando 
                menina.mudar_animacao(tipo_animacao=1)
        if evento.type == pygame.USEREVENT:
            #se o intervalo de tempo definido pelo timer for atingido
            #incrementa a taxa de quadros, aumentando, assim, a velocidade global
            fps+= incremento_fps
    #atualize background
    background.atualizar()
    #atualiza dino
    dino.atualizar()
    #atualiza menina
    menina.atualizar()    

    if detectar_colisao(menina, dino): 
        #se houver colisão 
        #muda animação da menina para morrendo 
        menina.mudar_animacao(tipo_animacao=2)
        #muda animação do background para tornar-se estático
        background.mudar_animacao(tipo_animacao=1) 
        #sai do loop principal
        break 
    #detecta se houve pontuação e atribui 
    detectar_pontuacao(menina, dino)
    #imprime a pontuação total na tela
    imprimir_pontuacao(tela, fonte_pontuacao, menina)
    #atualiza tela
    pygame.display.flip()
    clock.tick(fps)

while True: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    #background estático
    background.atualizar()
    #anima morte da menina
    menina.atualizar()
    #imprime a mensagem de game over
    imprimir_game_over(tela, fonte_game_over)
    pygame.display.flip()






