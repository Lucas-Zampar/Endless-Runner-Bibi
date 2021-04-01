import pygame
from decimal import Decimal
from .Constantes import altura_tela, largura_tela


class Ponto():
    """
    A classe Ponto define um ponto no espac ̧o a partir das coordenadas retangulares x e y.
    """
    def __init__(self, x, y):
        self.x = x #referente a coordenada retangular x, no caso, o índice da coluna do pixel na tela.
        self.y = y #referente a coordenada retangular y, no caso, o índice da linha do pixel na tela.
    
    def __str__(self):
        """
        Reescrita do método \_\_str\_\_ herdado de object, retorna uma string que representa o ponto com a notação matemática (x,y)
        """
        return '({},{})'.format(self.x, self.y)

class Sprite(): 
    def __init__(self, tela, x, y, sprite_atual, velocidade_animacao=0, velocidade_horizontal=0, velocidade_vertical=0):     
       
        self.coordenada_retangular = Ponto(x, y)  #recebe uma instância da classe Ponto() que guarda as coordenadas do ponto superior esquerdo, utilizado como referencial, do sprite exibido no frame corrente. 
        self.tela = tela #recebe o objeto, fornecido por pygame.display.set\_mode(), referente a tela onde o sprite será impresso. 
        
        self.velocidade_animacao = velocidade_animacao #recebe uma instância da classe Decimal(), empregado como controle da velocidade de animação dos sprites. Utiliza-se a classe Decimal a fim de garantir precisão na soma de pontos flutuantes.
        self.velocidade_horizontal = velocidade_horizontal #define a velocidade de deslocamento horizontal do sprite, representada por um inteiro.
        self.velocidade_vertical = velocidade_vertical  #define a velocidade de movimento vertical do sprite
        self.__sprite_atual = sprite_atual #define a velocidade de deslocamento vertical do sprite, representada por um inteiro. #recebe o objeto após aplicar pygame.image.load(caminho).convert(), em que o caminho é o caminho relativo do sprite em questão no diretório assets. Por se tratar de um setter, ao ser atribuída, executa outras operações. 
        
        self.index_sprite_atual = 0 #define o índice atual em uma lista de sprites.
        self.tipo_animacao = 0 #define o tipo de animação executada pelo sprite corrente.
    
    @property
    def sprite_atual(self):
        return self.__sprite_atual
    
    @sprite_atual.setter
    def sprite_atual(self, sprite_atual):
        self.largura_sprite_atual = self.sprite_atual.get_rect().width #guarda a largura do retângulo do sprite atual. É atribuída toda vez que um sprite mudar sua imagem no frame corrente.
        self.altura_sprite_atual = self.sprite_atual.get_rect().height #guarda a altura do retângulo do sprite atual. É atribuída toda vez que um sprite mudar sua imagem no frame corrente. 
        self.__sprite_atual = sprite_atual 
    

    def deslocar_horizontalmente(self, sentido=1):
        """
        Realiza o deslocamento horizontal do sprite no sentido passado como parâmetro, por padrão 1, ou seja, 
        a soma da cooredenada retangular x com o produto entre o sentido e a velocidade horizontal. O sentido pode assumir os valores inteiros 1 ou -1.
        """
        self.coordenada_retangular.x = self.coordenada_retangular.x + sentido*self.velocidade_horizontal
    
    def deslocar_verticalmente(self, sentido=1):
        """
        Realiza o deslocamento vertical do sprite no sentido passado como parâmetro, por padrão 1, ou seja, 
        a soma da cooredenada retangular y com o produto entre o sentido e a velocidade vetical. O sentido pode assumir os valores inteiros 1 ou -1.
        """
        self.coordenada_retangular.y = self.coordenada_retangular.y + sentido*self.velocidade_vertical 
    
    def imprimir_sprite(self):
        """
        Encapsula o método blit do objeto tela a fim de exibir o sprite atual do frame. 
        """
        self.tela.blit(self.sprite_atual, (self.coordenada_retangular.x, self.coordenada_retangular.y))   
    
    def animar_sprite(self, lista_sprites):
        """
        Imprime na tela o sprite atual pertencente a lista de sprites passada como parâmetro. 
        Os sprites são exibidos consoante ao valor do atributo velocidade\_animacao que incrementa index\_sprite\_atual.
        """
        if self.index_sprite_atual % 1  == Decimal('0.0'):    
            self.sprite_atual = lista_sprites[int(self.index_sprite_atual)] 
        self.index_sprite_atual = self.index_sprite_atual + self.velocidade_animacao
        self.imprimir_sprite()
    
    @property
    def coordenada_retangular_inferior_direita(self):  
        #propriedade que devolve uma instância da classe Ponto() contendo as coordenadas do ponto inferior direito do sprite atual.
        return Ponto(self.coordenada_retangular.x + self.largura_sprite_atual, self.coordenada_retangular.y + self.altura_sprite_atual)
    
    @property
    def coordenada_retangular_inferior_esquerda(self):
        #propriedade que devolve uma instância da classe Ponto() contendo as coordenadas do ponto inferior esquerdo do sprite atual.
        return Ponto(self.coordenada_retangular.x, self.coordenada_retangular.y + self.altura_sprite_atual)
    @property
    def coordenada_retangular_superior_direita(self):
        #propriedade que devolve uma instância da classe Ponto() contendo as coordenadas do ponto superior direito do sprite atual.
        return Ponto(self.coordenada_retangular.x + self.largura_sprite_atual, self.coordenada_retangular.y)
   

    def atualizar(self):
        '''
        O seguinte método deve ser implementado por cada classe que herda Spite
        a fim de atualizar as sprites
        '''
        pass







        




