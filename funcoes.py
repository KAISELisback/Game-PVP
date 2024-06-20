from classes import Jogador, Arma, Runas
from utilitarios import validar, ver_regras, ver_arsenal, ver_loja
import random as r
import time as t

def regras():

    while True:
        
        try:
                escolha = int(input("""
Deseja visualizar as regras do jogo?

    [1] Ver regras
    [2] Avançar         
                
    -> """))               
        except ValueError:
            print('O valor inserido não é um número. Tente novamente.')
            continue            
        if escolha == 1:
            ver_regras()             
            try:
                avancar = int(input('    [2] Avançar\n   => '))                
            except ValueError:
                print('O valor inserido não é um número. Tente novamente.')
                continue                       
            if avancar == 2:
                return True            
            else:
                print('O valor inserido não é correspondente. Tente novamente.')
                continue               
        elif escolha == 2:
            return True                
        else:
            print('O valor inserido não é correspondente. Tente novamente.')
            continue 
                             
def nomear():
    
    global jogador1, jogador2
    
    nome_jogador1 = input(f'\nJogador 1, digite o seu nome:\n\n    => ')
    jogador1 = Jogador()
    jogador1.nome = nome_jogador1
    
    nome_jogador2 = input(f'\nJogador 2, digite o seu nome:\n\n    => ')
    jogador2 = Jogador()
    jogador2.nome = nome_jogador2
        
def definir_arma():  
    global arma_jogador1, arma_jogador2
    opcoes_armas = (1, 2, 3, 4, 5)

    while True:
        
        ver_arsenal()
        
        try:
            escolha_j1 = int(input(f'    {jogador1.nome}, escolha a sua arma\n\n    => '))
        except ValueError:
            print('O valor inserido não é um número. Tente novamente.')
            continue   
        if escolha_j1 in opcoes_armas:
            arma_jogador1 = Arma()
            arma_jogador1.declarar_arma(escolha_j1)
            print(f'\n    {jogador1.nome} escolheu {arma_jogador1.tipo}.' )
        else: 
            print('O valor inserido não é correspondente. Tente novamente.')
            continue
        
        
        try:
            escolha_j2 = int(input(f'\n    {jogador2.nome}, escolha a sua arma\n\n    => '))
        except ValueError:
            print('O valor inserido não é um número. Tente novamente.')
            continue        
        if  escolha_j2 in opcoes_armas:
            arma_jogador2 = Arma()
            arma_jogador2.declarar_arma(escolha_j2)
            print(f'\n    {jogador2.nome} escolheu {arma_jogador2.tipo}.' )
        else:
            print('O valor inserido não é correspondente. Tente novamente.')
            continue       
        print('\nOs jogadores já estão prontos, o dano das armas serão revelados durante o confronto.')
        t.sleep(1.5)
        return True

def identificar_runa():
        
    global runa_jogador1, runa_jogador2
    runa_jogador1 = Runas()
    runa_jogador2 = Runas()

def confronto():
    
    expressoes_de_efeito = [
    'destruidor', 'colossal', 'brutal', 'avassalador', 'furioso', 'vital',
    'implacável', 'impiedoso', 'aniquilador', 'descomunal', 'desvastador',
    ]

    if (arma_jogador1.dano + runa_jogador1.dano) > (arma_jogador2.dano + runa_jogador2.dano):
        vencedor = jogador1
        perdedor = jogador2
    elif (arma_jogador2.dano + runa_jogador2.dano) > (arma_jogador1.dano + runa_jogador1.dano):
        vencedor = jogador2
        perdedor = jogador1
    else:
         vencedor = 'empate'
        
    print('\nIniciando batalha automática...')
    t.sleep(2)
    if vencedor == jogador1 or vencedor == jogador2:
        print(f"""
    {jogador1.nome} desferiu um golpe {r.choice(expressoes_de_efeito)} contra {jogador2.nome}.""")
        t.sleep(2)
        print(f"""    {arma_jogador1.tipo} de {jogador1.nome} causou {(arma_jogador1.dano + runa_jogador1.dano)} de dano.
""")
        t.sleep(2)
        print(f"""
    {jogador2.nome} desferiu um golpe {r.choice(expressoes_de_efeito)} contra {jogador1.nome}.""")
        t.sleep(2)
        print(f"""    {arma_jogador2.tipo} de {jogador2.nome} causou {(arma_jogador2.dano + runa_jogador2.dano)} de dano.
""")
        t.sleep(2)
        print(f"""
    {vencedor.nome} venceu o confronto!            
""")
        t.sleep(1.5)
        print(f"""
Recompensas:

    {vencedor.nome} recebeu 30 moedas
    {perdedor.nome} recebeu 20 moedas
    """)
        vencedor.vitorias += 1
        vencedor.moedas += 30
        perdedor.moedas += 20
        t.sleep(2)
        print(f"""
finalizando batalha automática...            
""")
        t.sleep(2)
    else:
        print(f'\n    As armas de {jogador1.nome} e {jogador2.nome} estão ressonando entre si\n')
        t.sleep(2)
        print(f'    O mesmo tipo de poder foi detectado\n')
        t.sleep(2)
        print(f'    Empate! Os jogadores avançarão iguais nessa rodada\n')
        jogador1.moedas += 20
        jogador2.moedas += 20
        t.sleep(2)
        print(f'    {jogador1.nome} e {jogador2.nome} receberam 20 moedas!\n')
        t.sleep(2)
    
    if jogador1.vitorias == 10 or jogador2.vitorias == 10:
        print(f"""
FIM DE JOGO!

    {vencedor.nome} derrotou {perdedor.nome} após muitos confrontos épicos
    e se tornou um lenda viva.

    Um novo posto governante foi alcançado e agora {vencedor.nome} lidera o mundo!
""")
        return False
    else:
        return True
  
def status():
    
    print(f"""
Informações dos Jogadores
    
Jogador: {jogador1.nome}

    {arma_jogador1.tipo}: {arma_jogador1.dano} de dano
    {runa_jogador1.tipo}: {runa_jogador1.dano} de dano
    Moedas: {jogador1.moedas}
    Vitórias: {jogador1.vitorias}
    
Jogador: {jogador2.nome}

    {arma_jogador2.tipo}: {arma_jogador2.dano} de dano
    {runa_jogador2.tipo}: {runa_jogador2.dano} de dano
    Moedas: {jogador2.moedas}
    Vitórias: {jogador2.vitorias}
""")

def loja():
    
    while True:
        
        ver_loja()
        try:
            escolha1 = int(input(f'    {jogador1.nome}, escolha:\n    Moedas: {jogador1.moedas}\n    => '))
        except ValueError:
            print('O valor inserido não é um número. Tente novamente.')
            continue
        if escolha1 == 1:
            if jogador1.moedas >= 40:
                backup_moedas = jogador1.moedas
                backup_dano_arma = arma_jogador1.dano
                jogador1.moedas -= 40
                arma_jogador1.forjar()
                print(f"""
{jogador1.nome}:

    Ferreiro aprimorou {arma_jogador1.tipo}!
    Dano: ???(Lute para revelar)
    Moedas restantes: {jogador1.moedas}
""")
            else:
                print("""
Moedas insuficientes.
""")
        elif escolha1 == 2:
            if jogador1.moedas >= 20:
                backup_moedas = jogador1.moedas
                jogador1.moedas -= 20
                backup_runa = runa_jogador1.dano
                runa_jogador1.declarar_runa()
                print(f"""
{jogador1.nome}:

    Runa: {runa_jogador1.tipo}
    Dano: ???(Lute para revelar)
    Moedas restantes: {jogador1.moedas}
""")
            else:
                print("""
Moedas insuficientes.
""")
        elif escolha1 == 3:
            print(f"""
{jogador1.nome} preferiu pular a loja
""")
            pass
        else:
            print('O valor inserido não é correspondente. Tente novamente.')   
            continue
        
        try:   
            escolha2 = int(input(f'    {jogador2.nome}, escolha:\n    Moedas: {jogador2.moedas}\n    => '))
        except ValueError:
            if escolha1 == 1:
                arma_jogador1.dano = backup_dano_arma
                jogador1.moedas = backup_moedas
            elif escolha1 == 2:
                runa_jogador1.dano = backup_runa
                jogador1.moedas = backup_moedas
            else:
                pass
            print('O valor inserido não é um número. Tente novamente.')
            print('\nOs jogadores devem escolher novamente seus itens')
            continue
        if escolha2 == 1:
            if jogador2.moedas >= 40:
                jogador2.moedas -= 40
                arma_jogador2.forjar()
                print(f"""
{arma_jogador2.tipo} foi aprimorada!
Dano: ???(Lute para revelar)
Moedas Restantes: {jogador2.moedas}
""")
            else:
                print("""
Moedas insuficientes.
""")
        elif escolha2 == 2:
            if jogador2.moedas >= 20:
                jogador2.moedas -= 20
                runa_jogador2.declarar_runa()
                print(f"""
{jogador2.nome}:

    Runa: {runa_jogador2.tipo}
    Dano: ???(Lute para revelar)
    Moedas Restantes: {jogador2.moedas}
""")
            else:
                print("""
Moedas insuficientes.
""")
        elif escolha2 == 3:
            print(f"""
{jogador2.nome} preferiu pular a loja
""")
            pass
        else:
            if escolha1 == 1:
                arma_jogador1.dano = backup_dano_arma
                jogador1.moedas = backup_moedas
            elif escolha1 == 2:
                runa_jogador1.dano = backup_runa
                jogador1.moedas = backup_moedas
            else:
                pass
            print('O valor inserido não é correspondente. Tente novamente.')
            print('\nOs jogadores devem escolher novamente seus itens')
            continue
        return True
    
def fluxo_principal():
        
    if not validar("""
Duelo AFK - 2 Jogadores

Iniciar?

    [1] Sim
    [2] Fechar Jogo
    
    => """):
        return
        
    regras()
    nomear()
    definir_arma()
    identificar_runa()
        
    while True:
        
        if not validar("""
Iniciar confronto?

    [1] Sim
    [2] Fechar Jogo

    => """):
            break
        if not confronto():
            break
        if not validar("""
Visualizar detalhes dos jogadores?

    [1] Sim
    [2] Fechar jogo

    => """):
            break
        status()
        if not validar("""
Abrir loja de aprimoramentos?

    [1] Sim
    [2] Fechar jogo
    
    => """):
            break
        loja()
        
