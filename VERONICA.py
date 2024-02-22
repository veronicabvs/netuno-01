import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, email, senha):
        self.nome = nome
        self.data_nascimento = data_nascimento 
        self.email = email
        self.senha = senha

def cadastrar_usuario():
    print("=== TELA DE CADASTRO ===")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirmar_senha = input("Confirmar senha: ")
    
    data_atual = datetime.date.today()
    ano_atual = data_atual.year
    
    try:
        dia, mes, ano = map(int, data_nascimento.split('/'))
        idade = ano_atual - ano - ((data_atual.month, data_atual.day) < (mes, dia))
        if idade < 18:
            print("Opa! O cadastro só é permitido para maiores de idade!")
            return None
    except ValueError:
        print("Opa! Data de nascimento inválida, verifique!")
        return None
    
    if senha != confirmar_senha:
        print("Opa, as senhas não coincidem!")
        return None

    usuario = Usuario(nome, data_nascimento, email, senha)
    print("Oba! Sucesso no cadastro!")
    return usuario

def tela_login(usuario):
    print("\n=== TELA DE LOGIN ===")
    tentativas = 0
    while tentativas < 3:
        email = input("E-mail: ")
        senha = input("Senha: ")
        if email == usuario.email and senha == usuario.senha:
            print("Sucesso no login!")
            return email
        else:
            print("Opa, e-mail ou senha incorretos. Tente até mais duas vezes.")
            tentativas += 1
    print("Ixe! Você excedeu o número de tentativas. Encerrando o programa.")

def main():
    email = ""
    usuario = cadastrar_usuario()
    if usuario:
       email = tela_login(usuario)
    
    if email:
       tela_jogo()
    if not usuario:
        return

class Jogador:
    def __init__(self, classe, avatar, montaria):
        self.classe = classe 
        self.avatar = avatar 
        self.montaria = montaria

def tela_jogo():
    print("\n=== TELA DO JOGO ===") 
    print("Escolha seu player:")
    print("1) Paladino [lança e escudo]") 
    print("2) Atirador [Arma]")
    print("3) Guerreiro [Espada e Escudo]") 
    print("4) Bárbaro [Machado ou Marreta]") 
    print("5) Arqueiro [Arco]")
    
    opcao_classe = input("Escolha: ")
    classes = {
        "1": "Paladino", "2": "Atirador", "3": "Guerreiro", "4": "Bárbaro", "5": "Arqueiro"
    }
    
    classe_escolhida = classes.get(opcao_classe) 
    if classe_escolhida is None:
        print("Opa, escolha inválida.") 
        return
    
    print("Agora as características físicas do player:")
    cor_cabelo = input("Cor de cabelo: ")
    cor_pele = input("Cor de pele: ")
    avatar = {"cor_cabelo": cor_cabelo, "cor_pele": cor_pele}
    
    if classe_escolhida == "Paladino": 
        arma_batalha = "lança ou escudo"
    elif classe_escolhida == "Atirador": 
        arma_batalha = "arma"
    elif classe_escolhida == "Guerreiro": 
        arma_batalha = "espada e escudo"
    elif classe_escolhida == "Bárbaro": 
        arma_batalha = "machado ou marreta"
    elif classe_escolhida == "Arqueiro": 
        arma_batalha = "arco"
    else:
        arma_batalha = "indefinida"
    
    print("Escolha sua montaria:") 
    print("1) Panda")
    print("2) Cavalo")
    print("3) Dragão")
    print("4) Lobo")
    print("5) Tigre")
    opcao_montaria = input("Escolha: ")
    montarias = { 
        "1": "Panda", "2": "Cavalo", "3": "Dragão", "4": "Lobo", "5": "Tigre"
    }
    
    montaria_escolhida = montarias.get(opcao_montaria) 
    if montaria_escolhida is None:
        print("Opa, escolha inválida.") 
        return
    
    atributos_classe = {
        "Paladino": {"Vida": 85, "Mana": 35, "Velocidade de Ataque": 1.25}, 
        "Atirador": {"Vida": 80, "Mana": 25, "Velocidade de Ataque": 1.50}, 
        "Guerreiro": {"Vida": 90, "Mana": 30, "Velocidade de Ataque": 1.00}, 
        "Bárbaro": {"Vida": 95, "Mana": 20, "Velocidade de Ataque": 1.75}, 
        "Arqueiro": {"Vida": 75, "Mana": 40, "Velocidade de Ataque": 1.10}
    }
    
    atributos_montaria = {
        "Panda": {"Velocidade": "3m/s", "Tempo para descanso": "5 minutos"}, 
        "Cavalo": {"Velocidade": "4m/s", "Tempo para descanso": "4 minutos"}, 
        "Dragão": {"Velocidade": "5m/s", "Tempo para descanso": "3 minutos"}, 
        "Lobo": {"Velocidade": "6m/s", "Tempo para descanso": "2 minutos"},
        "Tigre": {"Velocidade": "7m/s", "Tempo para descanso": "1 minuto"}
    }
    
    print(f"\n=== INFORMAÇÕES DA ESCOLHA ===") 
    print(f"Classe escolhida: {classe_escolhida}") 
    print(f"Armas de batalha: {arma_batalha}") 
    print(f"Player: {avatar}")
    print(f"Montaria: {montaria_escolhida}")
    
    print("\n=== CARACTERÍSTICAS DO PLAYER ===")
    for atributo, valor in atributos_classe[classe_escolhida].items():
        print(f"{atributo}: {valor}")
    
    print("\n=== CARACTERÍSTICAS DA MONTARIA ===")
    for atributo, valor in atributos_montaria[montaria_escolhida].items():
        print(f"{atributo}: {valor}")

if __name__ == "__main__": 
    main()