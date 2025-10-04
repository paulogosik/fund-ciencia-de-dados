def somatorio(n: int) -> None:
    i = 0
    result = 0
    while i <= n:
        result += i
        i += 1
    return result


def somatorio_ao_quadrado(n: int) -> None:
    i = 0
    result = 0
    while i <= n:
        result += i * i
        i += 1
    return result


def soma_dados(conjunto: list) -> int:
    result = 0
    for i in conjunto:
        result += i
    return result


def soma_dados_ao_quadrado(conjunto: list) -> int:
    result = 0
    for i in conjunto:
        result += i * i
    return result


def media(conjunto: list, casas_decimais=2) -> float:
    cont = val = 0
    for i in conjunto:
        cont += 1
        val += i
    media = val/cont
    return f'{media:.{casas_decimais}f}'


def media_harmonica(conjunto: list, casas_decimais=2) -> float:
    cont = val = 0
    for i in conjunto:
        cont += 1
        val += 1/i
    media_harmonica = cont/val
    return f'{media_harmonica:.{casas_decimais}f}'


def media_geometrica(conjunto: list, casas_decimais=2) -> float:
    val = 1
    cont = len(conjunto)
    for i in conjunto:
        val *= i
    media_geometrica = val ** (1/cont)
    return f'{media_geometrica:.{casas_decimais}f}'


def main() -> None:
    print("------------Somatório")
    print(somatorio(n=7))
    print("")
    
    print("------------Somatório ao quadrado")
    print(somatorio_ao_quadrado(n=4))
    print("")
    
    print("------------Somatório de conjunto")
    conjunto = [5, 4, 3, 2, 8, 8]
    print(soma_dados(conjunto=conjunto))
    print("")
    
    print("------------Somatório de conjunto ao quadrado")
    conjunto_ao_quadrado = [1, 7, 4, 9, 3, 2, 0]
    print(soma_dados_ao_quadrado(conjunto=conjunto_ao_quadrado))
    print("")
    
    conjunto_medias = [
        1.86,
        1.75,
        1.82,
        1.7,
        1.68,
        1.8,
        1.87,
        1.5,
        1.68,
        1.85,
        2.01,
        1.79,
        1.78,
        1.86,
        1.70,
        1.85,
        1.68,
        1.75,
        1.71,
        1.8,
        1.85,
        1.85,
        1.72
    ]
    
    print("------------Média")
    print(media(conjunto=conjunto_medias))
    print("")
    
    print("------------Média harmônica")
    print(media_harmonica(conjunto=conjunto_medias))
    print("")
    
    print("------------Média geométrica")
    print(media_geometrica(conjunto=conjunto_medias))
    print("")
    

if __name__ == "__main__":
    main()