from dataclasses import dataclass
import random as r

@dataclass
class Arma:
    tipo: str = ''
    dano: int = 0
    
    def declarar_arma(self, escolha):
    
        if escolha == 1:
            self.tipo = 'Adaga'
        elif escolha == 2:
            self.tipo = 'Espada'
        elif escolha == 3:
            self.tipo = 'Machado'
        elif escolha == 4:
            self.tipo = 'Alabarda'
        elif escolha == 5:
            self.tipo = 'Clava'
        
        self.dano = r.randint(5,10)
                          
    def forjar(self):
        self.dano += r.randint(20,30)

@dataclass 
class Runas:
    tipo: str = f'[Ainda não adquirido]'
    dano: int = 0
    
    def declarar_runa(self):
        
        runa = r.randint(5,35)
        if runa > self.dano:  
            if runa >= 30:
                self.tipo = 'Runa Ancestral(30-35)'
            elif runa >= 20 and runa <= 29:
                self.tipo = 'Runa Sombria(20-29)'
            elif runa >= 10 and runa <= 19:
                self.tipo = 'Runa Mágica(10-19)'
            else:
                self.tipo = 'Runa Arqueológica(5-9)'
            self.dano = runa
        elif runa < self.dano:
            print("""
A Runa recebida é inferior á Runa equipada,
portanto será descartada e o dano revelado durante o confronto
será o mesmo de antes""")
        else:
            print("""
A Runa recebida tem o mesmo valor da Runa equipada,
portanto será descartada e o dano revelado durante o confronto
será o mesmo de antes""")
            
@dataclass      
class Jogador:
    nome: str = ''
    moedas: int = 0
    vitorias: int = 0



        