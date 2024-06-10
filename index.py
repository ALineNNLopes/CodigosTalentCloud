produtos = [
    {"nome":"blusa","preco": 47.00},
    {"nome":"acessorio","preco": 52.00},
    {"nome":"sapato","preco": 101.00},
    {"nome":"joia","preco": 90.00},
    {"nome":"calca","preco": 85.00},
    {"nome":"short","preco": 49.90}
]

def classificar(preco):
    if preco < 50.00:
        return "Baixo"
    elif 50.00 <= preco <= 100.00:
        return "Medio"
    else:
        return "Alto"

def processamento(lista_de_produtos):
    for produto in lista_de_produtos:
        preco = produto["preco"]
        categoria = classificar(preco)
        produto["categoria"] = categoria


