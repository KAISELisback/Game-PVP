def validar(texto):
    
    while True:
        
        try:
            escolha = int(input(texto))
        except ValueError:
            print('O valor inserido não é um número. Tente novamente.')
            continue          
        if escolha == 1:       
            return True           
        elif escolha == 2:
            print('Espero vê-lo novamente em breve.')
            break        
        else:
            print('O valor inserido não é correspondente. Tente novamente.')   
            continue

def ver_regras():
    
    print("""
REGRAS BÁSICAS:

ARMAS:
    
    Cada jogador escolhe uma arma no ínicio do jogo
    Armas Disponíveis: Adaga, Espada, Machado, Alabarda e Clava
        
CONFRONTOS: 
    
    Os jogadores lutarão entre si em duelos automáticos
    O jogador com arma de maior dano vence o confronto
        
LOJA:
    
    Disponibiliza aprimoramentos que podem ser comprados com moedas
    Aprimoramentos disponíveis: Forja e Runas
    
FIM DE JOGO: 

    O primeiro a chegar á marca de 10 vitórias vence o jogo.

""")
    
def ver_arsenal():
    
    print("""
Arsenal de Armas

    [1] Adaga
    [2] Espada
    [3] Machado
    [4] Alabarda
    [5] Clava
    
    Possível dano base: 5-10
""")
    
def ver_loja():
    
    print(f"""
Loja de Aprimoramentos

[1] Forja
Custo: 40 Moedas

Descrição: Aumenta o dano base da arma
Aumento de dano: de 20 a 30

[2] Runas
Custo: 20 Moedas

Descrição: Recebe uma runa aleatória que garante dano bônus á arma
Dano bonûs: de 5 a 35

[3] Pular loja

Descrição: Pula a loja sem comprar nessa rodada
""")
    