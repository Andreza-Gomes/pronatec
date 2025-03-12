def conversar_dolar_real(valor_dolar):
    valor_real = valor_dolar * 5.79 
    return valor_real

valor_dolar = float(input("digite o valor em dolar: ")) 
valor_real = conversar_dolar_real(valor_dolar)

print(f"0 valor de ${valor_dolar: .1f} em real e de R${valor_real: .2f} ")