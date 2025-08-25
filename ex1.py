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

def aplicar_mascara(texto, mascara):
    conteudo_cifrado = ""
    for caracter in texto:
        if caracter.lower() in mascara:  # substitui mantendo maiúscula~minúscula
            simbolo = mascara[caracter.lower()]
            conteudo_cifrado += simbolo.upper() if caracter.isupper() else simbolo
        else:
            conteudo_cifrado += caracter
    return conteudo_cifrado

def salvar_arquivo(nome_arquivo, nome_metodo, conteudo):
    try:
        base = nome_arquivo.rsplit(".", 1)[0]   # pegará só o nome antes da extensão
        novo_nome = f"{base}-{nome_metodo}.txt" # vai montar o novo nome final
        with open(novo_nome, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"Resultado salvo em {novo_nome}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

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
        salvar_arquivo(nome_arquivo, "invertida", resultado)

    elif userchoice == 2:
        try:
            numdesc = int(input("Quantas letras você deseja deslocar? Selecione um número de 0 até 27: "))

            if 0 <= numdesc <= 27:
                resultado = deslocar_letras(conteudo, numdesc)
                print(
                    f'Você escolheu deslocar {numdesc} caracteres. Confira o conteúdo cifrado abaixo e também no novo arquivo')
                print(resultado)
                salvar_arquivo(nome_arquivo, "deslocar_letras", resultado)

            else:
                print(f'Você escolheu um número fora do intervalo indicado')

        except ValueError:
            print(f'Você digitou um valor inválido!')

    elif userchoice == 3:
        mascara = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '|_|',
            'á': '@', 'à': '4', 'ã': 'ã̃', 'â': '^a',
            'é': '&', 'ê': '€',
            'í': '!',
            'ó': '°', 'ô': 'ö', 'õ': 'õ̃',
            'ú': 'µ', 'ü': 'ü̈',
            'ç': '¢',
            'b': '8', 'c': '(', 'd': '|)', 'f': '#', 'g': '9', 'h': '}{',
            'j': '_|', 'k': '|<', 'l': '1_', 'm': '(V)', 'n': '|\\|',
            'p': '|*', 'q': '0_', 'r': '12', 's': '$', 't': '7',
            'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/', 'z': '2',
            '.': '*', ',': '~', '!': '¡', '?': '¿', ';': ':', ':': ';',
            '"': '”', "'": '`', '(': '[', ')': ']', '-': '_', '_': '-',
        }

        resultado = aplicar_mascara(conteudo, mascara)
        print("Mensagem com máscara personalizada:")
        print(resultado)
        salvar_arquivo(nome_arquivo, "saida_mascara", resultado)

    else:
        print(f'Você não selecionou uma opção válida!')
