def verificar_numero(valor_largura, valor_altura, valor_comprimento):
    try:
        valor_largura = float(valor_largura)
        valor_altura = float(valor_altura)
        valor_comprimento = float(valor_comprimento)
    except ValueError:
        return f'ALGUM VALOR INVÁLIDO!!'
        