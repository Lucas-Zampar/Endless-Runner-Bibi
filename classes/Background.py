import pygame
from .Sprite import Sprite
from .Constantes import altura_tela, largura_tela

"""
Constantes background
"""
#posição inicial da imagem de background
coordenada_retangular_x_background = 0
coordenada_retangular_y_background = 0
#velocidade horizontal
velocidade_horizontal_background = -2 
#caminhos background
caminho_background_imagem = 'assets/background/background.png'
caminho_background_musica_tema = 'assets/background/musica_tema.ogg'
caminho_background_musica_encerramento = 'assets/background/piano_triste.mp3'
#canal sonoro background 
canal_sonoro_background = 0

class Background(Sprite):
    """
    A classe Background herda Sprite. Tem com objetivo controlar o deslocamento 
    da imagem de background, bem com das músicas temas do jogo. 
    """
    
    def __init__(self, tela):
        super().__init__(tela=tela, x=coordenada_retangular_x_background, y=coordenada_retangular_y_background, 
        velocidade_horizontal= velocidade_horizontal_background, sprite_atual= pygame.image.load(caminho_background_imagem).convert())
        
        self.canal_sonoro = pygame.mixer.Channel(canal_sonoro_background) #instancia um canal sonoro dedicado ao background através do objeto retornado por pygame.mixer.Channel(canal), em que canal é o canal específico da classe. 
        self.musica_tema = pygame.mixer.Sound(caminho_background_musica_tema) #instancia a música tema do jogo através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo da música presente em assets.
        self.musica_encerramento = pygame.mixer.Sound(caminho_background_musica_encerramento) #instancia a música de encerramento do jogo através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo da música presente em assets.
        self.canal_sonoro.play(self.musica_tema, loops= -1) #toca infinitamente a música tema do jogo
        print(type(self.canal_sonoro))
        print(type(self.musica_encerramento))
    def animar_deslocamento_horizontal(self):
        """
        Controla o deslocamento horizontal do sprite. Caso a coordenada retangular x tenha alcançado 
        o valor igual ou menor a menos a largura da tela de exibição, a coordenada de x é reiniciada para 0, garantindo, assim, o deslocamento infinito.
        """
        if -self.coordenada_retangular.x <= largura_tela:
            self.deslocar_horizontalmente()
        else:
            self.coordenada_retangular.x = 0         
        self.imprimir_sprite() 
    
    def mudar_animacao(self, tipo_animacao, index_sprite_atual=0):
        """
        Altera a animação do sprite. No caso desta classe, quando a menina morrer,
        a animação passará de 0 (background em movimento tocando música tema) para 1 (background estático tocando música de encerramento melancólica).
        """
        self.tipo_animacao = tipo_animacao
        self.index_sprite_atual = index_sprite_atual
        self.tocar_musica_encerramento() 

    def tocar_musica_encerramento(self):
        """
        Toca a música de encerramento melancólica. 
        """
        self.canal_sonoro.play(self.musica_encerramento)

    def atualizar(self): 
        if self.tipo_animacao == 0:
            self.animar_deslocamento_horizontal()
        else:    
            self.imprimir_sprite() 

















