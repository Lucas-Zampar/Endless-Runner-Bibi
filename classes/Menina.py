import pygame
from decimal import Decimal
from .Sprite import Sprite

"""
Constantes Menina
"""
#posição inicial menina
coordenada_retangular_menina_x = 50
coordenada_retangular_menina_y = 600
#velocidade de animacão da menina 
velocidade_animacao_menina = Decimal('0.1')
#velocidade vertical da menina 
velocidade_vertical_menina = 12
#Caminhos relativo a menina 
caminho_menina_sprites_correr = 'assets/menina/sprites/run/Run ({}).png'
caminho_menina_sprites_morrer = 'assets/menina/sprites/dead/Dead ({}).png'
caminho_menina_sprites_pular = 'assets/menina/sprites/jump/Jump ({}).png'
caminho_menina_efeito_sonoro_pular = 'assets/menina/efeitos_sonoros/pular.wav'
caminho_menina_efeito_sonoro_pousar = 'assets/menina/efeitos_sonoros/pousar.wav'
caminho_menina_efeito_sonoro_pontuar = 'assets/menina/efeitos_sonoros/pontuar.wav'
caminho_menina_efeito_sonoro_morrer = 'assets/menina/efeitos_sonoros/morrer.wav'
#canal de som menina 
canal_sonoro_menina = 2
#pontos que a menina ganha 
pontos_menina = 100

class Menina(Sprite):
    """
    A classe Menina herda Sprite. Tem como objetivo controlar as animações e efeitos sonoros da heroína menina. 
    """
    def __init__(self, tela, x=10, y=600):

        self.sprites_correr = [pygame.image.load(caminho_menina_sprites_correr.format(_)) for _ in range(1,9)] #lista com as oito sprites que compõem a animação do menina correndo.
        self.sprites_pular = [pygame.image.load(caminho_menina_sprites_pular.format(_))  for _ in range(1,11)] #lista com as dez sprites que compõem a animação da menina pulando.
        self.sprites_morrer = [pygame.image.load(caminho_menina_sprites_morrer.format(_)) for _ in range(1,11)] #lista com as dez sprites que compõem a animação da menina morrendo.
        
        super().__init__(tela=tela, x=coordenada_retangular_menina_x, y=coordenada_retangular_menina_y,
        sprite_atual= self.sprites_correr[0], velocidade_animacao=velocidade_animacao_menina, 
        velocidade_vertical=velocidade_vertical_menina)

        self.viva = True # define o estado da personagem quanto a viva (True) ou morta (False) por meio de um booleano. 
        self.pontos = 0 #quantidade de pontos adquiridos. 
        
        self.canal_sonoro = pygame.mixer.Channel(canal_sonoro_menina) #instancia um canal sonoro dedicado a menina através do objeto retornado por pygame.mixer.Channel(canal), em que canal é o canal específico da classe.
        self.efeito_sonoro_pular = pygame.mixer.Sound(caminho_menina_efeito_sonoro_pular) #instancia o efeito sonoro de pulo da menina através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo do efeito sonoro presente em assets.
        self.efeito_sonoro_pousar = pygame.mixer.Sound(caminho_menina_efeito_sonoro_pousar) #instancia o efeito sonoro de pouso da menina através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo do efeito sonoro presente em assets.
        self.efeito_sonoro_morrer = pygame.mixer.Sound(caminho_menina_efeito_sonoro_morrer) #instancia o efeito sonoro de morte da menina através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo do efeito sonoro presente em assets.
        self.efeito_sonoro_pontuar = pygame.mixer.Sound(caminho_menina_efeito_sonoro_pontuar) #instancia o efeito sonoro ao pontuar da menina através do objeto retornado por pygame.mixer.Sound(caminho) tocada durante a partida, em que caminho é o caminho relativo do efeito sonoro presente em assets.
            
    def animar_correr(self):
        """
        Controla o fluxo de animação de corrida da menina. Os sprites são exibidos consoante ao atributo velocidade\_animacao. 
        Quando todos tiverem sido exibidos, o ciclo recomeça. Não há deslocamento horizontal, 
        uma vez que o backgorund se desloca, o que dá a impressão de movimento horizontal por parte da menina. 
        """
        self.animar_sprite(self.sprites_correr)
        if self.index_sprite_atual >= len(self.sprites_correr): 
            self.index_sprite_atual = 0 
    def animar_pular(self):
        """
        Controla a animação de pulo da menina. Há deslocamento vertical. O sentido do deslocamento é controlado pela quantidade de spritas exibidos. 
        Se metade dos sprites já tiverem sido exibidos, o parâmetro sentido do método deslocamento\_vertical recebe -1, ou seja, ela passa a descer.
        """
        self.animar_sprite(self.sprites_pular)
        if self.index_sprite_atual < len(self.sprites_pular)/2:
            self.deslocar_verticalmente(sentido=-1)
        elif len(self.sprites_pular)/2 < self.index_sprite_atual < len(self.sprites_pular): 
            self.deslocar_verticalmente()
        if self.index_sprite_atual >= len(self.sprites_pular):
            self.mudar_animacao(index_sprite_atual=0, tipo_animacao=0)
    def animar_morrer(self):
        """
        Controla o fluxo de animação da morte da menina. Todos os sprites da respectiva lista são exibidos uma única vez, 
        não havendo recomeço. Após todos serem exibidos, o último sprite será exibido então continuamente na tela de game over. 
        """
        if self.index_sprite_atual < len(self.sprites_correr):
            self.animar_sprite(self.sprites_morrer)
        else:
            self.imprimir_sprite()

    def tocar_efeito_sonoro_pular(self):
        #toca o efeito sonoro de pulo.
        self.canal_sonoro.play(self.efeito_sonoro_pular)
    
    def tocar_efeito_sonoro_pousar(self):
        #toca o efeito sonoro de pouso.
        self.canal_sonoro.play(self.efeito_sonoro_pousar)
    
    def tocar_efeito_sonoro_pontuar(self):
        #toca o efeito sonoro de pontuação.
        self.canal_sonoro.play(self.efeito_sonoro_pontuar)
    
    def tocar_efeito_sonoro_morrer(self):
        #toca o efeito sonoro de morte.
        self.canal_sonoro.play(self.efeito_sonoro_morrer)

    def ganhar_pontos(self):
        #computa os pontos ganhos na partida. 
        self.pontos += pontos_menina
        self.canal_sonoro.play(self.efeito_sonoro_pontuar)
    
    def mudar_animacao(self, tipo_animacao, index_sprite_atual=0):
        """
        Altera a prepara o ambiente para e passagem entre animações. Caso seja 0, significa que a menina acabou de retornar de um salto, 
        então o efeito sonoro de pouso é tocado e a animação passa a ser definida como correr. Caso seja 1, a menina executará um salto, 
        logo o respectivo efeito sonoro é tocado e a animação passa a ser de salto.
        Por fim, caso seja 2, o efeito de morte é tocado, o atributo viva é alterado para False e o processo de finalização é iniciado. 
        """
        if tipo_animacao == 1: 
            self.tipo_animacao = tipo_animacao
            self.index_sprite_atual = index_sprite_atual
            self.tocar_efeito_sonoro_pular()
        elif tipo_animacao == 0: 
            self.tipo_animacao = tipo_animacao
            self.index_sprite_atual = index_sprite_atual
            self.tocar_efeito_sonoro_pousar()
        elif tipo_animacao == 2: 
            self.viva = False
            self.coordenada_retangular.x = coordenada_retangular_menina_x
            self.coordenada_retangular.y = coordenada_retangular_menina_y 
            self.tipo_animacao = tipo_animacao
            self.index_sprite_atual = index_sprite_atual
            self.tocar_efeito_sonoro_morrer()

    def atualizar(self):
        if self.viva: 
            if self.tipo_animacao == 0:
                self.animar_correr()
            if self.tipo_animacao == 1:
                self.animar_pular() 
        elif self.tipo_animacao == 2:
            self.animar_morrer() 