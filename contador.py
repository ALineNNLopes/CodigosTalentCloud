def contar_caracteres(texto):
    return len(texto)

def contar_palavras(texto):
    return len(texto.split())

while True:
    opcao = input("\nEscolha a opção: \n 1. Contar caracteres\n 2. Contar palavras\n 3. Sair\n Digite o número da opção desejada:\n")

    if opcao == '1':
        texto = input("Insira um texto: ")
        print(f"Número de caracteres: {contar_caracteres(texto)}")
    elif opcao == '2':
        texto = input("Insira um texto: ")
        print(f"Número de palavras: {contar_palavras(texto)}")
    elif opcao == '3':
        print("Saída do programa")
        break
    else:
        print("Opção inválida. Tentar novamente.")