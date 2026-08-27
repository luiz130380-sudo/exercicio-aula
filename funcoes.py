def saudacao():
    """realiza a saudação a todos"""
    print("bem-vindo a aula de fuções")


def saudar_nome(nome:str):
    """realiza a saudação a um nome especifico"""
    print(f"ola {nome}")
    saudacao()


def somar(numUm: float, numDois: float) -> float:
    """Retorna a soma de dois numero"""
    return numUm + numDois

def calcular_media(notas:list[float]) -> float:
    """calcula e retorna a média das notas"""
    if not notas:
        return 0

    return sum(notas) / len(notas)


def calcular_desconto(valor:float, percentual:float=10.0) -> float:
    """
    calcula o valor com desconto.

    args:
        valor: preço original
        precentual: percentual de desconto (padrão 10%)

    returns:
        valor com desconto aplicado
    """
    desconto = valor * (percentual/100)
    return desconto

def  somar_multiplicar(numUm: int, numDois: int) -> tuple[int, int]:
    """função realiza a soma é a multiplicação dso números"""
    return numUm+numDois,numUm*numDois

 # saudacao() --> comentar a linha:
 # saudar_nome("luiz gusatvo")   

 # resultado = somar(5,8)
 # print(f"o resultado da soma é {resultado}")

 # media = calcular_media([4,6])
 # print(f"A nota fibnal do aluno é {media}")

 # resultado = calcular_desconto(100)
 # print(f"o resultado do desconto padrão é {resultado}")

 # resultado = calcular_desconto(100,30)
 # print(f"o resultado do desconto padrão é {resultado}")

# soma,vezes = somar_multiplicar(5, 14)
# print(f"resultado da soma é {soma}")
# print(f"resultado da multiplicação é {vezes}")

somarlambda = lambda numUm,numDois: numUm+numDois
print(f"o resultado da soma é{somarlambda(2,2)}")