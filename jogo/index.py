import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações iniciais
largura= 640
altura = 480
tamanho_bloco = 20
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Função para desenhar a cobra
def desenhar_cobra(cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, cor_cobra, segmento)

# Função principal do jogo
def jogo():
    cobra = [(100, 50)]
    cobra_direcao = (1, 0)
    comida = (random.randint(0, largura // tamanho_bloco - 1) * tamanho_bloco, random.randint(0, altura // tamanho_bloco - 1) * tamanho_bloco)
    pontuacao = 0

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and cobra_direcao != (0, 1):
                    cobra_direcao = (0, -1)
                elif evento.key == pygame.K_DOWN and cobra_direcao != (0, -1):
                    cobra_direcao = (0, 1)
                elif evento.key == pygame.K_LEFT and cobra_direcao != (1, 0):
                    cobra_direcao = (-1, 0)
                elif evento.key == pygame.K_RIGHT and cobra_direcao != (-1, 0):
                    cobra_direcao = (1, 0)

        cobra_cabeca = (cobra[0][0] + cobra_direcao[0] * tamanho_bloco, cobra[0][1] + cobra_direcao[1] * tamanho_bloco)
        cobra.insert(0, cobra_cabeca)

        if cobra_cabeca == comida:
            pontuacao += 1
            comida = (random.randint(0, largura // tamanho_bloco - 1) * tamanho_bloco, random.randint(0, altura // tamanho_bloco - 1) * tamanho_bloco)
        else:
            cobra.pop()

        tela.fill(cor_fundo)
        desenhar_cobra(cobra)
        pygame.draw.rect(tela, cor_comida, comida)
        pygame.display.update()

        if cobra_cabeca[0] < 0 or cobra_cabeca[0] >= largura or cobra_cabeca[1] < 0 or cobra_cabeca[1] >= altura or cobra_cabeca in cobra[1:]:
            fonte = pygame.font.Font(None, 36)
            mensagem = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
            tela.blit(mensagem, (largura // 2 - 100, altura // 2 - 18))
            pygame.display.update()
            pygame.time.delay(2000)
            return

        clock.tick(10)

# Execução do jogo
if __name__ == '__main__':
    jogo()
