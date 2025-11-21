from services import salvar_valor

if __name__ == "__main__":
    valor = input("Digite o nome do valor a ser salvo: ")
    registro = salvar_valor(valor)
    print(f"Valor salvo com ID: {valor.id} e Nome: {valor.nome}")