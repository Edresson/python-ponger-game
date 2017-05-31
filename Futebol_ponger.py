import random, math, pygame,time
from pygame.locals import *
import pygame.mixer

run = 1

class Bola(object):

    def __init__(self):
        self.Bolaxy = [200,200]
        
        self.Bolaspeed = 2
        self.Bolady = 1
        self.Boladx = 1
        self.BolaRolando = self.TRUE
        self.service = self.Esquerda
        self.BolaVerificar = 0 # Adicionado para resolver o problemas com Atleta da direita passar do limite da tela
        
        
    def Carregar(self):

        self.Tela.blit(self.BolaModel,self.Bolaxy)# Dando Blit no Modelo Da Bola para ela aparecer na Surface(superficie) de nossa Tela.


    def Mover_Bola(self):
		
        if self.BolaRolando is not self.TRUE:
            
            
                # Se a Bola bater no atleta da esquerda mover a Bola.
            if self.Bolaxy[0] <(self.AtletaEsquerdaxy[0] + 20) and self.Bolaxy[1] > (self.AtletaEsquerdaxy[1] - 18) and self.Bolaxy[1] < (self.AtletaEsquerdaxy[1] + 98):
                self.Boladx = -self.Boladx
                if self.Precionou_Tecla[K_w] or self.Precionou_Tecla[K_s]:
                    self.Bolady = random.randrange(2,4)
                else:
                    self.Bolady = random.randrange(0,3)
                        
            # Se a Bola bater no atleta da Direita Mover a Bola.
            elif self.Bolaxy[0] > (self.AtletaDireitaxy[0] - 20) and self.Bolaxy[1] > (self.AtletaDireitaxy[1] - 18) and self.Bolaxy[1] <= (self.AtletaDireitaxy[1] + 98):
                # Adicionado para corrigir o Problema da Bola sair da Tela e não voltar mais ( não foi necessario colocar no atleta esquerda pois não teve este problema com ele)
                
                if self.BolaVerificar == 0:
                    self.Boladx = -self.Boladx
                    if self.Precionou_Tecla[K_UP] or self.Precionou_Tecla[K_DOWN]:
                        self.Bolady = random.randrange(2,4)
                    else:
                        self.Bolady = random.randrange(0,3)
                    self.BolaVerificar = 1
                else:
                    self.BolaVerificar = self.BolaVerificar + 1
                    if self.BolaVerificar == 4:
                        self.BolaVerificar = 0
                            
            #Se a Bola chegar ao topo da tela fazer ela descer
            elif self.Bolaxy[1] <= self.MinimoY:
                self.Bolady = -self.Bolady
            #Se a bola chegar ao final(baixo) da Tela Fazer ela subir
            elif self.Bolaxy[1] >= self.MaximoY:
                self.Bolady = -self.Bolady
            #Se o Atleta fazer o gol na trave esquerda 
            elif self.Bolaxy[0] <= self.MinimoX:
                self.BolaRolando = self.TRUE
                self.service = self.Direita
                self.PontosDireita = self.PontosDireita + 1
                self.songol()
                # Limpa os pontos do atleta Direita para setar os novos
                pygame.draw.rect(self.Tela,self.Preto,self.textDireita)
            #Se o Atleta fazer o gol na trave Direita 
            elif self.Bolaxy[0] >= self.MaximoX:
                self.BolaRolando = self.TRUE
                self.service = self.Esquerda
                self.PontosEsquerda = self.PontosEsquerda + 1
                self.songol()
                # Limpa os Pontos do atleta Esquerdo para setar os novos.
                pygame.draw.rect(self.Tela,self.Preto,self.textEsquerda)
                    
            # Move Literalmente a Bola utilizando o valor de BOLADX e BOLADY gravado acima.
            self.Bolaxy[0] = self.Bolaxy[0] + (self.Bolaspeed * self.Boladx)
            self.Bolaxy[1] = self.Bolaxy[1] + (self.Bolaspeed * self.Bolady)

        # Configurar a bola para o outro Atleta:
        else:
            
            if self.service == self.Esquerda:
                self.Bolaxy[0] = self.AtletaEsquerdaxy[0] + 25
                self.Bolaxy[1] = self.AtletaEsquerdaxy[1] + 40
            elif self.service == self.Direita:
                self.Bolaxy[0] = self.AtletaDireitaxy[0] - 25
                self.Bolaxy[1] = self.AtletaDireitaxy[1] + 40

class Atleta(object):
    def __init__(self):
        self.Atleta_Passo = 20
        self.EsquerdaVal = 25 
        self.DireitaVal = 775
        self.Esquerda = 1
        self.Direita = 0
        self.AtletaPasso = 4

        self.AtletaEsquerdaxy = [5,200]
        self.AtletaDireitaxy = [775,200]

        
    def Mover_Atletas(self):
        
        
        for event in pygame.event.get():#pygame.event.get() """Obtendo os atuais Eventos"""
            
            
            if event.type == QUIT:# Se o Evento for o Quit( o de fechar o programa) Fechar o Jogo. Exit() Fecha a Janela atual e finaliza o Jogo
                exit()
                    
        self.Precionou_Tecla = pygame.key.get_pressed()#Metodo da pygame responsavel por obter a tecla precessionada pelo Jogador(usuario do Programa).

        
         # Verificando precionamento da Tecla W se for precionado mover o atleta da Esquerda para cima
        if self.Precionou_Tecla[K_w]:
                
                
            if self.AtletaEsquerdaxy[1] > self.MinimoY:
                    
                self.AtletaEsquerdaxy[1] = self.AtletaEsquerdaxy[1] - self.AtletaPasso
                   
                    
		# Verificando precionamento da Tecla S se for precionado mover o atleta da  Esquerda para baixo.
        elif self.Precionou_Tecla[K_s]:
            if self.AtletaEsquerdaxy[1] < self.MaximoY - 80:
                self.AtletaEsquerdaxy[1] = self.AtletaEsquerdaxy[1] + self.AtletaPasso

        # Verificando precionamento da Tecla UP (Seta para cima) se for precionado mover o atleta Esquerdo para cima.            
        if self.Precionou_Tecla[K_UP]:
            if self.AtletaDireitaxy[1] > self.MinimoY:
                self.AtletaDireitaxy[1] = self.AtletaDireitaxy[1] - self.AtletaPasso
		# Verificando precionamento da Tecla DOWN(seta para Baixo) se for precionado mover o atleta Esquerdo para baixo.
        elif self.Precionou_Tecla[K_DOWN]:
            if self.AtletaDireitaxy[1] < self.MaximoY - 80:
                self.AtletaDireitaxy[1] = self.AtletaDireitaxy[1] + self.AtletaPasso

        # Verificando precionamento da Tecla e  ou Enter  se for precionado mover o atleta Esquerdo para cima
        if (self.Precionou_Tecla[K_e] or self.Precionou_Tecla[K_RETURN]) and self.BolaRolando == self.TRUE:
            self.BolaRolando = self.FALSE
            if self.service == self.Esquerda:
                # Utilizado RandRange para obter um valor aleatorio assim mudando a direção da bola.
                self.Boladx = random.randrange(2,3)
                self.Bolady = random.randrange(-3,3)
                self.service = self.Direita
            else:
                # Utilizado RandRange para obter um valor aleatorio assim mudando a direção da bola.
                self.Boladx = random.randrange(2,3)
                self.Bolady = random.randrange(-3,3)
                self.service == self.Esquerda
                
                
        if self.Precionou_Tecla[K_q]:#Se precionar a tela Q fechar o Jogo.
            run = 0
            exit()

        if self.Precionou_Tecla[K_p]:# Se precionar a tecla P pausar o jogo
            self.gamepaused = self.TRUE 
            self.font = pygame.font.SysFont("arial", 64)
            self.paused_surface = self.font.render("PAUSADO", True, self.Azul)
            self.paused_rect = self.Tela.blit(self.paused_surface, (260,250))
            self.font = pygame.font.SysFont("arial", 15)
            self.paused_surface = self.font.render("Precione R para retomar", True, self.Vermelho)
            self.paused_rect = self.Tela.blit(self.paused_surface, (300,350))
            pygame.display.update() # atualizando a Tela.

            while self.gamepaused == self.TRUE: # enquanto o jogo estiver pausado faça.

                for event in pygame.event.get():# Verifica se o evento Atual é de saida(QUIT) se for fecha o Jogo.
                    if event.type == QUIT:
                        exit()
                    
                self.Precionou_Tecla = pygame.key.get_pressed()

                if self.Precionou_Tecla[K_r]:# Se precionar R Retormar ao Jogo
                    self.gamepaused = self.FALSE
                self.clock.tick(20)# Limitando a quantidade de FPS(Frames por segundo)para 20, visa minimizar o Uso de CPU do jogo enquanto o mesmo estiver Pausado.

            pygame.draw.rect(self.Tela,self.Preto,self.paused_rect) # Desenhando uma forma retangular na superfície TELA (isso desenha a caisa do pause com a cor Preta , e mostra o texto "PAUSADO" Dentro dele).
    
    

    
class Tela(object):
    def __init__(self):
        self.ResolucaoTela = [800,600]
        self.Branco = [255,255,255]
        self.Preto = [0,0,0]
        self.Vermelho = [255,0,0]
        self.Verde = [0,255,0]
        self.Azul = [0,0,255]
        self.Tamanho_Atleta = [20,20]
        self.MaximoX = 780
        self.MinimoX = 20
        self.MaximoY = 580
        self.MinimoY = 0
        self.PontosEsquerda = 0
        self.PontosDireita = 0
        self.PontosEsquerda = 0
        self.PontosDireita = 0
        #Text ou TextDrawn refere-se ao Texto na tela que marca os pontos referente a cada time(atleta), a variavel traz a posição da tela onde irá ficar
        self.textDireita = [3,3,4,4]
        #Text ou TextDrawn refere-se ao Texto na tela que marca os pontos referente a cada time(atleta) a variavel traz a posição da tela onde irá ficar
        self.textEsquerda = [1,1,2,2]
        pygame.init() #Inicializando todos os módulos importados importados de pygame.
        
        
        self.Tela = pygame.display.set_mode(self.ResolucaoTela)# Inicializando a  janela com a resolução especificada pelo atributo ResolucaoTela.
        pygame.display.set_caption('Futebol_Ponger') # Setando o Titulo Da Janela ( ou seja nome do jogo)
        self.Tela.fill(self.Preto) # Setando a Cor de Fundo da Pagina.
        self.BolaModel = pygame.image.load('BolaModel.bmp').convert() # Carregando a Imagem do Modelo, a necessidade é a mesma descrita acima no carregamento domodelo do atleta.
        self.Bola = pygame.image.load('Bola.bmp').convert()# Carregando a Imagem Da bola
        self.Atleta = pygame.image.load('Atleta1.bmp').convert() # Carregando a Imagem do Atleta1.
        self.Atleta2 = pygame.image.load('Atleta2.bmp').convert() # Carregando a Imagem do Atleta2.
        self.AtletaModel = pygame.image.load('AtletaModel.bmp').convert() # Carregando a Imagem do  Modelo do Atleta, ou seja, ao mover o Atleta é necessário colocar algo onde
        # ele estava anteriormente(Apagar a imagem deixa por ele),está imagem é do tamanho do atleta porém toda Preta(obs: se mudar a cor de fundo será necessário mudar a cor desta imagem)
        
    def Mensagem_Entrada(self):
        
        self.font = pygame.font.SysFont("arial", 20) # declarando variavel responsavel pela fonte e tamanho da Letra da mensagem de entrada.
        self.Texto_Tela = self.font.render("Futebol_Ponger", True, self.Verde) # Escrevendo o titulo na pagina, o metodo render cria uma nova imagem da Escrita.
        self.Tela.blit(self.Texto_Tela, (80,40)) # Dando Blit no texto para ela aparecer na Surface de nossa Tela.(80,40)"""Especifica o local da tela que será colocado o Texto(Imagem)""" 
        self.Texto_Tela = self.font.render("Dicas:", True, self.Azul)
        self.Tela.blit(self.Texto_Tela, (80,80)) # Dando Blit no texto para ela aparecer na Surface de nossa Tela. 
        self.Texto_Tela = self.font.render("Para mover o Atleta da Esquerda  use as teclas W e S", True, self.Azul)
        self.Tela.blit(self.Texto_Tela, (80,120))
        self.Texto_Tela = self.font.render("Para Mover o Atleta da Direita use as Teclas UP e DOWN ", True, self.Azul)
        self.Tela.blit(self.Texto_Tela, (80,160))
        self.Texto_Tela = self.font.render("E e Enter chuta a Bola", True, self.Azul)
        self.Tela.blit(self.Texto_Tela, (80,200))
        self.Texto_Tela = self.font.render("P Para Pausar , R para retornar ao Jogo e  Q para sair do jogo", True, self.Azul)
        self.Tela.blit(self.Texto_Tela, (80,240))
        self.Texto_Tela = self.font.render("Presione I para iniciar o Jogo", True, self.Vermelho)
        self.Tela.blit(self.Texto_Tela, (80,280))
        pygame.display.update() # Atualizando a Tela do Jogo
        Futebol_Ponger.Checar_Precionamento_tecla(self) #Chamando o Metodo de checagem de precionamento de tecla.


    def Preparar_Tela_Mostrar_Pontos(self):
        
        self.Tela.blit(self.AtletaModel,self.AtletaEsquerdaxy)# Dando Blit no Modelo do atleta(da esquerda)  para ela aparecer na Surface(superficie) de nossa Tela.
        self.Tela.blit(self.AtletaModel,self.AtletaDireitaxy)# Dando Blit no Modelo do atleta(da Direita) para ela aparecer na Surface(superficie) de nossa Tela.
        Bola.Carregar(self)
        self.font = pygame.font.SysFont("arial", 64) # Atribuindo a variavel font a fonte e o tamanho da Letra do Texto que mostra os pontos do Jogador.
        # Renderizando e Colocando TextDraw responsavel por mostrar pontuação dos Atletas (Placar).
        self.Texto_Tela1 = self.font.render(str(self.PontosEsquerda), True, self.Vermelho)
        self.textEsquerda = self.Tela.blit(self.Texto_Tela1, (40,40))
        self.Texto_Tela1 = self.font.render(str(self.PontosDireita), True, self.Azul)
        self.textDireita = self.Tela.blit(self.Texto_Tela1, (700,40))
    

    def Atualizar_Tela(self):# Seta os Atletas e a Bola para os devidos locais pegando os valores já calculados(Armazenados) nos metodos anteriores.
        
        self.Tela.blit(self.Atleta,self.AtletaEsquerdaxy)
        self.Tela.blit(self.Atleta2,self.AtletaDireitaxy)
        self.Tela.blit(self.Bola,self.Bolaxy)
        pygame.display.update()# Atualiza a Superficie de Nossa TELA

          
        self.clock.tick(100) # Limitando a quantidade de FPS(Frames por segundo)para 100 (durante o jogo é necessário uma maior quantidade de FPS).

        
class Futebol_Ponger():
    def __init__(self):
        
        self.TRUE = 1
        self.gameover = self.TRUE
        self.FALSE = 0
        
        Tela.__init__(self)
        Atleta.__init__(self) # Chamando construtor da classe Atleta.
        Bola.__init__(self)# Chamando construtor da classe Bola.
        self.tempo =time.time() # Armazenando 
        
        self.clock = pygame.time.Clock() #Criando um objeto Clock que vai ser usado   para controlar o FPS  do jogo.

        #SoM do jogo
        self.torcida = pygame.mixer.Sound("torcida.wav")
        self.gol = pygame.mixer.Sound("soUMgol.wav")

        
    def Mensagem_Inicial(self):

        Tela.Mensagem_Entrada(self)

        
    def Checar_Precionamento_tecla(self):
		

        for event in pygame.event.get():#pygame.event.get() """Obtendo os atuais Eventos"""
            if event.type == QUIT:#Se o Evento for o Quit( o de fechar o programa) Fechar o Jogo. Exit() Fecha a Janela atual e finaliza o Jogo
                exit()
                    
        self.Precionou_Tecla = pygame.key.get_pressed()#Metodo da pygame responsavel por obter a tecla precessionada pelo Jogador(usuario do Programa).
            
        if self.Precionou_Tecla[K_i]:# se o jogador precionar a tecla I então inicie o Jogo
            self.gameover = self.FALSE
            self.Tela.fill(self.Preto)# se o jogador precionar a tecla Q saia do jogo(feche o jogo).
        elif self.Precionou_Tecla[K_q]:
            run = 0
            exit()

        self.clock.tick(20)# Limitando a quantidade de FPS(Frames por segundo)para 20 , visa minimizar o Uso de CPU do jogo. 
   

    def sontorcida(self):
        self.torcida.play()

    def songol(self):
        self.gol.play()
            
    def Fechar(self):
        self.torcida.stop()
        self.font = pygame.font.SysFont("arial", 64)
        self.Placar_surface = self.font.render("FIM DE JOGO", True, self.Azul)
        self.Placar_rect = self.Tela.blit(self.Placar_surface, (200,250))
        self.font = pygame.font.SysFont("arial", 15)

        self.Texto_Tela1 = self.font.render(("Time Vermelho  "+ str(self.PontosEsquerda)+" X "), True, self.Vermelho)
        self.Placar_rect1 = self.Tela.blit(self.Texto_Tela1, (230,350))
        self.Texto_Tela1 = self.font.render((str(self.PontosDireita)+" Time Azul"), True, self.Azul)
        self.Placar_rect2 = self.Tela.blit(self.Texto_Tela1, (392,350))

                                              
        pygame.display.update() # atualizando a Tela.
        self.tempo = time.time()
        
        while(True):
            if(time.time()-self.tempo >=15):
                exit()
        
    def Iniciar(self):
        
            #Ajusta a Tela para ter Tela clara em Atletas ,bola e imprimir pontuação
            Tela.Preparar_Tela_Mostrar_Pontos(self)
            # Move os atletas checando se os atletas precionaram as Teclas.
            Atleta.Mover_Atletas(self)
                


            # Mover o Bola se a Mesma não estiver parada com um atleta
            Bola.Mover_Bola(self)
        
            
            
            #Atualizar a Tela
            Tela.Atualizar_Tela(self)
            


    
def main():
    
    while run == 1: 
        F = Futebol_Ponger() # Cria uma instancia da Classe Futebol_Ponger

        
        
        while F.gameover == F.TRUE:# Enquanto o  jogo ainda não inicio mostrar a mensagem de entrada
            
            #Mensagem ao INiciar Tela
            F.Mensagem_Inicial()
        

        F.sontorcida()
        F.tempo =time.time()
        minutos =0
        # Enquanto o jogo estiver rodando
        while F.gameover == F.FALSE:
            
            print(time.time()-F.tempo )
            if(time.time()-F.tempo >= 60):
                F.sontorcida()
                minutos = minutos+1
                F.tempo = time.time()
                if(minutos == 5):
                    F.Fechar()
            
            F.Iniciar()
            
            
        

if __name__ == '__main__':
    main()
    
