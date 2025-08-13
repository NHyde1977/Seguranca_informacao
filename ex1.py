def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        return None

def cifrar_invertido(texto):
    return texto[::-1]

def salvar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

nome_arquivo = input("Digite o nome do arquivo (.txt) que deseja cifrar: ")
conteudo = carregar_arquivo(nome_arquivo)

if conteudo is None:
    exit()

print('Selecione a opção desejada abaixo:')
print('1 - Inverter mensagem')
print('2 - Deslocar letras')
print('3 - Usar máscara personalizada')

userchoice = int(input('Digite a opção desejada (1, 2 ou 3): '))

if userchoice == 1:
    resultado = cifrar_invertido(conteudo)
    print("Mensagem invertida:")
    print(resultado)
    salvar_arquivo("saida_invertida.txt", resultado)

elif userchoice == 2:
    try:
        numdesc = int(input("Quantas letras você deseja deslocar? Selecione um número de 0 até 27: "))
        if 0 <= numdesc <= 27:
            print(f'Você escolheu deslocar {numdesc} caracteres. Confira o conteúdo cifrado abaixo e também no novo arquivo')
        else:
            print(f'Você escolheu um número fora do intervalo indicado')
    except ValueError:
        print(f'Você digitou um valor inválido e explodiu a cabeça do programa')

elif userchoice == 3:
    print("teste 3")

else:
    print(f'Você não selecionou uma opção válida! isso explodiu a cabeça do programa')