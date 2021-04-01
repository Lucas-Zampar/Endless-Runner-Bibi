import pygame
from random import randint
from decimal import Decimal

from .Sprite import Sprite
from .Constantes import largura_tela


"""
Constantes Dino
"""
#posição inicial do Dino 
coordenada_retangular_dino_x = largura_tela + 50
coordenada_retangular_dino_y = 560
#caminhos relativo a dino
caminho_dino_sprites_caminhar = 'assets/dino/sprites/walk/Walk ({}).png'
caminho_dino_som_grunir = 'assets/dino/efeitos_sonoros/grunido.mp3'
#velocidade de animação do dino 
velocidade_animacao_dino = Decimal('0.1')
#velocidade horizontal do dino 
velocidade_horizontal_dino = -20
#canal de som dino
canal_sonoro_dino = 1

class Dino(Sprite):
    """
    A classe Dino herda de Sprite. Tem como objetivo controlar as animações e efeitos sonoros do inimigo dinossauro. 
    """

    def __init__(self, tela):
        
        self.sprites_caminhar = [pygame.image.load(caminho_dino_sprites_caminhar.format(_)).convert_alpha() for _ in range(1,11)] # lista com as dez sprites que compõem a animação do dino caminhando.
        
        super().__init__(tela=tela, x=coordenada_retangular_dino_x , y=coordenada_retangular_dino_y, 
        sprite_atual= self.sprites_caminhar[0], velocidade_animacao=velocidade_animacao_dino, 
        velocidade_horizontal=velocidade_horizontal_dino)       
        
        self.canal_sonoro = pygame.mixer.Channel(canal_sonoro_dino) #instancia um canal sonoro dedicado ao dino através do objeto retornado por pygame.mixer.Channel(canal), em que canal é o canal específico da classe.
        self.efeito_sonoro_grunir = pygame.mixer.Sound(caminho_dino_som_grunir) #instancia o efeito sonoro de grunir do dinossauro através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo do efeito sonoro presente em assets.
    
    def animar_caminhar(self):
        """
        Controla o deslocamento horizontal do dino. Caso a coordenada x do ponto inferior direito tenha se deslocado para além do limite da tela, 
        ela passa a valer um valor superior ao da largura da tela escolhido randomicamente, reposicionando, assim, o dino.
        """
        self.animar_sprite(self.sprites_caminhar)
        self.deslocar_horizontalmente()

        if self.coordenada_retangular_inferior_direita.x <= 0:
            self.coordenada_retangular.x = largura_tela + self.coeficiente_aparecimento()
        
        if self.index_sprite_atual >= len(self.sprites_caminhar):            
            self.index_sprite_atual=0 

    def tocar_efeito_sonoro_grunir(self):
        """
        Se o dino estiver prestes a aparecer, isto é, se a coordenada x atual mais a velocidade horizontal 
        seja menor do que a largura da tela, e efeito sonoro de grunir é ativado. 
        """
        if self.coordenada_retangular.x > largura_tela and self.coordenada_retangular.x + self.velocidade_horizontal <= largura_tela:
            self.canal_sonoro.play(self.efeito_sonoro_grunir)
            
    def coeficiente_aparecimento(self):
        """
        Estipula uma nova posição randômica para o dino. 
        """
        return randint(largura_tela//2, largura_tela) 
    
    def atualizar(self):
        self.animar_caminhar() 
        self.tocar_efeito_sonoro_grunir()
