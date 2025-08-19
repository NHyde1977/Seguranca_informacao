import string

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        return None


def cifrar_invertido(texto):
    return texto[::-1]


def deslocar_letras(texto, numdesc):
    conteudo_cifrado = ""

    alfabeto_low = list(string.ascii_lowercase)
    alfabeto_up = list(string.ascii_uppercase)

    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                posicao = (alfabeto_low.index(caracter) + numdesc) % 26
                conteudo_cifrado += alfabeto_low[posicao]

            else:
                posicao = (alfabeto_up.index(caracter) + numdesc) % 26
                conteudo_cifrado += alfabeto_up[posicao]
        else:
            conteudo_cifrado += caracter

    return conteudo_cifrado


def salvar_arquivo(nome_arquivo, nome_metodo, conteudo):
    novo_arquivo = nome_arquivo.split(".")[0]
    with open(novo_arquivo + "-" + nome_metodo, 'w', encoding='utf-8') as f:
        f.write(conteudo)


if __name__ == '__main__':

    nome_arquivo = input("Digite o nome do arquivo (.txt) que deseja cifrar: ")
    conteudo = carregar_arquivo(nome_arquivo)

    if conteudo is None:
        exit()

    print('Selecione a opção desejada abaixo:')
    print('1 - Inverter mensagem')
    print('2 - Deslocar letras')
    print('3 - Usar máscara personalizada')

    userchoice = int(input('Digite a opção desejada (1, 2 ou 3): '))

    print(conteudo)

    if userchoice == 1:
        resultado = cifrar_invertido(conteudo)
        print("Mensagem invertida:")
        print(resultado)
        salvar_arquivo(nome_arquivo, "deslocar_letras.txt", resultado)

    elif userchoice == 2:
        try:
            numdesc = int(input("Quantas letras você deseja deslocar? Selecione um número de 0 até 27: "))

            if 0 <= numdesc <= 27:
                resultado = deslocar_letras(conteudo, numdesc)
                print(
                    f'Você escolheu deslocar {numdesc} caracteres. Confira o conteúdo cifrado abaixo e também no novo arquivo')
                print(resultado)
                salvar_arquivo(nome_arquivo, "saida_invertida.txt", resultado)

            else:
                print(f'Você escolheu um número fora do intervalo indicado')

        except ValueError:
            print(f'Você digitou um valor inválido e explodiu a cabeça do programa')

    elif userchoice == 3:
        print("teste 3")

    else:
        print(f'Você não selecionou uma opção válida! isso explodiu a cabeça do programa')
